---
name: yagni-ladder
description: Use before writing new code for a feature or fix, and when asked to review, audit, or clean up an existing diff/component/file for over-engineering. Two modes — write (a 7-rung ladder checked before adding code) and review (produce a scoped, cited delete-list, not general critique).
---

# YAGNI Ladder

A discipline for two moments: before you write new code, and when you're asked to look at code someone (possibly you) already wrote and find what doesn't need to be there.

## Write mode — the ladder

Read the task, read the code the change touches, understand the actual flow first. The ladder runs *after* that — it is lazy about the solution, never about reading. Then, in order, stop at the first rung that holds:

1. **Does this need to exist at all?** No caller, no stated requirement → don't build it. (YAGNI)
2. **Already in this codebase?** → reuse it, don't rewrite it.
3. **Does the language's standard library do it?** → use that.
4. **Is there a native platform feature?** → use that.
5. **Does an already-installed dependency do it?** → use that. (Reaching for a *new* dependency is not this rung — that's scope, go back to rung 1 and ask if the need is real.)
6. **Does it fit in one line?** → one line.
7. **Only then** — the minimum code that actually works, scoped to the real requirement, not the anticipated one.

A hint about future scale ("we'll have 200 of these next sprint", "make it flexible for later") is not a requirement today. Solve today's shape; rung 1 applies to imagined future callers exactly like it applies to imagined present ones.

## Protected zones — never traded for brevity

These are never cut, skipped, or simplified away to make the diff smaller, no matter which rung the rest of the code lands on:

- **Security** (auth checks, input sanitization, secret handling)
- **Accessibility** (label/input association, keyboard operability, ARIA where the interaction needs it)
- **Data-loss handling** (confirmations, atomic writes, anything that can silently drop a user's work)
- **Trust-boundary validation** (anything crossing from user input, network, or another process into your code)

"Less code" is never the justification for missing one of these. A minimal solution that skips a protected zone isn't minimal — it's incomplete.

## Review mode — produce a delete-list, not a critique

When asked to review a diff, a component, or a file for over-engineering:

1. **For each construct that looks unused** (a prop, a branch, a config option, a whole abstraction) — **grep the repo for real callers before recommending removal.** "If it's not used elsewhere" is not a finding, it's a question you didn't answer yet. Answer it, then commit to the verdict.
2. **Output only the delete-list.** Bugs, accessibility gaps, and style feedback are real, but they are a different list — don't let them dilute or hedge the over-engineering findings. If something belongs in both, say so explicitly rather than burying the delete-list in mixed prose.
3. **Every item cites what makes it removable**: which rung it fails (no real caller = rung 1; hand-rolled where stdlib/a dependency already does it = rung 3/5), or that it's speculative generality for a future that isn't real yet.
4. **Format:**
   ```
   Remove: <file>:<line or prop/block> — <what it is>
   Because: <rung failed, in one clause> — <confirmed no other caller, or: still called at <file:line>, keep>
   ```
5. If a construct genuinely has a caller elsewhere, or the ambiguity can't be resolved by grepping (e.g. it's a public API of a published package), say so plainly and leave it off the delete-list — don't guess in either direction.

## False justifications — counter them, don't accept them

| The model says | The ladder says back |
|---|---|
| "More flexible for future use cases" | No caller today = rung 1. Flexibility for an imagined caller is speculative generality, not a requirement. |
| "More configurable" | Unused config is dead code with extra steps — harder to read, not more capable, until something actually calls it. |
| "The library will save time later" | Rung 5 covers dependencies already installed. A *new* dependency for a need that isn't confirmed yet is scope creep, not reuse — go back to rung 1. |
| "It's more robust this way" | Robustness for the actual failure modes of this code is rung 7. Robustness for failure modes that can't happen here is padding. |
| "Shorter code isn't always better" | Correct — that's exactly why the protected zones exist and this ladder never touches them. Minimal means scoped to the real requirement, not fewer characters. |
| "I can't tell if it's used elsewhere, so I'll suggest removing it as an option" | Not a stopping point — grep for it. A hedge is not a verdict. |

## When not to use

- Protected-zone work itself (writing the validation, the a11y wiring, the security check) — the ladder governs everything *around* that work, not the work itself.
- Genuinely exploratory/spike code explicitly marked as throwaway, where the point is to learn something before any real version gets built.
- A requirement that's already been decided and scoped by the owner/spec as needing the fuller version (e.g. the abstraction is requested because a second real caller is landing this week, not hypothetically) — the ladder resolves *unstated* scope, not overrides a stated one.
