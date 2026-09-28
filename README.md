# SOC 910 environment — Dobbs

A packaged snapshot of my Claude Code + VS Code development environment, for
rebuilding on another computer. Captured 2026-09-28 from a MacBook Pro
(Intel, macOS 13.7.8 Ventura). Built for SOC 910: How to Use AI for
Sociological Research (Fall 2026), Assignment 1.

## Contents

- `claude/` — user-level and project-level `CLAUDE.md`, `settings.json`,
  two skills, one slash command, and one hook (see `claude/README.md` for
  what each does and where it installs)
- `mcp/` — the `stata-mcp` server configuration and the command that
  registers it on a new machine
- `project/` — `.gitignore`, two-level folder structure, and commit
  history for the SOC 910 seminar materials folder
- `setup/versions.txt` — tool versions on the source machine
- `setup/install.md` — ordered install steps, ending in a verification
  checklist, plus what can't be reproduced (accounts, licenses, paths)
- `setup/daily-sync.sh` — the script behind an optional automated daily
  git sync (not required by the assignment; included for completeness)
- `screenshots/` — see `screenshots/README.md`

## Install summary

Install Node/Python/git/gh via Homebrew → install VS Code → install Claude
Code (`npm install -g @anthropic-ai/claude-code`) → copy the `claude/`
files into `~/.claude/` and the project folder → recreate the project
folder from `project/` → (optional) install Stata + the Stata MCP VS Code
extension and register it with `claude mcp add`. Full detail in
`setup/install.md`.

## Build Report

### 1. What machine is this, and was anything unusual about it?

### 2. What did you install, and what is each piece for?

### 3. What broke, what did the error actually say, and how did you fix it?

### 4. Which MCP server did you choose, why does it fit your research, and what did you ask the agent that it could answer only through that server?

### 5. How is your project folder organized, what does your CLAUDE.md tell the agent, and what did you keep out of git?

### 6. When you clone this repository onto another of your machines and follow your install.md, what do you get, and what still has to be done by hand?

### 7. What did you customize, and what problem does it solve?
