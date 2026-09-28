# SOC 910 environment — Dobbs

A packaged snapshot of my Claude Code + VS Code development environment, for
rebuilding on another computer. Captured 2026-09-28 from a MacBook Pro
(Intel, macOS 13.7.8 Ventura).

## Contents

- `claude/` — Claude Code user config (`settings.json`) and an inventory of
  what CLAUDE.md/skills/commands/hooks do and don't exist
- `mcp/` — the one configured MCP server (`stata-mcp`, for Stata integration)
  and the command to register it on a new machine
- `project/` — `.gitignore`, two-level folder structure, and commit history
  for the SOC 910 seminar materials folder
- `setup/versions.txt` — tool versions on the source machine
- `setup/install.md` — ordered install steps, ending in a verification
  checklist, plus what can't be reproduced (accounts, licenses, paths)

## Install summary

Install Node/Python/git/gh via Homebrew → install VS Code → install Claude
Code (`npm install -g @anthropic-ai/claude-code`) → copy `claude/settings.json`
into `~/.claude/` → (optional) install Stata + the Stata MCP VS Code
extension and register it with `claude mcp add` → recreate the project
folder from `project/`. Full detail in `setup/install.md`.

## Report

### What is in your Claude Code environment?

### What tools does it use to reach your files and the internet?

### What did you have to install versus what came from your account?

### What could not be copied, and why?

### What surprised you about what was/wasn't actually configured?

### How would you verify the rebuilt environment actually works?

### What would you change about this environment going forward?
