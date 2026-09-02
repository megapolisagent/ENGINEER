# 2026-09-02 — Задача: Tooling Inventory в repository-design/SKILL.md, закрытие 3 пунктов контрольного аудита, финальный коммит

## Слова владельца (дословно)

«Согласовано, твоё замечание технически абсолютно точное. Никаких фиктивных .mcp.json ради галочки.

1. Зафиксируй в repository-design/SKILL.md именно «Tooling Inventory» по принципу capability-resolver.md:
   - В чек-лист сборки: обязательная фиксация инструментов исполнения (штатные тулы среды, Python-библиотеки в requirements.txt, скрипты автоматизации или внешние MCP при реальной необходимости).
   - Критерий сдачи: подтверждение физической работоспособности инструментальной цепочки на реальном прогоне (а не на словах в промпте).

2. Сделай итоговый git commit всех закрытых пунктов:
   git add -A
   git commit -m "fix(engineer): resolve security gitignore, sync docs, add Tooling Inventory to repository standards"

3. Покажи статус git status — и на этом реформа ENGINEER официально завершена.»

Контекст: контрольный аудит Codex (ID b045ycjic, 2026-09-02) после коммита Data
Contract/Behavioral Contract вернул ACTION REQUIRED по трём пунктам. Один (`.claude/settings.local.json`
не в `.gitignore`) проверен и оказался ложным срабатыванием — файл уже в `.gitignore` и не
отслеживается git, не тронут. Два реальных — README.md ссылался на несуществующий
`decision-documentation/SKILL.md` (и не упоминал реально установленный `skill-authoring`) —
исправлено; отсутствие git у Researcher зафиксировано одной строкой в `OPEN_QUESTIONS.md`
как внешний техдолг, не блокирующий приёмку ENGINEER — сделано. Отдельно отклонена (с
согласия владельца, после явного технического возражения Engineer) буквальная версия
«Tooling & MCP Contract» — MCP путают со штатными инструментами Claude Code
(Read/Write/Bash/WebFetch уже встроены, MCP — отдельный протокол для внешних сервисов) и
с pip-библиотеками (`docxtpl` — не MCP). Согласована замена — «Tooling Inventory» по
принципу `instructions/capability-resolver.md` (потребность → класс инструмента, не
фиктивная инфраструктура).

## Критерий достаточности (зафиксирован до работы)

1. `skills/repository-design/SKILL.md` содержит пункт чек-листа «Tooling Inventory»:
   фиксация реального класса инструмента (штатный тул среды / Python-библиотека в
   requirements.txt / скрипт автоматизации / внешний MCP — только при подтверждённой
   реальной необходимости) для каждой операции агента с внешними данными/сервисами, плюс
   критерий сдачи — подтверждённый реальный прогон цепочки, не декларация в промпте.
2. Все правки этого дня (Data Contract, E2E-приёмка, Behavioral Contract, README-фикс,
   OPEN_QUESTIONS-запись, Tooling Inventory) — в одном финальном коммите.
3. Показан `git status` после коммита.
