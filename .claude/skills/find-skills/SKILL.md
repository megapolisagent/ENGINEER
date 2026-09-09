---
name: find-skills
description: Helps discover existing skills from the open agent skills ecosystem via read-only search, when the user asks "how do I do X", "find a skill for X", "is there a skill that can...", or before building a new capability from scratch. Installation of anything found is NEVER done by this skill — see "Home safety rules" below.
---

# Find Skills

This skill helps discover skills from the open agent skills ecosystem through a single read-only search command. It never installs anything itself — a candidate found here still goes through this home's own manual Skill System pipeline before it's trusted.

## Home safety rules (added by ENGINEER, 2026-09-09 — read before using)

Source audit of `vercel-labs/skills` (the CLI behind this skill, ~400KB TypeScript) found: `npx skills add` **symlinks** skill files into the agent directory by default (`--copy` is required for a physical copy), and `add`/`init`/`update`/`experimental_sync` write to disk over a network path that was not fully audited. Symlinking directly violates this home's rule that every mounted skill must be a full physical copy (`CLAUDE.md` §7). Only the search path was read in full and cleared.

**Allowed — the only command that may ever be run, exactly like this:**

```bash
DISABLE_TELEMETRY=1 npx skills@1.5.23 find [query] [--owner <owner>]
```

- Version pinned to `1.5.23` (the last audited published release) — never `npx skills find` unpinned, never `@latest`.
- `DISABLE_TELEMETRY=1` always set.
- Read-only: one GET to the skills.sh search API, no filesystem writes, `add` is never triggered by this invocation path.

**Forbidden — categorically, never run these:**

- `npx skills add ...` (aliases `a`, `i`, `install`) — symlinks by default; unaudited write/network path.
- `npx skills init ...` — unaudited.
- `npx skills update ...` / `upgrade` / `check` — unaudited.
- `npx skills experimental_sync` / `experimental_install` — unaudited.
- `npx skills use ...` — unaudited.

**When `find` surfaces a candidate worth taking:** do not install it with this CLI. Fetch its `SKILL.md` by hand (raw GitHub URL or the source repo), read it in full, compare it against what already exists (Challenger vs Champion), adapt it if needed, then add it to the Skill System through the normal canonical pipeline (`CLAUDE.md` §7: validate → `set-origin`/`set-category` → physical copy, no symlink).

## When to Use This Skill

Use this skill when the user:

- Asks "how do I do X" where X might be a common task with an existing skill
- Says "find a skill for X" or "is there a skill for X"
- Asks "can you do X" where X is a specialized capability
- Expresses interest in extending agent capabilities
- Wants to search for tools, templates, or workflows
- Mentions they wish they had help with a specific domain (design, testing, deployment, etc.)

## How to Help Find Skills

### Step 1: Understand What They Need

When asked for help with something, identify:

1. The domain (e.g., React, testing, design, deployment)
2. The specific task (e.g., writing tests, creating animations, reviewing PRs)
3. Whether this is a common enough task that a skill likely exists

### Step 2: Check the Leaderboard First

Before running a CLI search, check the [skills.sh leaderboard](https://skills.sh/) to see if a well-known skill already exists for the domain. The leaderboard ranks skills by total installs, surfacing the most popular and battle-tested options.

For example, top skills for web development include:
- `vercel-labs/agent-skills` — React, Next.js, web design (100K+ installs each)
- `anthropics/skills` — Frontend design, document processing (100K+ installs)

### Step 3: Search for Skills

If the leaderboard doesn't cover the need, run the search (see "Home safety rules" above for the exact allowed invocation):

```bash
DISABLE_TELEMETRY=1 npx skills@1.5.23 find [query] [--owner <owner>]
```

For example:

- "how do I make my React app faster?" → `find react performance`
- "can you help me with PR reviews?" → `find pr review`
- "I need to create a changelog" → `find changelog`

### Step 4: Verify Quality Before Recommending

**Do not recommend a skill based solely on search results.** Always verify:

1. **Install count** — Prefer skills with 1K+ installs. Be cautious with anything under 100.
2. **Source reputation** — Official sources (`vercel-labs`, `anthropics`, `microsoft`) are more trustworthy than unknown authors.
3. **GitHub stars** — Check the source repository. A skill from a repo with <100 stars should be treated with skepticism.

### Step 5: Present Options

When relevant skills are found, present them with:

1. The skill name and what it does
2. The install count and source
3. A link to learn more at skills.sh

Example:

```
Found a skill that might help: "react-best-practices" — React and Next.js
performance optimization guidelines from Vercel Engineering. (185K installs)

Learn more: https://skills.sh/vercel-labs/agent-skills/react-best-practices
```

### Step 6: If It's Worth Taking — Hand It to the Manual Pipeline

Do not run `npx skills add`. Instead: fetch the candidate's `SKILL.md` directly, read it in full, run the Challenger vs Champion comparison against what's already in the Skill System, and — only if it earns its place — bring it in through the normal canonical import (`CLAUDE.md` §7).

## Common Skill Categories

When searching, consider these common categories:

| Category        | Example Queries                          |
| --------------- | ----------------------------------------- |
| Web Development | react, nextjs, typescript, css, tailwind |
| Testing         | testing, jest, playwright, e2e           |
| DevOps          | deploy, docker, kubernetes, ci-cd        |
| Documentation   | docs, readme, changelog, api-docs        |
| Code Quality    | review, lint, refactor, best-practices   |
| Design          | ui, ux, design-system, accessibility     |
| Productivity    | workflow, automation, git                |

## Tips for Effective Searches

1. **Use specific keywords**: "react testing" is better than just "testing"
2. **Try alternative terms**: If "deploy" doesn't work, try "deployment" or "ci-cd"
3. **Check popular sources**: Many skills come from `vercel-labs/agent-skills` or `ComposioHQ/awesome-claude-skills`

## When No Skills Are Found

If no relevant skills exist:

1. Acknowledge that no existing skill was found
2. Offer to help with the task directly using general capabilities
3. If this is something done often, a new skill can be authored — through `skill-authoring`, not `npx skills init` (unaudited, forbidden — see "Home safety rules")
