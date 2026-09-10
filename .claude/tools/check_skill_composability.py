#!/usr/bin/env python3
"""Механическая проверка скиллов агента против Composability & Tooling Gate
(`.claude/rules/02-execution-gates.md`). Выдаёт факты, не вердикт — решение,
монолит это или нет, нужен ли код, остаётся за Engineer/владельцем, скрипт
только считает.

Не заменяет skill-auditor (тот нормализует ДОНОРСКИЕ скиллы под стандарт
frontmatter/структуры при интеграции) — это отдельная, узкая проверка уже
установленных скиллов любого агента на три конкретные вещи из
`docs/architecture/pipeline-architecture.md` §3:
  1. Сколько в SKILL.md заголовков "## Модуль N" — сигнал монолита (Правило 3 Anthropic).
  2. Есть ли рядом `tools/` или `scripts/` с хотя бы одним файлом, и есть ли в тексте
     признаки того, что скилл прозой описывает формулу/расчёт без ссылки на реальный
     скрипт.
  3. Соответствует ли наличие/отсутствие кода заявленному типу скилла (необязательное
     frontmatter-поле `type:`) — протокольный/ревью-скилл не обязан иметь код,
     скилл, заявленный как tool/calculator, обязан.

Использование: python3 check_skill_composability.py <путь к .claude/skills агента>
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

MODULE_HEADER_RE = re.compile(r"(?m)^##\s+Модуль\s+\d+")
FRONTMATTER_RE = re.compile(r"(?s)^---\s*\n(.*?)\n---\s*\n")
TYPE_FIELD_RE = re.compile(r"(?m)^type:\s*(\S+)")

# Скилл заявлен как дисциплина/протокол/ревью — не обязан иметь исполняемый код,
# даже если в тексте встречаются слова расчёта (может описывать чужую формулу,
# не считать сам). Не блокирующий список — только снимает флаг №2 для этих типов.
CODE_EXEMPT_TYPES = {"protocol", "review", "thinking"}
# Скилл заявлен как инструмент/калькулятор — отсутствие кода само по себе находка.
CODE_REQUIRED_TYPES = {"tool", "calculator"}

# Эвристика "похоже на детерминированный расчёт прозой" — не строгая, только сигнал
# для человека, не автоматический провал. Язык-нейтральная и домен-нейтральная:
# общие слова расчёта на русском и английском, без словаря конкретного домена
# (ипотека/кредит/аренда и т.п. — это дело конкретного агента, не системного чекера).
CALC_SIGNAL_RE = re.compile(
    r"(формул[а-я]*|рассчит[а-я]*|вычисл[а-я]*|процент[а-я]*"
    r"|\bformula\b|\bcalculat(?:e|es|ed|ing|ion)\b|\bcompute[sd]?\b|\bpercentage\b)",
    re.IGNORECASE,
)


def read_type(text: str) -> str:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "unspecified"
    type_match = TYPE_FIELD_RE.search(match.group(1))
    return type_match.group(1).lower() if type_match else "unspecified"


def has_code(skill_dir: Path) -> bool:
    for dirname in ("tools", "scripts"):
        d = skill_dir / dirname
        if d.is_dir() and any(d.iterdir()):
            return True
    return False


def audit_skill(skill_dir: Path) -> dict:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {"name": skill_dir.name, "error": "SKILL.md отсутствует"}

    text = skill_md.read_text(encoding="utf-8")
    module_headers = MODULE_HEADER_RE.findall(text)
    skill_type = read_type(text)
    code_present = has_code(skill_dir)
    calc_signals = len(CALC_SIGNAL_RE.findall(text))

    flags = []
    if len(module_headers) >= 2:
        flags.append(f"составной: {len(module_headers)} заголовков '## Модуль N' — кандидат на разбиение (Правило 3)")
    if calc_signals > 0 and not code_present and skill_type not in CODE_EXEMPT_TYPES:
        flags.append(f"{calc_signals} признак(ов) расчёта в тексте без tools/scripts (Правило 2)")
    if skill_type in CODE_REQUIRED_TYPES and not code_present:
        flags.append(f"тип '{skill_type}' подразумевает код, но tools/ и scripts/ пусты или отсутствуют")

    return {
        "name": skill_dir.name,
        "type": skill_type,
        "module_headers": len(module_headers),
        "has_code": code_present,
        "calc_signals_without_code": calc_signals if not code_present else 0,
        "flags": flags,
    }


def main() -> None:
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    if len(sys.argv) != 2:
        print(f"Использование: python3 {sys.argv[0]} <путь к .claude/skills агента>", file=sys.stderr)
        sys.exit(2)

    skills_root = Path(sys.argv[1])
    if not skills_root.is_dir():
        print(f"Не найдена директория: {skills_root}", file=sys.stderr)
        sys.exit(2)

    results = [audit_skill(d) for d in sorted(skills_root.iterdir()) if d.is_dir()]
    flagged = [r for r in results if r.get("flags")]

    print(json.dumps(results, ensure_ascii=False, indent=2))
    print(f"\nВсего скиллов: {len(results)}. С замечаниями: {len(flagged)}.", file=sys.stderr)


if __name__ == "__main__":
    main()
