# FOUNDATION-репозиторий на Рабочем столе — разобран и слит

Category: decisions_and_constraints

Дата: 2026-09-09

## Контекст

Владелец перенесла репозиторий `FOUNDATION` на Рабочий стол и уже выбросила устаревшие монолитные шаблоны (`HOME.md`, `SOUL.md`, `UPDATE.md`, старый скилл-установщик). Остаток — `DECISIONS.md` и `instructions/*.md` (7 файлов: `capability-resolver.md`, `direct-reading-policy.md`, `direct-response-policy.md`, `epistemic-markers.md`, `memory-rules.md`, `pre-task-check.md`, `verify-before-analyze.md`) — разобран полностью, лично, файл за файлом.

## Что нашлось

Все 7 файлов `instructions/` оказались **более старыми снимками** тех же самых правил, что уже живут в `.claude/rules/ENGINEER` — только без вчерашней (2026-09-09) чистки: там ещё встречаются ссылки на `HOME.md`, `DECISIONS.md`, `LIFECYCLE.md`, `UPDATE.md`. То есть `.claude/rules/` ENGINEER уже был впереди источника по содержанию — переносить контент не потребовалось, только убедиться в этом сверкой (сделано, построчно).

`DECISIONS.md` — реальная история из 6 записей, из них 5 Locked и 1 Proposal:

| Решение | Статус | Что с ним |
|---|---|---|
| Capability Resolver: та же дисциплина перед «источник недоступен» (2026-08-28) | Locked | Уже есть в `.claude/rules/capability-resolver.md` |
| Новое правило: неясна природа данных — вопрос до текста (2026-08-26) | Locked | Уже есть в `.claude/rules/verify-before-analyze.md` |
| Материал для разговора читает сам агент (2026-08-26) | Locked | Уже есть в `.claude/rules/direct-reading-policy.md` |
| «Высокий радиус поражения» → пропорциональная проверка (2026-08-13) | Locked | **Перенесено сегодня** — раньше жило только как обрывочная цитата без источника (сама цитата случайно осиротела при вчерашней чистке `DECISIONS.md`-цепочки); теперь полноценный Proportional Review Gate в `.claude/rules/pre-task-check.md` |
| Универсальный pre-task check (2026-08-13) | Locked | Уже есть в `.claude/rules/pre-task-check.md` (8 вопросов) |
| Поле «Последствия» в формат записи решений (2026-08-11) | **Proposal**, не Locked | Не перенесено — у нас больше нет `DECISIONS.md`-механизма как такового (сама цепочка `DECISIONS.md`/`LIFECYCLE.md`/`UPDATE.md`/`workspace/` признана рудиментом и удалена 2026-09-09, см. `MEMORY.md`), формат записи решений не актуален. Идея сама по себе (фиксировать не только «почему», но и «чем жертвуем») осталась не решённой ни тогда, ни сейчас — если понадобится, решать заново с нуля, не как автоматическое продолжение старого Proposal |

## Проверено отдельно

`.claude/settings.json` FOUNDATION и ENGINEER — блок `deny` (node_modules/dist/build/__pycache__/.venv/venv/vendor/*.min.js/package-lock.json/poetry.lock) идентичен в обоих. Разница только в `allow` (ENGINEER без Firecrawl — уже осознанное решение от вчерашнего MCP-аудита, не расхождение).

Скиллы `.claude/skills/` (11 папок) и их учёт — тоже сверено, без расхождений: 5 через `skills-lock.json` (`code-review`/`diagnosing-bugs`/`git-guardrails-claude-code`/`grilling`/`writing-for-agents`, все из `mattpocock/skills`), 4 через `registry.json` Skill System (`find-skills`/`handoff`/`yagni-ladder`/`knowledge-wiki`), 2 — заявленная инфраструктура движка (`skill-authoring`/`skill-auditor`, `CLAUDE.md` §7). Каждый скилл учтён ровно один раз, ровно там, где положено по его происхождению.

## Вывод

Сама папка `FOUNDATION` на Рабочем столе не удалена — только прочитана. Решение, удалять ли её или архивировать, за владельцем.

## Связанные страницы

- нет — первая страница этой темы
