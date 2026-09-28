# MCP servers

One MCP server is configured for Claude Code on the source machine: **stata-mcp**,
provided by the "Stata MCP" VS Code extension (`deepecon.stata-mcp`, v0.5.3), which
runs a local HTTP MCP server on port 4000 whenever VS Code has the extension active.

No token or credential is required for this server — it's a local loopback
connection (`http://localhost:4000`), so `mcp/stata-mcp.json` needed no redaction.

## Registering it on a new machine

1. Install [Stata](https://www.stata.com/) itself (licensed software — see
   `setup/install.md` "cannot be reproduced" section).
2. Install the **Stata MCP** extension in VS Code: search the Extensions
   marketplace for `deepecon.stata-mcp`, or:
   ```bash
   code --install-extension deepecon.stata-mcp
   ```
3. Set the extension's Stata path in VS Code settings (`settings.json`):
   ```json
   "stata-vscode.stataPath": "/Applications/Stata"
   ```
   (adjust to wherever Stata is installed on the new machine)
4. Open VS Code — the extension starts the local MCP server automatically
   (status bar shows "Stata"). Verify it's listening:
   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" http://localhost:4000/mcp-streamable
   ```
   A `406` response means it's up (it's rejecting a plain GET, which is expected).
5. Register the server with Claude Code:
   ```bash
   claude mcp add --transport http stata-mcp http://localhost:4000/mcp-streamable --scope user
   ```
   (Older Claude Code versions predating 2026 may need `--transport sse` and
   `http://localhost:4000/mcp` instead.)
6. Restart Claude Code / the VS Code window — MCP tool lists only refresh on
   restart, so the `stata_run_selection` tool won't appear until then.

## GitHub — not an MCP server

GitHub access does **not** go through an MCP server on the source machine. It's
handled by the `gh` CLI, authenticated separately:
```bash
gh auth login
```
See `setup/install.md` for the full ordered sequence.
