# knowledge/ — index

Одна строка на страницу. Читается целиком при любом обращении к `knowledge/` — это и есть поиск, отдельной базы для него нет.

- [[git-bash-python-cyrillic-path-mangling]] (problems_and_fixes) — git-bash портит кириллицу в путях при передаче в `python3 -c "..."`, вызывая `FileNotFoundError`; обход — не встраивать путь-литерал, использовать переменные/аргументы или grep/cat/Read вместо python.
- [[skills-lock-hash-algorithm]] (project_knowledge) — `computedHash` в `skills-lock.json` — sha256 по путям+содержимому всех файлов папки скилла, не по одному `SKILL.md`; отдельный, другой алгоритм используется в глобальном `~/.agents/.skill-lock.json` (GitHub tree SHA).
- [[find-skills-scope]] (decisions_and_constraints) — из `find-skills` разрешён только `DISABLE_TELEMETRY=1 npx skills@1.5.23 find`; `add`/`init`/`update`/`experimental_sync`/`use` категорически запрещены (`add` симлинкает по умолчанию).
- [[domain_knowledge_retrieval]] (project_knowledge) — паттерн предметного каталога через knowledge-wiki (карточки сущностей + ручные wikilinks) для домен-агентов, отвечающих клиентам фактами; отличие от GraphRAG-инструментов (LightRAG) и порог, когда к ним стоит вернуться. Наполнение — не в ENGINEER, а у профильного агента-владельца.
- [[graphify-verdict]] (decisions_and_constraints) — не устанавливать сейчас: тихая самоустановка пакета, skill.md 713 строк (выше потолка 500), автовписывание в CLAUDE.md, git-хук, заявлен на 16 ассистентов сразу. Не конкурент knowledge-wiki — другая ниша (разовая индексация чужого корпуса, не растущая память).
- [[magic-mcp-21st-dev]] (decisions_and_constraints) — не устанавливать сейчас: строго фронтенд-UI (React/Tailwind/shadcn), платный облачный сервис без self-hosted режима, нет адресата среди текущих собранных агентов. Пересмотреть, если появится фронтенд-агент.
- [[yt-dlp-verdict]] (decisions_and_constraints) — не устанавливать сейчас: зрелый и ответственно поддерживаемый (189k звёзд, 13 официальных security advisory, все патчены), но реальный RCE-паттерн через `--exec`/`--netrc-cmd`; нет текущей задачи — всплыл только как video-экстра graphify, уже отклонённая.
