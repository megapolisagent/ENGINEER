# knowledge/ — index

Одна строка на страницу. Читается целиком при любом обращении к `knowledge/` — это и есть поиск, отдельной базы для него нет.

- [[git-bash-python-cyrillic-path-mangling]] (problems_and_fixes) — git-bash портит кириллицу в путях при передаче в `python3 -c "..."`, вызывая `FileNotFoundError`; обход — не встраивать путь-литерал, использовать переменные/аргументы или grep/cat/Read вместо python.
- [[skills-lock-hash-algorithm]] (project_knowledge) — `computedHash` в `skills-lock.json` — sha256 по путям+содержимому всех файлов папки скилла, не по одному `SKILL.md`; отдельный, другой алгоритм используется в глобальном `~/.agents/.skill-lock.json` (GitHub tree SHA).
- [[find-skills-scope]] (decisions_and_constraints) — из `find-skills` разрешён только `DISABLE_TELEMETRY=1 npx skills@1.5.23 find`; `add`/`init`/`update`/`experimental_sync`/`use` категорически запрещены (`add` симлинкает по умолчанию).
