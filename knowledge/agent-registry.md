# Agent Registry — статус переноса канона

Единственный источник правды на вопрос «применено ли уже правило X ко всем известным агентам», а не память Engineer о том, что должно было быть сделано.

Пустая ячейка или прочерк = не проверено. Не значит «прошло» — значит «неизвестно», пока не прогнано и не вписана дата.

Эта страница фиксирует текущий статус, не историю его получения — кто нашёл проблему, почему, как чинили — живёт в `git log`/commit message затронутого репозитория, не в теле этой страницы (`.claude/rules/memory-rules.md`, «Целостность документа»).

## Известные агенты

| Агент | Путь | Особенность |
|---|---|---|
| ENGINEER | (себя) | — |
| AI Marketing Strategist | `../AI Marketing Strategist` | — |
| AI Avitolog | `../AI Avitolog` | — |
| AI Legal Constructor | `../AI Legal Constructor` | — |
| AI Intelligence | `../AI Intelligence` | Старый Foundation-канон — `instructions/`, не `.claude/rules/`; `skills/`, не `.claude/skills/` |
| AI Copywriter | `../AI Copywriter` | Собран на чистом каркасе `pipeline-architecture.md` §9 |

Список сверяется, не берётся по памяти — см. `.claude/rules/capability-resolver.md` за тем, как убедиться, что список полон.

## Composability & Tooling Gate

Команда: `python3 .claude/tools/check_skill_composability.py <путь к .claude/skills агента>`. Флаг — сигнал для человека, не автоматический вердикт.

| Агент | Дата прогона | Скиллов | Реальных замечаний |
|---|---|---|---|
| ENGINEER | 2026-09-14 | 11 | 0 |
| AI Marketing Strategist | 2026-09-14 | 12 | 0 |
| AI Avitolog | 2026-09-14 | 10 | 0 |
| AI Legal Constructor | 2026-09-14 | 4 | 0 |
| AI Intelligence | 2026-09-14 | 3 | 0 |
| AI Copywriter | — | — | не прогонялось |

## Confirmation Gate / Входной гейт

Сверено с текущим каноном FOUNDATION (без самопротиворечия «без исключений по осям» + «оси низкие → сразу»).

| Агент | Статус |
|---|---|
| ENGINEER | Актуальная формулировка |
| AI Marketing Strategist | Актуальная формулировка |
| AI Avitolog | Актуальная формулировка |
| AI Legal Constructor | Иная, более старая формулировка — баг не воспроизводится, правка не нужна |
| AI Intelligence | Иная, более старая формулировка — баг не воспроизводится, правка не нужна |
| AI Copywriter | Не проверено |

## Hooks (`guard-rules-bloat.sh`, `block-dangerous-git.sh`) и `data-discipline.md`

| Агент | guard-rules-bloat.sh | block-dangerous-git.sh | data-discipline.md |
|---|---|---|---|
| ENGINEER | ✅ | ✅ | ✅ (`01-data-discipline.md`) |
| AI Marketing Strategist | ✅ | ✅ | ✅ |
| AI Avitolog | ✅ | ✅ | ✅ |
| AI Legal Constructor | ✅ | ✅ | ✅ (3 файла — `ask-before-searching.md` в этом доме не существует) |
| AI Intelligence | ✅ (хук адаптирован под `instructions/`) | ✅ | ✅ (3 файла) |
| AI Copywriter | ❌ отсутствует (нет `.claude/hooks/`) | ❌ отсутствует (нет `.claude/hooks/`) | Не проверено |

## MCP: Windows-баг Claude Code — `npx` без `cmd /c` не стартует (CONNECT_TIMEOUT)

Задокументированный баг Claude Code на Windows (`github.com/anthropics/claude-code/issues/68221`, `#58510`, `#3369`) — MCP-сервер с `"command": "npx"` спавнится напрямую, без shell; `npx` на Windows — `.cmd`-шим, `child_process.spawn` не может выполнить его без `shell: true` (защита после CVE-2024-27980). Проявляется как `CONNECT_TIMEOUT` через 30000мс, не как явная ошибка — воспроизводится даже после рестарта сессии. Прямое рукопожатие с тем же сервером вне спавна Claude Code проходит за секунды — сервер/токен не виноваты. Решение — оборачивать: `"command": "cmd", "args": ["/c", "npx", ...]`.

| Агент | Статус |
|---|---|
| ~/.claude.json (глобально: context7, firecrawl) | ✅ обёрнуто |
| AI Avitolog (apify) | ✅ обёрнуто — **не подтверждено реальным подключением**, ждёт рестарта сессии и проверки Авитологом |
| AI Legal Constructor (clients-db) | ✅ обёрнуто, не проверено (параллельная сессия) |
| AI Marketing Strategist, AI Copywriter | Не применимо — нет project-level `npx`-серверов |
| AI Intelligence | Использует `uvx` (нативный `.exe`, не `.cmd`-шим) — тот же баг не воспроизводится, не трогала |

## MCP: `${VAR}` в `.mcp.json` не резолвится из `settings.local.json`

Задокументированный баг Claude Code (`github.com/anthropics/claude-code/issues/60513`) — `${VAR}` в `env`-блоке `.mcp.json` резолвится только из реальной переменной окружения ОС, не из `settings.local.json`. Проверка: `grep -rn '\${[A-Z_]*}' */.mcp.json` по всем известным агентам; находка требует подтверждения реальной переменной ОС (`[Environment]::GetEnvironmentVariable`) — ключ в `settings.local.json` не считается доказательством.

| Агент | Статус |
|---|---|
| ENGINEER | Не применимо — нет `.mcp.json` |
| AI Marketing Strategist | Чисто — Firecrawl глобальный (`~/.claude.json`) |
| AI Avitolog | Чисто — Firecrawl глобальный, `APIFY_TOKEN` — переменная окружения ОС |
| AI Legal Constructor | Чисто — Firecrawl/Exa глобальные, в `.mcp.json` остался только `clients-db` |
| AI Intelligence | Чисто — Exa глобальный |
| AI Copywriter | Не применимо — нет `.mcp.json`/веб-доступа по дизайну |

## Exa: `web_fetch_exa` может молча отдать устаревший кэш вместо live-данных

MCP-инструмент `mcp__exa__web_fetch_exa` не передаёт параметр свежести API Exa (`maxAgeHours`) — нет способа заставить его дать живой ответ через обычный вызов, и нет сигнала, что ответ пришёл из кэша. Для цены/наличия/любого live-факта — прямой `curl` к `api.exa.ai/contents` с `maxAgeHours: 0` (ключ — переменная окружения `EXA_API_KEY`, поставлена на уровне пользователя ОС).

| Агент | Статус |
|---|---|
| ENGINEER | ✅ `capability-resolver.md` |
| AI Avitolog | ✅ `capability-resolver.md` |
| AI Marketing Strategist | ✅ `tool-preference.md` |
| AI Legal Constructor | Не перенесено — `capability-resolver.md` держит несохранённые правки параллельной сессии |
| AI Intelligence | Не перенесено — базового правила «Exa по умолчанию» там ещё нет вообще, добавлять кэш-оговорку раньше основы преждевременно |
| AI Copywriter | Не применимо — нет веб-доступа по дизайну |

## Веб-доступ по умолчанию — Exa, не встроенные WebSearch/WebFetch

| Агент | Статус |
|---|---|
| ENGINEER | ✅ `capability-resolver.md` |
| AI Marketing Strategist | ✅ `tool-preference.md` |
| AI Avitolog | ✅ `capability-resolver.md` |
| AI Legal Constructor | Не проверено — `capability-resolver.md` держит несохранённые правки параллельной сессии |
| AI Intelligence | Не проверено |
| AI Copywriter | Не проверено |

## Гигиена памяти (`.claude/rules/memory-rules.md`)

| Агент | Статус |
|---|---|
| ENGINEER | ✅ |
| AI Avitolog | ✅ |
| AI Marketing Strategist | Не перенесено |
| AI Legal Constructor | Не перенесено |
| AI Intelligence | Не перенесено |
| AI Copywriter | Не проверено |

## Foundation `instructions/` — состав относительно текущего канона

Критерий: `confirmation-before-action.md` присутствует, `data-discipline.md` консолидирован (не 3 отдельных файла).

| Агент | Статус |
|---|---|
| AI Intelligence | ✅ актуальный состав, 6 файлов |
| AI Marketing Strategist | Не проверено |
| AI Avitolog | Не проверено |
| AI Legal Constructor | Не проверено |

## Мёртвые ссылки на до-миграционный канон (HOME.md/SOUL.md/ROUTING.md/VISION.md)

Проверка после любого переименования/консолидации канонического файла: `grep -rn 'HOME\.md\|SOUL\.md\|ROUTING\.md'` по всему репозиторию агента, не только в файле, ради которого зашли.

| Агент | Статус |
|---|---|
| AI Intelligence | ✅ чисто |
| AI Legal Constructor | ✅ чисто |
| AI Marketing Strategist | Не проверено |
| AI Avitolog | Не проверено |
| AI Copywriter | Не применимо — не мигрировал с этой схемы |

## Как использовать эту страницу

1. **Появилось новое каноническое правило/гейт/хук** — прежде чем считать перенос канона завершённым (`CLAUDE.md` §2, «Синхронизация экосистемы»), пройти по списку агентов выше и вписать реальный статус по каждому, не только по тому, с которым велась текущая сессия.
2. **Начинается значимая доработка конкретного агента** (Canon Sync Gate, `02-execution-gates.md`) — сверить его строку здесь перед началом, не только его собственные файлы: если тут дата прогона Composability Gate отсутствует или старше последнего канонического изменения — прогнать `check_skill_composability.py` заново как часть той же доработки, не откладывать отдельным поводом.
3. Обновлять таблицы по факту, а не переписывать регулярно «на всякий случай» — эта страница фиксирует состояние, не хронику попыток.
