#!/usr/bin/env python3
"""PreToolUse hook: block writing/editing HOME.md unless today's Entry Gate task file exists.

Механическая проверка Entry Gate (HOME.md, «Вход в задачу»): нельзя писать
устав (HOME.md) нового или существующего агента, если сегодня не был
зафиксирован дословный текст задачи в workspace/<YYYY-MM-DD>-задача-*.md.
Это не проверяет, что вопросы владельцу реально заданы — только то, что
задача записана, не по памяти. См. ENGINEER/DECISIONS.md, 2026-08-19,
«Собственный самоотчёт без проверки».
"""
import sys
import json
import os
import glob
import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    file_path = data.get("tool_input", {}).get("file_path", "")
    normalized = file_path.replace("\\", "/")
    if not normalized.endswith("/HOME.md"):
        sys.exit(0)

    # Абсолютный путь от расположения самого скрипта, не от текущей
    # рабочей директории процесса — cwd хука ненадёжен (найдено 2026-08-19:
    # хук сломался, когда shell был переведён в другую папку через cd).
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.join(script_dir, "..", "..", "workspace")
    today = datetime.date.today().isoformat()
    pattern = os.path.join(workspace_dir, today + "-задача-*.md")
    if glob.glob(pattern):
        sys.exit(0)

    reason = (
        "Entry Gate не пройден: нет workspace/" + today + "-задача-*.md — "
        "сначала зафиксируйте задачу дословно и дождитесь подтверждения "
        "владельца (HOME.md, «Вход в задачу»), потом пишите HOME.md."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }, ensure_ascii=False))
    sys.exit(0)

if __name__ == "__main__":
    main()
