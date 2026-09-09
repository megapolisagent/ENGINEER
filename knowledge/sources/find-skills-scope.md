# find-skills: разрешён только read-only find

Category: decisions_and_constraints

Дата: 2026-09-09

## Решение

Из скилла `find-skills` (обёртка над npm-пакетом `skills`, `vercel-labs/skills`) разрешена ровно одна команда:

```bash
DISABLE_TELEMETRY=1 npx skills@1.5.23 find [query] [--owner <owner>]
```

Версия закреплена (`1.5.23`, последний прочитанный целиком релиз), телеметрия отключена явно.

**Категорически запрещены:** `add`/`init`/`update`/`experimental_sync`/`use`.

## Почему

Полный аудит исходников CLI (~2900 строк: `cli.ts`, `find.ts`, `telemetry.ts`, `skill-lock.ts`, `local-lock.ts`, `github-host.ts`) показал: `npx skills add` **симлинкает** файлы в папку агента по умолчанию (`--copy` нужен явно для физической копии) — прямой конфликт с правилом «только физическая копия, symlink запрещён категорически» (CLAUDE.md §7). `init`/`update`/`experimental_sync`/`use` вообще не аудированы — не гарантировано, что они безопасны.

`find` в некомандном режиме (с заданным query, не интерактивно) — прочитана и проверена вживую: один GET на `skills.sh/api/search`, никакой записи на диск, `add` не вызывается этим путём. Формула хеша `computedHash` в `skills-lock.json`, найденная в том же аудите исходников — см. [[skills-lock-hash-algorithm]].

## Область применения

Любая внешняя разведка (обязательна всегда — см. закон в `.claude/rules/capability-resolver.md`) через `find-skills` — только `find`, версия и телеметрия фиксированы как указано выше. Найденный кандидат ставится вручную через канонический конвейер Skill System, никогда через `npx skills add`.

## Связанные страницы

- [[skills-lock-hash-algorithm]]
