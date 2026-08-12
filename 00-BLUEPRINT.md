# Engineering Blueprint

What's needed for the Engineering Agent to exist — status, not a specification. Rewritten 2026-08-11 after the first version wrongly concluded "not ready yet"; see `feedback_mvp_over_completeness_gate` — a completeness gate is a false dependency when the missing pieces can only really be discovered by running the thing once.

## Можно начинать Engineer: ДА

**Ограничения первой версии (named, not hidden):**
- Repository Assembly строится на существующей архитектуре Foundation as-is — не переосмысливается заново.
- Skill Selection использует текущую библиотеку Skills as-is.
- При отсутствии нужного Skill Engineer обязан инициировать Research, а не изобретать Skill на месте.
- Workflow будет уточняться после первых реальных сборок, не раньше.
- Tool Rules пока используют прямые инструкции, до появления отдельного Skill.

## Необходимые Skills Engineer

**Статус: UNKNOWN.** Известно только, что для работы Engineer потребуется несколько переиспользуемых Skills. Их конкретные границы будут определены после первых практических сборок, не предсказаны заранее. (Предыдущая версия этого раздела перечисляла 10 кандидатных Skills как решённый список — это была гипотеза, выданная за факт; исследование этого не доказало.)

## Что уже готово

✅ Foundation — архитектура и обоснование задокументированы (`Foundation/03_ARCHITECTURE/`, `04_REPOSITORY/README.md`).
✅ Skill System — механизм `installer`, контракт `SKILL.md`, задокументированы и подтверждены рынком.
✅ Research — профессия описана (`research/AI-Engineering/`).

## Как начать завтра утром

1. Создать Engineer (минимальная специализация поверх Foundation — кто это, что делает).
2. Подключить Foundation.
3. Подключить Skill System.
4. Установить существующие Skills.
5. Дать первую задачу: собрать нового агента.
6. Во время работы фиксировать: чего не хватает, что повторяется, что становится Skill.

Это план действия, не документ, закрывающий все неизвестные. Неизвестные закрываются во время шага 5–6, не до него.
