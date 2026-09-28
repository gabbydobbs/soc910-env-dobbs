# Install: rebuilding this environment on a clean machine

Target versions match `versions.txt`. Steps assume macOS with Homebrew
available; adjust package manager commands for another OS.

## 1. Core tools

```bash
xcode-select --install        # git, compilers
brew install node@24          # Node.js
brew install python@3.14      # Python
brew install gh               # GitHub CLI
gh auth login
gh auth setup-git             # so plain `git push` uses gh's credentials
```

## 2. VS Code

Download and install VS Code from https://code.visualstudio.com/, and
enable the `code` CLI shortcut (Command Palette → "Shell Command: Install
'code' command in PATH").

## 3. GitHub Desktop (optional GUI, used alongside the CLI)

Download from https://desktop.github.com/ (resolves to a signed,
notarized `.dmg`/`.zip` from GitHub). If unzipping on macOS, use `ditto -x -k`
rather than `unzip` — plain `unzip` can strip the code-signing metadata and
fail Gatekeeper verification even on a legitimate download.

## 4. Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```
Sign in when prompted.

## 5. Claude Code configuration

```bash
mkdir -p ~/.claude/skills ~/.claude/commands ~/.claude/hooks
cp claude/CLAUDE.md.user ~/.claude/CLAUDE.md
cp claude/settings.json ~/.claude/settings.json
cp claude/style-notes.md ~/.claude/style-notes.md
cp -R claude/skills/citation-filename ~/.claude/skills/
cp -R claude/skills/pdf-to-markdown ~/.claude/skills/
cp claude/commands/wrapup.md ~/.claude/commands/
cp claude/hooks/check-pdf-full-read.py ~/.claude/hooks/
chmod +x ~/.claude/hooks/check-pdf-full-read.py
python3 -c "import pymupdf" || pip3 install pymupdf   # the hook needs this
```
`settings.json` already registers the hook by absolute path
(`/Users/gabrielledobbs/...`) — **edit that path** to match the new
machine's home directory before it will work.

## 6. Project folder

```bash
mkdir -p ~/Desktop/"SOC 910"
cp project/.gitignore ~/Desktop/"SOC 910"/.gitignore
cp claude/CLAUDE.md.project ~/Desktop/"SOC 910"/CLAUDE.md
cd ~/Desktop/"SOC 910" && git init && git add -A && git commit -m "Reinitialize on new machine"
gh repo create soc-910-coursework --private --source=. --remote=origin --push
```
`project/structure.txt` shows the expected two-level layout;
`project/last-20-commits.txt` shows history as of packaging. The actual
paper/presentation files aren't in this packaging repo (participant/thesis
data risk and file size) — re-download or re-sync those separately.

## 7. Stata MCP server (optional — only if you use Stata)

1. Install Stata itself — **licensed software, not included here**.
2. Install the `deepecon.stata-mcp` VS Code extension (marketplace, or
   `code --install-extension deepecon.stata-mcp`).
3. Set `stata-vscode.stataPath` in VS Code settings to wherever Stata is
   installed on the new machine.
4. Open VS Code — the extension starts a local MCP server automatically
   (status bar shows "Stata"). Verify: `curl -s -o /dev/null -w "%{http_code}\n" http://localhost:4000/mcp-streamable`
   (a `406` means it's up).
5. Register it with Claude Code:
   ```bash
   claude mcp add --transport http stata-mcp http://localhost:4000/mcp-streamable --scope user
   ```
6. Restart Claude Code / VS Code — MCP tool lists only refresh on restart.

See `mcp/register.md` for full detail.

## 8. Daily automated sync (optional)

```bash
mkdir -p ~/.claude/scripts
cp setup/daily-sync.sh ~/.claude/scripts/daily-sync.sh
chmod +x ~/.claude/scripts/daily-sync.sh
# edit the TARGET_DIR path inside the script to match this machine's home dir
```
Then create `~/Library/LaunchAgents/com.<you>.soc910-daily-sync.plist`
(a `StartCalendarInterval` job at hour 0, minute 0, running that script)
and `launchctl load -w` it. This piece is a personal convenience, not
required by the assignment — skip it if you don't want unattended pushes.

## 9. Verify it worked

```bash
claude --version && git --version && python3 --version && node --version   # match versions.txt
gh auth status                    # "Logged in to github.com"
claude mcp list                   # stata-mcp shows "Connected" (if step 7 done)
```
Then open Claude Code in `~/Desktop/SOC 910` and ask it to read a file in
`reading articles for seminar/` — if it can see and read it, and the
`/wrapup` command appears when typed, the setup works.

## Cannot be reproduced by this repo

- **Claude Code account/subscription** — sign-in is per-account.
- **GitHub account (`gabbydobbs`) and its auth token** — `gh auth login`
  must be run interactively; the token itself is never stored here.
- **Google Drive/Slides/Sheets/Docs connectors** — these are claude.ai
  account-level OAuth connectors, not machine config. Reauthorize them at
  claude.ai connector settings on the new machine/account; there's no
  local file or command that recreates them.
- **Stata license** — commercial, seat-licensed software; this repo
  assumes you already have a valid license and installer.
- **GitHub Desktop sign-in**, if used.
- **Machine-specific paths** — e.g. `/Applications/Stata`, the absolute
  hook path in `settings.json`, and `/Users/gabrielledobbs/...` throughout.
  Update these to the new machine's actual paths.
- **The local Stata MCP server's runtime state** — a process VS Code
  starts, not a saved file; it must be started fresh each machine.
- **The launchd daily-sync job** (if used) — has to be recreated with the
  new machine's actual home directory path.
