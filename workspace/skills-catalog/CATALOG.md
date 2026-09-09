# CATALOG — реестр каталога навыков экосистемы

Дашборд по всем скиллам, перенесённым из центральной `Skill System/` в `workspace/skills-catalog/` (полный протокол переноса — [`AUDIT_LOG.md`](AUDIT_LOG.md) рядом с этим файлом). Каждый скилл лежит в своей папке `<Кластер>/<имя>/SKILL.md` (+ `references/`/`examples/`/`scripts/` по месту).

## Базовая сетка кластеров — не потолок

Текущие 5 кластеров (Multi-Agent & Orchestration, Engineering & Architecture, Quality Gates & Foundation, Strategy Marketing & Growth, Documents Knowledge & Formats) — это стартовая сетка, не закрытый список. **Engineer имеет право и обязан открывать новые кластеры** под новые домены по мере того, как экосистема обрастает агентами вне текущего охвата (юридический, финансовый, HR и т.д.) — не пытаться силой втиснуть скилл нового домена в одну из пяти существующих корзин, если по смыслу он не подходит ни в одну.

## Статусы

- **[INBOX]** — перенесён и нормализован, лежит в каталоге, не подключён ни одному агенту.
- **[ACTIVE]** — смонтирован в `.claude/skills/` конкретного агента, реально используется.
- **[DEPRECATED]** — вытеснен более сильной версией (см. протокол ниже) или устарел; остаётся в каталоге для истории, не монтируется заново без отдельного решения.

---

## Протокол селекции: Challenger vs Champion

Применяется всякий раз, когда для роли агента находится новый кандидат-скилл (внешний поиск, донор, следующий проход по Skill System), а по этой же роли в каталоге уже есть покрывающий её [ACTIVE] или [INBOX] скилл ( — «Champion»). Новый кандидат — «Challenger». Сравнение — не автоматическое: Engineer формулирует вывод, решение о `Replace` подтверждает владелец (см. `.claude/rules/pre-task-check.md`, входной гейт).

1. **Match** — Challenger реально закрывает ту же роль, что Champion, а не смежную? Если нет — это не конкурент, заводится отдельной строкой каталога, протокол дальше не идёт.
2. **Compare** — по существу, не по объёму: глубина метода, актуальность (даты/версии), наличие evidence/провенанса, отсутствие фантомных ссылок, соответствие стандарту `skill-authoring`.
3. **Вердикт** — один из трёх, без исключений:
   - **Merge** — Challenger добавляет то, чего у Champion нет, но не отменяет его целиком → взять недостающее, оформить как `references/`-дополнение к Champion (не отдельный скилл-дубликат). Champion остаётся [ACTIVE]/[INBOX].
   - **Replace** — Challenger по всем значимым параметрам сильнее Champion → Champion переводится в **[DEPRECATED]** (запись в каталоге не удаляется, статус меняется, дата и причина фиксируются), Challenger занимает его место и роль.
   - **Reject** — Challenger не даёт преимущества, дублирует по имени, но не по содержанию (см. прецеденты `competitor-profiling`/`competitors` и `taste-capture`/`taste-skill` в этом же переносе — разные функции под похожим названием, слияние их бы испортило) → не заносится в каталог как замена, максимум — отдельная строка своей роли.

Тихий Reject без объяснения запрещён — как и для навыков, отклонённые кандидаты **называются** в отчёте по проверке (что нашли, почему не взяли), не тонут молча.

---

## Реестр

### Multi-Agent & Orchestration

| Кластер | Навык | Статус | Роль агента | Триггер вызова |
|---|---|---|---|---|
| Multi-Agent & Orchestration | dispatching-parallel-agents | [INBOX] | Engineer / универсальный (оркестрация субагентов) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| Multi-Agent & Orchestration | executing-plans | [INBOX] | Engineer / универсальный | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| Multi-Agent & Orchestration | subagent-driven-development | [INBOX] | Engineer / универсальный | Use when executing implementation plans with independent tasks in the current session (fresh subagent per task + two-stage review) |
| Multi-Agent & Orchestration | writing-plans | [INBOX] | Engineer / универсальный | Use when you have a spec or requirements for a multi-step task, before touching code |

### Engineering & Architecture

| Кластер | Навык | Статус | Роль агента | Триггер вызова |
|---|---|---|---|---|
| Engineering & Architecture | andrej-karpathy-skills | [INBOX] | Engineer | Use when writing, reviewing, or refactoring code — overcomplication, surgical changes, surfaced assumptions, verifiable success criteria |
| Engineering & Architecture | architecture-review | [INBOX] | Engineer | После того как задача и профессия агента понятны, до чек-листа «репозиторий готов» — Reliability Architecture / AI Reasoning Boundaries / capability map |
| Engineering & Architecture | claude-api | [INBOX] | Engineer (или любой агент, пишущий код против Claude API) | Имя Claude/Anthropic в любой форме, вопрос про LLM (цены/модель/лимиты/кэш), или задача LLM-shaped без названного провайдера |
| Engineering & Architecture | codebase-design | [INBOX] | Engineer | Use when designing/improving a module's interface, finding deepening opportunities, deciding where a seam goes |
| Engineering & Architecture | domain-modeling | [INBOX] | Engineer | Use when discussing codebase terminology, writing/editing CONTEXT.md, recording/editing an ADR |
| Engineering & Architecture | legacy-repository-audit | [INBOX] | Engineer | Владелец указывает на старый/внешний репозиторий агента и просит проверить перед тем, как строить новое |
| Engineering & Architecture | mcp-builder | [INBOX] | Engineer | Use when building MCP servers to integrate external APIs/services (Python FastMCP или Node/TS MCP SDK) |
| Engineering & Architecture | resolving-merge-conflicts | [INBOX] | Engineer | Use when you need to resolve an in-progress git merge/rebase conflict |
| Engineering & Architecture | reverse-engineering | [INBOX] | Engineer | Нужно узнать, как что-то реально делается лучшими практиками в мире, для одной цели за раз (Intelligence Report с evidence) |
| Engineering & Architecture | systematic-debugging | [INBOX] | Engineer / универсальный | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| Engineering & Architecture | test-driven-development | [INBOX] | Engineer / универсальный | Use when implementing any feature or bugfix, before writing implementation code |
| Engineering & Architecture | tool-selection | [INBOX] | Engineer | Перед тем как начать искать информацию, менять репозиторий или задавать вопрос владельцу |
| Engineering & Architecture | webapp-testing | [INBOX] | Engineer | Тестирование локальных веб-приложений через Playwright — функциональность фронтенда, UI-баги, скриншоты, логи браузера |

### Quality Gates & Foundation

| Кластер | Навык | Статус | Роль агента | Триггер вызова |
|---|---|---|---|---|
| Quality Gates & Foundation | capability-creation-methodology | [INBOX] | Engineer | Задача — построить агента для целой незнакомой профессиональной области, не точечный инструмент |
| Quality Gates & Foundation | capability-recommend | [INBOX] | Engineer / универсальный | Пользователь формулирует рабочую задачу и хочет понять, какие Skills/MCP/инструменты помогут — до ручной работы над задачей |
| Quality Gates & Foundation | claude-md-improver | [INBOX] | Engineer | Use when user asks to check, audit, update, improve, or fix CLAUDE.md files |
| Quality Gates & Foundation | final-quality-gate | [INBOX] | Engineer / универсальный | Перед тем как считать ответ завершённым — Coverage/Evidence/Opportunity/Simplification/Future Problems/Completion/System Opportunity |
| Quality Gates & Foundation | generalization-ladder | [INBOX] | Engineer / универсальный | Любое субъективное наблюдение — Raw Observation → Hypothesis → Recurring Pattern, статус только при независимом повторении |
| Quality Gates & Foundation | grilling | [INBOX] | Универсальный | Use when the user wants to stress-test a plan, decision, or idea, or uses any "grill"/"grill me"/"grill with docs" trigger phrase |
| Quality Gates & Foundation | independent-validation | [INBOX] | Engineer | Новый агент, высокая цена ошибки, сложный архитектурный анализ, или изменение самой методологии |
| Quality Gates & Foundation | outcome-gate | [INBOX] | Универсальный (не для Engineering-домена) | Перед стартом/сохранением артефакта, заявляющего внешний наблюдаемый результат для адресата (решение, структура, метрика) |
| Quality Gates & Foundation | verification-before-completion | [INBOX] | Engineer / универсальный | Use when about to claim work is complete, fixed, or passing — evidence before assertions always |

### Strategy, Marketing & Growth

| Кластер | Навык | Статус | Роль агента | Триггер вызова |
|---|---|---|---|---|
| Strategy, Marketing & Growth | competitor-profiling | [INBOX] | AI Marketing Strategist | Пользователь хочет исследовать/профилировать конкурентов по URL — «competitor research/analysis», конкурентный ландшафт |
| Strategy, Marketing & Growth | competitors | [INBOX] | AI Marketing Strategist | Пользователь хочет создать сравнительные/alternative-страницы для SEO и sales enablement |
| Strategy, Marketing & Growth | content-strategy | [INBOX] | AI Marketing Strategist | Планирование контент-стратегии, выбор тем, «what should I write about», редакционный календарь |
| Strategy, Marketing & Growth | conversion-method | [INBOX] | AI Marketing Strategist | Пишешь текст, убеждающий одного конкретного человека совершить одно действие за одну сессию чтения (лендинг, объявление) |
| Strategy, Marketing & Growth | cro | [INBOX] | AI Marketing Strategist | Оптимизация/увеличение конверсии на маркетинговой странице или форме — «CRO», «эта страница не конвертит» |
| Strategy, Marketing & Growth | idea-calibration | [INBOX] | Engineer | «Входной гейт» (CLAUDE.md) отметил по-настоящему крупное решение — новый агент, смена методологии, редизайн >2 модулей |
| Strategy, Marketing & Growth | lead-magnets | [INBOX] | AI Marketing Strategist | Создание/планирование/оптимизация лид-магнита для email capture — «lead magnet», «gated content», «ebook» |
| Strategy, Marketing & Growth | opportunity-discovery | [INBOX] | Engineer / универсальный | Пользователь делится новой технологией/моделью/инструментом/статьёй — материалом, меняющим пространство возможностей экосистемы |
| Strategy, Marketing & Growth | pricing | [INBOX] | AI Marketing Strategist (справочный материал, не готовое решение) | Нужно понять, что взять за основу для решения по цене/пакетированию — модели ценообразования, аудит pricing-страницы |
| Strategy, Marketing & Growth | revops | [INBOX] | AI Marketing Strategist / Sales-агент (справочный материал) | Нужен справочный материал по устройству CRM/лид-процессов — жизненный цикл лида, скоринг/роутинг |
| Strategy, Marketing & Growth | taste-capture | [INBOX] | Marketing/Brand-агент | Нужно определить эстетическое/творческое/брендовое направление, готового брендбука нет — вкус обнаруживается через реакцию человека |
| Strategy, Marketing & Growth | taste-skill | [INBOX] | Дизайн/фронтенд-агент (пока не собран) | Создание/редизайн лендинга, портфолио или маркетингового сайта — результат не должен выглядеть шаблонным (anti-slop) |
| Strategy, Marketing & Growth | to-questionnaire | [INBOX] | Универсальный (user-invocable only) | Явный вызов — превратить решение, на которое сам агент не может ответить, в анкету для другого человека |
| Strategy, Marketing & Growth | triage | [INBOX] | Универсальный (user-invocable only) | Явный вызов — провести issue/внешний PR через конвейер ролей: категоризация → верификация → grill при нужде → бриф |
| Strategy, Marketing & Growth | youtube-analysis | [INBOX] | AI Marketing Strategist | Пользователь прислал ссылку на YouTube-видео — субтитры → транскрипция → кадры, результат в opportunity-discovery |

### Documents, Knowledge & Formats

| Кластер | Навык | Статус | Роль агента | Триггер вызова |
|---|---|---|---|---|
| Documents, Knowledge & Formats | decision-documentation | [INBOX] | Engineer | Решение переживёт диалог, меняет правила работы, затрагивает файлы устава, или владелец спрашивает «что мы решили по X» |
| Documents, Knowledge & Formats | defuddle | [INBOX] | Универсальный | Вместо WebFetch, когда пользователь даёт URL на статью/документацию/блог-пост для чтения |
| Documents, Knowledge & Formats | doc-coauthoring | [INBOX] | Универсальный | Пользователь хочет написать документацию/proposal/tech spec и выиграет от гайдед-воркфлоу вместо одного черновика |
| Documents, Knowledge & Formats | docx | [INBOX] | Универсальный | Создание/чтение/правка Word-документов (.docx/.dotx) |
| Documents, Knowledge & Formats | humanizer | [INBOX] | Универсальный | Правка прозы на AI-штампы — раздутые claims, sales language, безликая структура, filler |
| Documents, Knowledge & Formats | hyperframes | [INBOX] | Видео-агент (пока не собран) | Mandatory entry point для любого запроса сделать/отредактировать/отрендерить видео, анимацию или motion graphic |
| Documents, Knowledge & Formats | json-canvas | [INBOX] | Универсальный | Работа с .canvas файлами — визуальные канвасы, mind maps, флоучарты, Obsidian Canvas |
| Documents, Knowledge & Formats | obsidian-bases | [INBOX] | Универсальный (Obsidian-контекст) | Работа с .base файлами — database-like виды заметок, table/card views, фильтры, формулы |
| Documents, Knowledge & Formats | obsidian-cli | [INBOX] | Универсальный (Obsidian-контекст) | Взаимодействие с Obsidian vault из командной строки, или разработка/отладка Obsidian-плагинов |
| Documents, Knowledge & Formats | obsidian-markdown | [INBOX] | Универсальный (Obsidian-контекст) | Работа с .md в Obsidian — wikilinks, callouts, frontmatter, embeds, свойства |
| Documents, Knowledge & Formats | pdf | [INBOX] | Универсальный | Любая операция с PDF — чтение/извлечение, merge/split, водяные знаки, формы, OCR |
| Documents, Knowledge & Formats | pptx | [INBOX] | Универсальный | Любая работа с .pptx/.potx — создание/чтение/правка слайд-дек, шаблоны, спикер-ноуты |
| Documents, Knowledge & Formats | tldraw-offline | [INBOX] | Универсальный | Агенту нужно читать/редактировать открытый tldraw-канвас или писать document scripts для реактивных фигур |
| Documents, Knowledge & Formats | visual | [INBOX] | Content/Marketing-агент | Генерация фото/видео/аудио — text-to-image, image-to-video, TTS, апскейл (через VelsVisual CLI + KIE API) |
| Documents, Knowledge & Formats | xlsx | [INBOX] | Универсальный | Любая работа с .xlsx/.csv/.tsv как основным входом/выходом — правка, формулы, чистка данных |

---

**Итого в реестре: 56 скиллов**, все со статусом [INBOX]. Ни один пока не смонтирован ни в один `.claude/skills/`. Источник (`ПРОЕКТЫ/Skill System/`) остаётся read-only для этого каталога — обновления сюда идут через повторный проход `skill-auditor`, не прямой правкой каталога задним числом.
