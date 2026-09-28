# Claude Code configuration

As of 2026-09-28. Install locations on a new machine:

| File here | Goes to |
|---|---|
| `CLAUDE.md.user` | `~/.claude/CLAUDE.md` |
| `CLAUDE.md.project` | `<project folder>/CLAUDE.md` (e.g. `~/Desktop/SOC 910/CLAUDE.md`) |
| `settings.json` | `~/.claude/settings.json` |
| `style-notes.md` | `~/.claude/style-notes.md` (referenced by `CLAUDE.md.user`) |
| `skills/citation-filename/` | `~/.claude/skills/citation-filename/` |
| `skills/pdf-to-markdown/` | `~/.claude/skills/pdf-to-markdown/` |
| `skills/match-my-style/` | `~/.claude/skills/match-my-style/` |
| `commands/wrapup.md` | `~/.claude/commands/wrapup.md` |
| `hooks/check-pdf-full-read.py` | `~/.claude/hooks/check-pdf-full-read.py` (registered in `settings.json`) |

No keys, tokens, or passwords appear in any of these files — nothing here
needed redaction. `settings.json` only configures theme and the hook
below.

## What each customization does

- **`citation-filename` skill** — renames downloaded papers to
  `lastname_etal_year_short title_journal name`, automatically, whenever a
  paper is downloaded/ingested.
- **`pdf-to-markdown` skill** — picks the right PDF→Markdown tool (Docling
  for table-heavy papers, pymupdf4llm/markitdown for prose-only), matching
  this machine's pinned dependency constraints.
- **`match-my-style` skill** — applies the user's own writing/slide style
  (extracted from her real papers and Google Slides decks into
  `style-notes.md`) whenever drafting prose or slides, instead of defaulting
  to generic AI style.
- **`check-pdf-full-read.py` hook** (PostToolUse on `Read`) — flags when a
  multi-page PDF was only partially read, so a partial read never gets
  mistaken for the whole document.
- **`/wrapup` command** — logs the work session, commits, and pushes the
  coursework repo in one step.

`style-notes.md` is not one of the three required customization types
(skill/command/hook) — it's reference data those customizations and
CLAUDE.md draw on, included for completeness.
