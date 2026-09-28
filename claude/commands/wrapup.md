---
description: End-of-session wrap-up — log what happened, commit, and push to GitHub
---

Wrap up this work session on the SOC 910 coursework folder
(`~/Desktop/SOC 910`):

1. Append a short entry to `~/Desktop/SOC 910/SESSION_LOG.md` (create it if
   it doesn't exist) with today's date and 2-5 bullet points summarizing
   what was actually done this session — new readings added, notes
   written, anything coded/converted. Be concrete, not generic.
2. Run, in `~/Desktop/SOC 910`:
   ```bash
   git add -A
   git commit -m "Session wrap-up: <one-line summary>"
   git push
   ```
   Skip the commit/push if `git status` shows nothing changed — say so
   plainly rather than creating an empty commit.
3. Never touch or include `~/Desktop/Files/Fall 2025/Thesis/` or anything
   from Apple Notes in this process, per the standing exclusions in
   `~/.claude/CLAUDE.md`.
4. Report back plainly: what got logged, whether anything was pushed, and
   the current GitHub URL (`https://github.com/gabbydobbs/soc-910-coursework`)
   so it's easy to check from another device.
