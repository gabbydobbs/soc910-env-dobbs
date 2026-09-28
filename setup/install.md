# Install: rebuilding this environment on a clean machine

Target versions match `versions.txt`. Steps assume macOS with Homebrew
available; adjust package manager commands for another OS.

## 1. Core tools

```bash
# Xcode command line tools (git, etc.)
xcode-select --install

# Node.js (v24.20.0)
brew install node@24

# Python (3.14.7)
brew install python@3.14

# GitHub CLI
brew install gh
gh auth login
```

## 2. VS Code

Download and install VS Code 1.138.0 (or current) from
https://code.visualstudio.com/. Confirm the `code` CLI shortcut is on PATH
(Command Palette → "Shell Command: Install 'code' command in PATH").

## 3. Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version   # confirm it runs
```

Sign in when prompted (`claude` will walk through auth on first run).

## 4. Claude Code configuration

```bash
mkdir -p ~/.claude
cp claude/settings.json ~/.claude/settings.json
```

No user or project `CLAUDE.md` existed on the source machine, so there's
nothing to copy for that — see `claude/README.md` for the full inventory of
what is/isn't present. If you want to start one:
```bash
mkdir -p ~/.claude
$EDITOR ~/.claude/CLAUDE.md
```

## 5. Stata + Stata MCP (optional — only if you use Stata)

1. Install Stata itself — **licensed software, not included in this repo**
   (see "Cannot be reproduced" below).
2. Follow `mcp/register.md` in full: install the `deepecon.stata-mcp` VS Code
   extension, set `stata-vscode.stataPath`, open VS Code to start the local
   MCP server, then run:
   ```bash
   claude mcp add --transport http stata-mcp http://localhost:4000/mcp-streamable --scope user
   ```
3. Restart Claude Code / VS Code.

## 6. Project

```bash
git clone <wherever you push ~/Desktop/SOC 910 to, if anywhere>
# or, to just recreate the folder locally without a remote:
mkdir -p "~/Desktop/SOC 910"
cp project/.gitignore "~/Desktop/SOC 910/.gitignore"
```
`project/structure.txt` shows the expected two-level layout;
`project/last-20-commits.txt` shows history as of packaging (one commit —
the folder was only just put under git tracking on 2026-09-28).

## 7. Verify it worked

```bash
claude --version                 # Claude Code responds
git --version && python3 --version && node --version   # match versions.txt
gh auth status                   # shows "Logged in to github.com"
claude mcp list                  # shows stata-mcp (if step 5 was done), status "connected"
```
Then open Claude Code in the project folder and ask it to read a file — if it
can see and read `~/Desktop/SOC 910/reading articles for seminar/`, the basic
setup is working. If Stata MCP was configured, ask Claude to run a trivial
Stata command (e.g. "load the auto dataset and summarize") to confirm the
tool is live.

## Cannot be reproduced by this repo

- **Claude Code account / subscription** — sign-in is per-account, not a file.
- **GitHub account (`gabbydobbs`) and its auth token** — `gh auth login` must
  be run interactively on each new machine; the token itself is never stored
  in this repo.
- **Stata license** — Stata (`/Applications/Stata/StataSE.app`, StataSE) is
  commercial, seat-licensed software. This repo assumes you already have a
  valid license and installer; neither Stata nor its license key ships here.
- **VS Code sign-in / Settings Sync account**, if used — not captured.
- **Machine-specific paths** — e.g. `/Applications/Stata` (Stata install
  location), `/Users/gabrielledobbs/...` (home directory name/username). The
  new machine's home directory and app install paths will differ; update
  `stata-vscode.stataPath` and any absolute paths accordingly.
- **The local Stata MCP server's runtime state** — it's a process VS Code
  starts, not a saved file; it must be started fresh on the new machine.
