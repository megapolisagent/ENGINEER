# AUDIT_LOG — импорт навыков из Skill System в skills-catalog

Журнал разбора центральной библиотеки `ПРОЕКТЫ/Skill System/skills/` (строго read-only источник) по протоколу `skill-auditor`. Каждый взятый скилл нормализуется и копируется в `workspace/skills-catalog/<Кластер>/<имя-скилла>/` (папка `inbox-skills` переименована в `skills-catalog` на этапе финальной сборки — см. запись в самом низу), источник не модифицируется.

**Статус: ЗАВЕРШЕНО.** Разбор всех 5 кластеров закрыт, каталог собран и зарегламентирован — см. итоговую запись в конце файла.

Формат записи: `[Кластер] Имя | Исходный путь | Действие | Заметки`.

---

## [Multi-Agent & Orchestration] dispatching-parallel-agents
- Исходный путь: `Skill System/skills/dispatching-parallel-agents/SKILL.md`
- Действие: Перенесён
- Заметки: без изменений тела — description уже был чистым триггером, внешних привязок не найдено. `evidence.json` не скопирован (не часть канона).

## [Multi-Agent & Orchestration] subagent-driven-development
- Исходный путь: `Skill System/skills/subagent-driven-development/` (SKILL.md + implementer-prompt.md + task-reviewer-prompt.md + re-review-prompt.md + scripts/{sdd-workspace,task-brief,review-package})
- Действие: Перенесён (с нормализацией)
- Заметки: ядро было 503 строки (превышение лимита на 3) — раздел «Example Workflow» вынесен в `examples/example-workflow.md`, ядро стало 441 строка. Убраны 7 фантомных вызовов `superpowers:*` (`using-git-worktrees`, `finishing-a-development-branch` ×3 вкл. 2 узла dot-диаграммы, `requesting-code-review/code-reviewer.md`) — заменены на локальную формулировку без ссылки на несуществующий скилл. Три скрипта и три файла-шаблона промптов скопированы без изменений — самодостаточны, внешних зависимостей нет. Не тронуто: внутреннее имя рабочей директории `.superpowers/sdd/` в скриптах и в двух местах прозы — это чисто косметическая метка каталога (не вызов внешнего инструмента), трогать не стал, чтобы не расходовать скрипты с прозой. `evidence.json` не скопирован.

## [Multi-Agent & Orchestration] executing-plans
- Исходный путь: `Skill System/skills/executing-plans/SKILL.md`
- Действие: Перенесён (с нормализацией)
- Заметки: убрана рекламная фраза про донорский фреймворк «Superpowers» и три фантомных вызова (`superpowers:using-git-worktrees`, `superpowers:subagent-driven-development` → заменён на прямую ссылку на соседний скилл этого же кластера, `superpowers:finishing-a-development-branch` → заменён на прямую инструкцию). description уже был триггер-only. `evidence.json` не скопирован.

## [Multi-Agent & Orchestration] writing-plans
- Исходный путь: `Skill System/skills/writing-plans/SKILL.md` + `plan-document-reviewer-prompt.md`
- Действие: Перенесён (с нормализацией)
- Заметки: убраны 6 упоминаний `superpowers:*` — жёстко зашитый путь сохранения плана `docs/superpowers/plans/` заменён на `docs/plans/`, вызовы `superpowers:subagent-driven-development`/`superpowers:executing-plans` заменены на прямые ссылки на соседние скиллы кластера. `plan-document-reviewer-prompt.md` скопирован без изменений — чист. `evidence.json` не скопирован.

## [Multi-Agent & Orchestration] oh-my-openagent
- Исходный путь: `Skill System/skills/oh-my-openagent/SKILL.md`
- Действие: Пропущен
- Заметки: сам исходник уже помечен прежним аудитом как «не Agent Skill» — справочная запись-указатель на отдельный CLI-харнесс (`bunx oh-my-openagent install`), устанавливаемый целиком поверх всего рантайма. Риск vendor lock-in уже отмечен. Копировать в inbox-skills как «скилл» было бы искажением статуса записи.

---

**Итог кластера Multi-Agent & Orchestration:** 4 перенесено (3 с нормализацией), 1 пропущен. 0 дублей в этом кластере.

---

## [Engineering & Architecture] andrej-karpathy-skills
- Действие: Перенесён
- Заметки: без изменений — description и тело уже соответствуют стандарту, внешних привязок в теле нет (только одна содержательная ссылка на твит-источник происхождения материала, не на пакет/установку).

## [Engineering & Architecture] architecture-review
- Действие: Перенесён (с нормализацией)
- Заметки: собственный (не донорский) чек-лист Engineer'а. Поправлена одна устаревшая внутренняя ссылка — `HOME.md, «Вход в задачу»` → `CLAUDE.md, «Входной гейт»` (HOME.md удалён из ENGINEER в этой же сессии ранее).

## [Engineering & Architecture] codebase-design
- Действие: Перенесён (с нормализацией)
- Заметки: `DEEPENING.md` и `DESIGN-IT-TWICE.md` вынесены в `references/`, обе ссылки в SKILL.md обновлены. `agents/openai.yaml` удалён. `LICENSE.txt` сохранён.

## [Engineering & Architecture] claude-api
- Действие: Перенесён (с нормализацией)
- Заметки: официальный скилл Anthropic, уже образцовый Progressive Disclosure (`{lang}/`, `shared/`, `curl/` — скопированы полностью, 66 файлов). Единственная проблема — объём ядра 548 строк (превышение на 48). Вынесены секции «Provider Clients» (Bedrock/Foundry/Vertex) и «Workload Identity Federation» → новый `shared/provider-clients.md`; секция «Task Budgets» → новый `shared/task-budgets.md`, по образцу уже существующей в скилле конвенции `shared/*.md`. Ядро стало 490 строк. Внешних донорских привязок не найдено — все упомянутые URL (modelcontextprotocol.io и т.п. в других скиллах, здесь — сама документация Anthropic) являются содержанием скилла, не автономными нарушениями.

## [Engineering & Architecture] domain-modeling
- Действие: Перенесён (с нормализацией)
- Заметки: `ADR-FORMAT.md` и `CONTEXT-FORMAT.md` вынесены в `references/`, ссылки обновлены. `agents/openai.yaml` удалён. `LICENSE.txt` сохранён.

## [Engineering & Architecture] legacy-repository-audit
- Действие: Перенесён (с нормализацией)
- Заметки: собственный чек-лист Engineer'а. Поправлена устаревшая ссылка `registry.json/HOME.md/файлами` → `registry.json/CLAUDE.md/.claude/skills/файлами`.

## [Engineering & Architecture] mcp-builder
- Действие: Перенесён
- Заметки: без структурных изменений — уже использует `reference/` (не `references/` — минорное расхождение в имени папки с нашим каноном, не тронул: скилл внутренне консистентен, ре-именование ради формы дало бы 15+ правок ссылок без функциональной пользы). `scripts/`, `LICENSE.txt` скопированы полностью. Внешние URL (modelcontextprotocol.io, SDK-репозитории) — содержание самого скилла (гайд по разработке MCP-серверов), не донорская привязка.

## [Engineering & Architecture] repository-design
- Действие: Пропущен
- Заметки: устарело. Весь чек-лист построен вокруг файлов старого Foundation (`HOME.md`, `SOUL.md`, `ROUTING.md`, `PROFILE.md`, `MEMORY.md`, `UPDATE.md`/`update.sh`, `OPEN_QUESTIONS.md` как корневые файлы), которые сам ENGINEER удалил в этой же сессии как раздутый устаревший каркас. Перенос воспроизвёл бы именно ту структуру, от которой владелец только что осознанно отказался.

## [Engineering & Architecture] reverse-engineering
- Действие: Перенесён (с нормализацией)
- Заметки: `references/{PRINCIPLES,METHODOLOGY,REVIEW_LOOP}.md` уже в каноническом виде, скопированы как есть. Ядро (28 строк) — чистый оркестратор. Найдена фантомная ссылка `../../MISSION.md` (файл на уровень выше папки скилла, специфичный для родительского проекта-источника, не переносится) — заменена на явное пояснение пробела вместо мёртвой ссылки.

## [Engineering & Architecture] resolving-merge-conflicts
- Действие: Перенесён
- Заметки: `agents/openai.yaml` удалён. Тело (14 строк) без изменений — генерическая инструкция, внешних привязок нет.

## [Engineering & Architecture] systematic-debugging
- Действие: Перенесён (с нормализацией)
- Заметки: `root-cause-tracing.md`/`defense-in-depth.md`/`condition-based-waiting.md` → `references/`; `find-polluter.sh` → `scripts/`; `condition-based-waiting-example.ts` → `examples/` (обнаружена как реальная зависимость `condition-based-waiting.md`, не служебный артефакт — довезена). Все внутренние ссылки на эти файлы обновлены под новые пути. Убраны 2 фантомных вызова `superpowers:test-driven-development`/`superpowers:verification-before-completion` → заменены на прямые ссылки (`test-driven-development` — сосед по кластеру; `verification-before-completion` — уже установлен как реальный скилл в `.claude/skills/` ENGINEER). Не перенесены: `CREATION-LOG.md`, `test-academic.md`, `test-pressure-1/2/3.md` — собственные авторские RED/GREEN-артефакты создания скилла у донора, не материал для пользователей скилла (аналог `evidence.json`).

## [Engineering & Architecture] test-driven-development
- Действие: Перенесён (с нормализацией)
- Заметки: `writing-good-tests.md` → `references/`, ссылка обновлена. Остальное без изменений — уже соответствует стандарту.

## [Engineering & Architecture] webapp-testing
- Действие: Перенесён
- Заметки: без изменений — `examples/`, `scripts/`, `LICENSE.txt` уже в каноническом виде. Внешних привязок нет (Playwright — заявленная функциональная зависимость самого скилла, не донорский артефакт).

## [Engineering & Architecture] tool-selection
- Действие: Перенесён
- Заметки: собственный (не донорский) документ Engineer'а про выбор инструментов в этой среде. Устаревших ссылок не найдено (в отличие от architecture-review/legacy-repository-audit, HOME.md здесь не упоминается). Взят как есть.

**Итог кластера Engineering & Architecture:** 13 перенесено (8 с нормализацией, 5 без изменений), 1 пропущен (repository-design — устарело). 0 дублей в этом кластере.

---

## [Quality Gates & Foundation] final-quality-gate
- Действие: Перенесён
- Заметки: собственный (не донорский) чек-лист. Ссылается на `generalization-ladder` — сосед по этому же кластеру. Без изменений.

## [Quality Gates & Foundation] independent-validation
- Действие: Перенесён
- Заметки: собственный. Упоминает «capability Architecture Review или Code Review» — обобщённо, не фантомная ссылка на конкретный несуществующий файл. Без изменений.

## [Quality Gates & Foundation] outcome-gate
- Действие: Перенесён
- Заметки: собственный, происхождение из `AI_OS` уже честно задокументировано в самом файле (статус DRAFT). Упоминает `decision-documentation` (существует в Skill System, но не входит ни в один из 5 кластеров этого разбора) — не как обязательный вызов, а как «здесь работает другой скилл, не этот» — утверждение верно и без физического наличия соседа, не трогал.

## [Quality Gates & Foundation] verification-before-completion
- Действие: Перенесён
- Заметки: без изменений. **Дубликат по смыслу**, не по файлу: в `.claude/rules/verification-before-completion.md` ENGINEER уже есть отдельно принесённый владельцем текст на ту же тему (Iron Law/Gate Function), но это правило (`.claude/rules/`), а не скилл — разные роли в системе, не конфликтуют. Оставляю оба, решение о дальнейшей судьбе — за владельцем при разборе inbox.

## [Quality Gates & Foundation] generalization-ladder
- Действие: Перенесён
- Заметки: собственный, самодостаточный. Без изменений.

## [Quality Gates & Foundation] grilling (слит с grill-me, grill-with-docs)
- Исходные пути: `Skill System/skills/{grilling,grill-me,grill-with-docs}/SKILL.md`
- Действие: Слит
- Заметки: `grill-me` (7 строк) и `grill-with-docs` (7 строк) были не самостоятельным содержанием, а тонкими алиасами-переключателями (`disable-model-invocation: true`) — «вызови grilling» и «вызови grilling + domain-modeling». Функциональность обоих сохранена внутри `grilling`: триггер `grill-me` добавлен прямой фразой в description (`"grill me"`), вариант `grill-with-docs` — отдельным абзацем в теле («Docs-as-you-go variant: … additionally invoke `domain-modeling`»). Отдельные папки для двух алиасов не создавались — по духу задачи «сильнейшая версия», не три параллельных файла. `agents/openai.yaml` (был у grilling) не скопирован.

## [Quality Gates & Foundation] capability-creation-methodology
- Действие: Перенесён
- Заметки: собственная методология Engineer'а (не донор — прямо указано в файле «перенесено из AI_OS» с честной пометкой статуса v0.1/гипотеза). Ссылается на `architecture-review`/`repository-design` (кластер 2, уже перенесены) и «Вход в задачу устава агента» обобщённо, без имени конкретного файла — не требует правки.

## [Quality Gates & Foundation] capability-recommend
- Действие: Перенесён
- Заметки: собственный протокол, ссылается на `CATALOG.md`/`skillctl.py` — реальные файлы/инструменты Skill System, легитимное описание рабочего процесса, не донорская привязка. Без изменений.

## [Quality Gates & Foundation] claude-md-improver
- Действие: Перенесён (с нормализацией)
- Заметки: найден «осиротевший» файл `references/update-guidelines.md` (150 строк, содержательный, расширяет секцию Phase 4) — существовал на диске, но ни разу не был связан из `SKILL.md`. Добавлен один указатель в месте, где он тематически нужен («Update Guidelines (Critical)»). `quality-criteria.md`/`templates.md` уже были корректно связаны. `LICENSE.txt` сохранён.

**Итог кластера Quality Gates & Foundation:** 8 перенесено (2 с нормализацией), 1 слияние трёх скиллов в один (grilling+grill-me+grill-with-docs). 0 пропущено.

---

## [Strategy, Marketing & Growth] competitor-profiling — НЕ СЛИТ с competitors
- Действие: Перенесён (с нормализацией)
- Заметки: **отклонение от задания**: инструкция просила слить с `competitors`, но по содержанию это разные функции одного пайплайна — `competitor-profiling` собирает данные о конкуренте (скрейпинг + SEO → структурированный профиль), `competitors` пишет из готовых профилей сравнительные SEO-страницы. Сами файлы взаимно ссылаются друг на друга как на соседей («For creating comparison/alternative pages, see competitors»), не как на дубликат. Слияние испортило бы оба. Оставлены раздельными. Найден и задокументирован пробел донора: ссылки на `references/tool-reference.md`/`references/templates.md` ведут в никуда — папка `references/` отсутствует в источнике; добавлена явная пометка пробела вместо тихого переноса битой ссылки.

## [Strategy, Marketing & Growth] competitors — НЕ СЛИТ с competitor-profiling
- Действие: Перенесён (с нормализацией)
- Заметки: см. запись competitor-profiling выше — то же решение. Пробел донора: `references/templates.md`/`references/content-architecture.md` отсутствуют, пометка добавлена.

## [Strategy, Marketing & Growth] content-strategy
- Действие: Перенесён (с нормализацией)
- Заметки: тот же донор (`coreyhaines31/marketingskills`), тот же пробел — `references/content-distribution.md`/`references/headless-cms.md` отсутствуют в источнике, помечено. 441 строка, в пределах лимита.

## [Strategy, Marketing & Growth] conversion-method
- Действие: Перенесён
- Заметки: собственный (не донорский) документ, статус честно указан как «рабочая гипотеза». Без изменений.

## [Strategy, Marketing & Growth] cro
- Действие: Перенесён (с нормализацией)
- Заметки: тот же донор, тот же пробел — `references/experiments.md`/`references/form.md` отсутствуют, помечено.

## [Strategy, Marketing & Growth] idea-calibration
- Действие: Перенесён (с нормализацией)
- Заметки: собственный документ Engineer'а. Устаревшая ссылка `HOME.md` встречалась 3 раза (включая description во frontmatter) — заменена на `CLAUDE.md` везде.

## [Strategy, Marketing & Growth] lead-magnets
- Действие: Перенесён (с нормализацией)
- Заметки: тот же донор, тот же пробел — `references/benchmarks.md`/`references/format-guide.md` отсутствуют, помечено.

## [Strategy, Marketing & Growth] opportunity-discovery
- Действие: Перенесён
- Заметки: собственный, ссылается на `youtube-analysis` (сосед по кластеру) как на приёмник результата — легитимно. Без изменений.

## [Strategy, Marketing & Growth] pricing
- Действие: Перенесён
- Заметки: уже в каноническом виде — `references/` (4 файла) и `evals/` скопированы полностью, без изменений.

## [Strategy, Marketing & Growth] revops
- Действие: Перенесён
- Заметки: уже в каноническом виде — `references/` (4 файла) и `evals/` скопированы полностью, без изменений.

## [Strategy, Marketing & Growth] taste-capture — НЕ СЛИТ с taste-skill
- Действие: Перенесён
- Заметки: **отклонение от задания**: инструкция просила слить с `taste-skill`, но по содержанию это не пересекающиеся области — `taste-capture` (120 строк) — методология выявления эстетических предпочтений человека через реакцию (Evidence Board, Taste Swipe, лестница обобщения); `taste-skill` (1208 строк) — свод правил генерации anti-slop фронтенд-кода (типографика, цвет, анимации, дизайн-системы). Общее — только слово «taste» в имени. Слияние дало бы бессвязный гибрид «как узнать вкус» + «как писать CSS». Оставлены раздельными. Взят как есть, без изменений.

## [Strategy, Marketing & Growth] taste-skill — НЕ СЛИТ с taste-capture
- Действие: Перенесён (с нормализацией)
- Заметки: см. запись taste-capture выше. Отдельная проблема объёма: ядро было 1208 строк (превышение лимита почти втрое). Вынесено 5 блоков по естественным границам разделов: §4 Design Engineering Directives (191 стр.) → `references/design-engineering-directives.md`; §5.A-C канонические скелеты кода (144 стр.) → `examples/canonical-skeletons.md`; §9 AI Tells (110 стр.) → `references/ai-tells.md`; §10 Reference Vocabulary (78 стр.) → `references/reference-vocabulary.md`; блок Appendices A+B+C (224 стр., уже имел собственный заголовок-разделитель в источнике) → `references/appendices.md`. Ядро стало 482 строки. Все 5 указателей на новые файлы вставлены на месте вырезанного текста. description переформулирован под чистый триггер (был чистый пересказ «что делает»).

## [Strategy, Marketing & Growth] to-questionnaire
- Действие: Перенесён
- Заметки: `agents/openai.yaml` удалён. `LICENSE.txt` сохранён. Тело без изменений.

## [Strategy, Marketing & Growth] triage
- Действие: Перенесён
- Заметки: `agents/openai.yaml` удалён. `AGENT-BRIEF.md`/`OUT-OF-SCOPE.md`/`LICENSE.txt` сохранены — без внешних привязок.

## [Strategy, Marketing & Growth] youtube-analysis
- Действие: Перенесён
- Заметки: собственный, ссылается на `opportunity-discovery` (сосед по кластеру) как на приёмник результата — легитимно. Без изменений.

**Итог кластера Strategy, Marketing & Growth:** 15 перенесено (9 с нормализацией), 0 пропущено. **2 слияния из задания отклонены** (competitor-profiling/competitors, taste-capture/taste-skill) — по содержанию не дубли, обоснование в записях выше.

---

## [Documents, Knowledge & Formats] docx / pdf / pptx / xlsx
- Действие: Перенесены (все 4)
- Заметки: официальные скиллы Anthropic для Office-документов, уже образцовая структура (`scripts/`, `references`/`reference.md`, общие XSD-схемы для Office-форматов). Скопированы директориями целиком (173 файла на четверых), только `evidence.json` вычищен. Ядра 91–314 строк — далеко в пределах лимита. Изменений не потребовалось.

## [Documents, Knowledge & Formats] obsidian-bases
- Действие: Перенесён (с нормализацией)
- Заметки: ядро было 501 строка (превышение на 1). Секция «Complete Examples» (125 строк, самодостаточный блок примеров) вынесена в `examples/complete-examples.md`. Ядро стало 379 строк. Найден и помечен пробел донора: `references/FUNCTIONS_REFERENCE.md` упомянут дважды в тексте, но физически отсутствует в источнике. description переформулирован под чистый триггер.

## [Documents, Knowledge & Formats] obsidian-cli
- Действие: Перенесён (с нормализацией)
- Заметки: description переформулирован под чистый триггер (был «что делает» + «use when»). Тело без изменений.

## [Documents, Knowledge & Formats] obsidian-markdown
- Действие: Перенесён (с нормализацией)
- Заметки: пробел донора — `references/{CALLOUTS,EMBEDS,PROPERTIES}.md` упомянуты, но отсутствуют в источнике, помечено. description переформулирован под триггер.

## [Documents, Knowledge & Formats] json-canvas
- Действие: Перенесён (с нормализацией)
- Заметки: пробел донора — `references/EXAMPLES.md` отсутствует, помечено. description переформулирован под триггер.

## [Documents, Knowledge & Formats] tldraw-offline
- Действие: Перенесён (с нормализацией)
- Заметки: description не имел явного «Use when» вообще — добавлен. Тело (37 строк) без изменений.

## [Documents, Knowledge & Formats] doc-coauthoring
- Действие: Перенесён (с нормализацией)
- Заметки: description переформулирован под триггер (было «что делает» + дублирующиеся «Use when»/«Trigger when»). Тело без изменений.

## [Documents, Knowledge & Formats] decision-documentation
- Действие: Перенесён (с нормализацией)
- Заметки: собственный документ Engineer'а. Устаревшая ссылка на `HOME.md`/`SOUL.md`/`ROUTING.md` (файлы устава) заменена на `CLAUDE.md`/`.claude/rules/`. description переформулирован под чистый триггер.

## [Documents, Knowledge & Formats] humanizer
- Действие: Перенесён (с нормализацией)
- Заметки: происхождение уже честно задокументировано в файле (лицензия сохранена в `references/LICENSE-original`, `references/validate-package.py` — тоже). description переформулирован под чистый триггер.

## [Documents, Knowledge & Formats] hyperframes
- Действие: Перенесён (с нормализацией)
- Заметки: entry-point файл из репозитория с ~19 сопутствующими специализациями (уже честно описано прежним аудитом). Найден и помечен пробел донора: 5 ссылок на `references/*.md` (`creator-editing-recipes`, `intent-interview`, `media-treatments`, `skill-lifecycle`, `routes/remotion-to-hyperframes`) ведут в никуда — ни один из этих файлов не был перенесён вместе с entry-point. description уже был триггер-only, не тронут.

## [Documents, Knowledge & Formats] openmontage
- Действие: Пропущен
- Заметки: тот же паттерн, что `oh-my-openagent` в кластере 1 — сам донор честно пишет «это не один установимый SKILL.md — это целый продукт... не подключён ни одному агенту, паркуется до появления видео-агента». Копировать в inbox-skills как «скилл» было бы искажением статуса записи.

## [Documents, Knowledge & Formats] visual
- Действие: Перенесён (с нормализацией)
- Заметки: **не пробел, а рабочая интеграция** — полноценный CLI (VelsVisual) + внешний API (kie.ai) с раскрытыми инструкциями установки, обработкой ошибок и обязательной оценкой стоимости перед платным запуском. Не донорский артефакт для зачистки — это заявленная функциональность самого скилла. description переформулирован под чистый триггер.

## [Documents, Knowledge & Formats] defuddle
- Действие: Перенесён (с нормализацией)
- Заметки: description переформулирован под чистый триггер. Тело без изменений.

**Итог кластера Documents, Knowledge & Formats:** 15 перенесено (11 с нормализацией, 4 без изменений — docx/pdf/pptx/xlsx), 1 пропущен (openmontage — не Agent Skill по признанию самого донора).

---

# ИТОГ ВСЕГО РАЗБОРА (5 кластеров, 73 исходных скилла в Skill System)

| Кластер | Перенесено | Пропущено | Слияний выполнено | Слияний отклонено (не дубли) |
|---|---|---|---|---|
| Multi-Agent & Orchestration | 4 | 1 | 0 | — |
| Engineering & Architecture | 13 | 1 | 0 | — |
| Quality Gates & Foundation | 9 (папок; из них 1 — слитая из 3 источников) | 0 | 1 (grilling+grill-me+grill-with-docs) | — |
| Strategy, Marketing & Growth | 15 | 0 | 0 | 2 (competitor-profiling/competitors; taste-capture/taste-skill) |
| Documents, Knowledge & Formats | 15 | 1 | 0 | — |
| **Итого** | **56 папок** | **3** | **1** | **2** |

Источник (`ПРОЕКТЫ/Skill System/`) на всём протяжении разбора оставался read-only — ни одной правки, ни одного удаления. Все 56 перенесённых скиллов лежали в `workspace/inbox-skills/<Кластер>/<имя>/` внутри ENGINEER — см. запись ниже о финальной сборке и переименовании каталога.

---

# ФИНАЛЬНАЯ СБОРКА И РЕГЛАМЕНТАЦИЯ КАТАЛОГА

Дата: 2026-09-09.

1. **Переименование**: `workspace/inbox-skills/` → `workspace/skills-catalog/` (все 56 папок скиллов перенесены без изменений содержимого).
2. **Дашборд**: создан `workspace/skills-catalog/CATALOG.md` — реестр всех 56 скиллов по 5 кластерам, колонки Кластер/Навык/Статус/Роль агента/Триггер вызова. Все строки сейчас `[INBOX]`. В шапке зафиксировано правило масштабирования (5 кластеров — не потолок, Engineer открывает новые под новые домены) и протокол селекции **Challenger vs Champion** (Merge / Replace / Reject) для будущих сравнений кандидат-скиллов с уже занятыми ролями.
3. **CLAUDE.md**: добавлена секция **§7 Capability Discovery & Skills Catalog** — каталог читается On-Demand (доменная/специализированная задача, сборка роли агента), не читается на типовых инженерных задачах; прописан 5-шаговый механизм монтирования скилла из каталога в `.claude/skills/` целевого агента с обязательным обновлением статуса на `[ACTIVE]`.
4. **Обнаруженная и исправленная по ходу несостыковка**: секция была изначально пронумерована `## 8`, хотя действующий `CLAUDE.md` (отредактирован владельцем параллельно, вне этой сессии) на момент правки содержал только 6 разделов — исправлено на `## 7` сверкой по факту, не по устаревшей памяти.

**Каталог навыков экосистемы закрыт первой версией.** Дальнейшая жизнь — через `skill-auditor` (новые проходы по Skill System или внешним донорам) и протокол Challenger vs Champion выше, не прямые правки строк каталога без проверки.
