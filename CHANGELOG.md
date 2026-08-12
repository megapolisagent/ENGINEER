# Changelog

## Foundation v2.0 — 2026-08-08

Первое эволюционное обновление Foundation после v1.0.

### Добавлено

- `DECISIONS.md` — подсистема управления жизненным циклом решений.
- `OPEN_QUESTIONS.md` — реестр открытых вопросов с отслеживанием их статуса.

### Улучшено

- `HOME.md` — добавлены Entry Gate и Execution Drift.
- `ROUTING.md` — добавлен Capability Resolver.
- `instructions/memory-rules.md` — добавлена иерархия доверия источникам (Sources of Truth).
- `UPDATE.md` — добавлены Self-Modification Guard и System Health Check.

### Архитектурные изменения

- Все изменения прошли проверку ответственности перед интеграцией.
- Новые сущности добавлялись только в случаях, когда существующие документы не могли взять на себя их ответственность.
- Ни один документ Foundation v1 не был переписан с нуля — архитектура эволюционировала без разрушения существующей структуры.

---

## Foundation v1.0 — 2026-08-07

**Статус:** Stable
**Foundation Version:** 1.0

Первая версия универсального дома агента.

### Создан на основе

- **Repository Library** — 23 архитектурных блока, извлечённых из репозитория Дмитрия (content-agent).
- **World Practices Library** — отчёт по мировым практикам построения AI Agent Framework (Anthropic, OpenAI, LangGraph, CrewAI, MCP, A2A и др.).
- **Foundation Construction Library** — 79 дословных блоков, извлечённых напрямую из 14 первоисточников.
- **FOUNDATION_BLUEPRINT.md** — карта происхождения блоков по каждому файлу.
- **FOUNDATION_ARCHITECTURE.md** — обоснование архитектуры и распределения материала по источникам.
- **FOUNDATION_DECISIONS.md** — журнал решений: что клонировано, что изменено, что удалено, что добавлено, и почему — по каждому из 13 файлов.
- **FOUNDATION_OBSERVATIONS.md** — архитектурный аудит первой сборки.

Полные материалы — в `01_SOURCE_LIBRARY/`, `02_BLUEPRINT/`, `03_ARCHITECTURE/`, `05_DECISIONS/` репозитория, из которого собран этот дом.

### Состав v1.0

14 файлов/папок:

`VISION.md`, `HOME.md`, `AGENTS.md`, `SOUL.md`, `PROFILE.md`, `MEMORY.md`, `README.md`, `UPDATE.md` + `update.sh`, `ROUTING.md`, `COMMUNICATION.md`, `instructions/memory-rules.md`, `knowledge/`, `skills/` + скилл `installer`, `memory/`, `workspace/`.

`VISION.md` — единственный документ v1.0, написанный не по циклу Blueprint→Карта→Документ→Decisions: он не архитектурный, а человеческий, добавлен перед публикацией по прямому запросу — отвечает на «зачем», а не «как устроено». Источник — не три библиотеки, а сама эта сборка как пройденный опыт.

### Известные ограничения этой версии

- `SOUL.md`, `PROFILE.md`, `COMMUNICATION.md`, `workspace/` — точки расширения без собственного содержимого (обоснование — `FOUNDATION_OBSERVATIONS.md`, Наблюдение 2).
- `COMMUNICATION.md` не описывает рабочий механизм — Foundation v1 одноагентный.
- `knowledge/` содержит один рабочий файл (`lessons-learned.md`) из семи в исходной реализации — остальные признаны специфичными для одной специализации.

Полный список открытых вопросов — в `FOUNDATION_OBSERVATIONS.md`, раздел «Что требует дальнейших исследований».
