---
name: knowledge-wiki
description: Use when a technical fact, decision, workflow, recurring problem/fix, or result worth remembering across sessions surfaces during work, and it belongs in this home's knowledge/ folder — writing it in (ingest mode). Also use when a task needs to look something up in knowledge/ (query mode), or to check knowledge/ for broken links and orphan pages (lint mode).
---

# Knowledge Wiki

How this home's `knowledge/` layer (level 3 of `.claude/rules/memory-rules.md`) actually gets written to and read from. Plain markdown pages, linked, no database, no background process — everything here is something the agent does inline, as part of the normal session, not a separate service.

## Scope — read this before anything else

`knowledge/` is for **work topics**: technical facts, conventions, decisions, workflows, recurring problems and their fixes, results. It is **not** for the owner's preferences, habits, or how to talk to them — that is already covered by the harness's own auto-memory (`user_*`/`feedback_*` entries). Before writing here, ask: is this about the work, or about the person? If it's about the person, it doesn't belong in `knowledge/` — say so and point at the auto-memory system instead of writing a duplicate branch here.

## Page types

```
knowledge/
  index.md              — one line per page, the only thing read in full every time
  sources/<slug>.md      — a fact/finding tied to a specific origin (a bug, a repo audit, a session discovery)
  entities/<slug>.md     — a specific tool, repo, service, or system knowledge accumulates about
  concepts/<slug>.md      — an idea, pattern, or principle that isn't tied to one origin
  syntheses/<slug>.md     — an answer to a past query worth keeping, built from multiple pages
```

Not every category needs every type populated. A page belongs to exactly one type — if unsure, `sources` is the default (a dated finding is almost always a source page).

## Every page carries a category

One of, written as `Category: <name>` right under the page's title:

| Category | What goes here |
|---|---|
| `project_knowledge` | Facts about how something works — a tool, a repo, an API, a system's real behavior |
| `decisions_and_constraints` | A choice made and why, or a hard limit discovered (resource, license, scope) |
| `workflows` | A repeatable procedure that worked, worth doing the same way again |
| `problems_and_fixes` | A bug/failure and its confirmed fix or workaround |
| `results` | An outcome worth citing later (a benchmark, an audit verdict, a measured number) |

Pick one. A page that seems to need two is usually two pages, linked.

## Ingest mode — writing something in

1. **Read `knowledge/index.md` in full.** It's small by design — this is the only "search" step, not a database query.
2. **Check for contradiction.** Does anything already in the index cover the same topic and say something different? This is a required step, not a nice-to-have — skipping it is how a wiki accumulates silent conflicts. If a contradiction is found, don't overwrite silently: note it in the page (`**Contradicts:** [[OldPage]] — <what differs>`) and say so in your summary to the user.
3. **Write or update the right page**, with its category, dated where the fact is time-bound, `[[wikilinks]]` to any related existing page.
4. **Update `index.md`** — one line: `- [[PageName]] (category) — one-line gist`.
5. **Summarize** what was added, and any contradiction found — don't let step 2's finding get lost in a "done" message.

## Query mode — looking something up

1. Read `knowledge/index.md` in full.
2. Pick up to ~10 pages that look relevant — read those, not the whole folder.
3. Answer with `[[wikilink]]` citations inline, and a `## Sources` section listing the pages drawn from.
4. If nothing in the index covers it, say so plainly — don't guess from the page title alone, and don't pad an empty answer.

## Lint mode — hygiene, on request only

Not automatic, not scheduled — run when asked to check `knowledge/` health:

1. Every `[[PageName]]` in every page — does `PageName` actually exist as a file? List the broken ones.
2. Every page under `sources/`, `entities/`, `concepts/`, `syntheses/` — is it linked from `index.md` or from another page? List the orphans.

Report both lists; fixing them is a separate, explicit step, not automatic on lint.

## What this deliberately does not do

- **No autoload at session start.** `knowledge/` is read point-by-point, under a task — never dumped into context up front. This is `.claude/rules/memory-rules.md`'s own existing rule; this skill doesn't change it, it just gives the point-by-point reads a real structure to land on.
- **No background capture.** Nothing here runs between turns or after the session ends. If a fact is worth keeping, it gets written in the same turn it surfaced, by the agent, as part of the conversation — not queued for a worker process that doesn't exist.
- **No database, no embeddings, no external API call.** `index.md` is the entire search mechanism. If `knowledge/` grows large enough that a flat index genuinely stops working, that's a real signal to revisit — not a reason to add infrastructure preemptively now.
- **No changelog, no change-history articles.** `knowledge/` holds the current state of a fact, not the story of how it got that way. When a skill, rule, or file is replaced, removed, or updated, edit or replace the relevant page in place so it reflects the new state — don't add a page narrating what was found, what changed, and why. `git log` is the history; a second, hand-written one here goes stale the moment it stops matching the real one. Ingest mode step 3 ("write or update the right page") means this literally: update in place.

## When not to use

- A fact about the owner, not the work — goes to harness auto-memory instead, not here.
- A one-off detail that won't matter past this session — most things don't need to be written down; only durable, reusable facts do (same discipline as `memory-rules.md`'s own triggers).
- Something that already belongs in `MEMORY.md` (always-true, one-line) or today's diary (`memory/<date>.md`, session narrative) — `knowledge/` is for topics, not for those two other levels' jobs.
