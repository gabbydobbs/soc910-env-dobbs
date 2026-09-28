# Claude Code configuration

As of 2026-09-28, on the source machine:

| Item | Status |
|---|---|
| User-level `~/.claude/CLAUDE.md` | Does not exist |
| Project-level `CLAUDE.md` (in `~/Desktop/SOC 910`) | Does not exist |
| `~/.claude/settings.json` | Exists — copied here as `settings.json` (contains only `{"theme": "dark"}`, nothing sensitive) |
| User-written skills (`~/.claude/skills/`) | None. The only entry present is a marketplace-synced plugin skill, not something written by the user — not copied, since it's reinstalled via the marketplace rather than carried by hand (see `setup/install.md`) |
| Custom slash commands (`commands/`) | Directory does not exist |
| Custom hooks (`hooks/`) | Directory does not exist |

Nothing was redacted in this folder — `settings.json` contains no keys, tokens,
or passwords.

If you want a starting `CLAUDE.md`, `setup/install.md` step 6 notes where to add
one on the new machine.
