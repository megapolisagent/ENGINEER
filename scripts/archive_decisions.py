#!/usr/bin/env python3
"""Split a DECISIONS.md into an active index + DECISIONS_ARCHIVE.md.

Entries whose status starts with Locked/Отклонено are moved to
<same folder>/DECISIONS_ARCHIVE.md with a one-line stub left behind in the
original file. Open statuses (Proposal, Discussion, Открыт, etc.) stay in
place untouched. Entries already replaced by a stub in a previous run are
left alone (idempotent — safe to run repeatedly as the file grows again).

New archive entries are APPENDED to an existing DECISIONS_ARCHIVE.md, never
overwritten — running this twice must not lose anything already archived.

Usage: python archive_decisions.py <path_to_DECISIONS.md>

Rule that triggers this script (ENGINEER, instructions/pre-task-check.md,
"Size Gate", 2026-09-03): a session touching some repo's DECISIONS.md is not
considered closed while that file exceeds 50 KB or holds more than 10 closed
(Locked/Отклонено) entries — run this script first.
"""
import re
import sys
from pathlib import Path

CLOSED_STATUS_RE = re.compile(r"^Статус:\s*(Locked|Отклонено)\b", re.IGNORECASE)
ALREADY_STUB_RE = re.compile(r"перенесён в `DECISIONS_ARCHIVE\.md`")


def split_file(path: Path, archive_already_has: set[str]):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    journal_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Журнал":
            journal_idx = i
            break
    if journal_idx is None:
        raise SystemExit("Не найден заголовок '## Журнал' — формат файла не совпадает с ожидаемым.")

    preamble = lines[: journal_idx + 1]
    body = lines[journal_idx + 1 :]

    entry_starts = [i for i, l in enumerate(body) if l.startswith("### ")]
    if not entry_starts:
        raise SystemExit("Не найдено ни одной записи '### ' после '## Журнал'.")
    entry_starts.append(len(body))

    entries = [body[entry_starts[i] : entry_starts[i + 1]] for i in range(len(entry_starts) - 1)]

    active_out = []
    new_archive_out = []
    closed_count = 0
    open_count = 0
    skipped_stub_count = 0

    for entry in entries:
        title_line = entry[0]
        status_line = None
        for l in entry[1:6]:
            if l.startswith("Статус:"):
                status_line = l
                break

        already_stub = bool(status_line and ALREADY_STUB_RE.search(status_line))
        is_closed = bool(status_line and CLOSED_STATUS_RE.match(status_line) and not already_stub)

        entry_stripped = entry[:]
        while entry_stripped and entry_stripped[-1].strip() == "":
            entry_stripped.pop()

        if already_stub:
            # Уже заархивировано в прошлый прогон — не трогаем, не дублируем в архив.
            skipped_stub_count += 1
            active_out.extend(entry_stripped)
            active_out.append("")
        elif is_closed:
            if title_line in archive_already_has:
                raise SystemExit(
                    f"Заголовок «{title_line.strip()}» уже есть в DECISIONS_ARCHIVE.md, но в "
                    "основном файле это не заглушка — расхождение, требует ручной проверки, "
                    "не продолжаю автоматически."
                )
            closed_count += 1
            new_archive_out.extend(entry_stripped)
            new_archive_out.append("")
            active_out.append(title_line)
            active_out.append("")
            active_out.append(
                f"{status_line} — полный текст перенесён в `DECISIONS_ARCHIVE.md` (тот же заголовок и дата)."
            )
            active_out.append("")
        else:
            open_count += 1
            active_out.extend(entry_stripped)
            active_out.append("")

    new_main = "\n".join(preamble + [""] + active_out).rstrip() + "\n"
    new_archive_chunk = "\n".join(new_archive_out).rstrip() + "\n" if new_archive_out else ""
    return new_main, new_archive_chunk, closed_count, open_count, skipped_stub_count


def load_existing_archive_titles(archive_path: Path) -> set[str]:
    if not archive_path.exists():
        return set()
    titles = set()
    for line in archive_path.read_text(encoding="utf-8").split("\n"):
        if line.startswith("### "):
            titles.add(line)
    return titles


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python archive_decisions.py <path_to_DECISIONS.md>")

    src = Path(sys.argv[1])
    archive_path = src.parent / "DECISIONS_ARCHIVE.md"
    existing_titles = load_existing_archive_titles(archive_path)

    new_main, new_archive_chunk, closed_count, open_count, skipped = split_file(src, existing_titles)

    print(f"{src}: {closed_count} новых записей в архив, {skipped} уже были заглушками, {open_count} остаются активными")

    if closed_count == 0:
        print("  Новых закрытых записей для архивации нет — файлы не изменены.")
        sys.exit(0)

    if not archive_path.exists():
        header = (
            f"# Архив закрытых решений — {src.parent.name}\n\n"
            "> Полный текст записей `DECISIONS.md` со статусом Locked/Отклонено, вынесенных сюда\n"
            "> для экономии стартового контекста. Ничего не удалено — правило «отклонённые\n"
            "> альтернативы не удаляются» соблюдено полностью, просто вне горячего чтения при старте.\n"
            "> Читать по явной ссылке из `DECISIONS.md` или по запросу владельца, не автоматически.\n"
            "> Новые записи дописываются сюда в конец при каждом запуске archive_decisions.py —\n"
            "> порядок не строго хронологический, ищи по заголовку, не по позиции в файле.\n\n"
            "## Архив\n\n"
        )
        archive_path.write_text(header + new_archive_chunk, encoding="utf-8")
    else:
        with archive_path.open("a", encoding="utf-8") as f:
            f.write("\n" + new_archive_chunk)

    src.write_text(new_main, encoding="utf-8")

    print(f"  {src.name}: {len(new_main.encode('utf-8'))} байт")
    print(f"  {archive_path.name}: {len(archive_path.read_text(encoding='utf-8').encode('utf-8'))} байт")
