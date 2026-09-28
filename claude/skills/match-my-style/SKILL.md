---
name: match-my-style
description: Applies the user's own writing and slide-design style whenever drafting prose or slides for them, instead of defaulting to generic AI style. Use whenever asked to write academic prose, a summary, a paper section, or draft/design slides for the user.
---

# Match the user's own style

Before drafting any prose or slides for the user, read
`~/.claude/style-notes.md` in full and apply its patterns rather than
defaulting to generic style. It covers:

- **Prose**: structure, sentence/paragraph craft, tone/voice by subject
  matter, citation habits, and formatting conventions, drawn from her
  actual academic papers.
- **Slides**: a specific color system (dark and light variants), font
  trio (Lato/Merriweather/DM Sans), title-slide convention, and a
  card-block content layout, drawn from her actual Google Slides decks.

`style-notes.md` is a living reference, not a fixed template — if the
user gives direct style feedback on a draft, treat that as an update to
apply going forward, and consider proposing an edit to the file itself
rather than only fixing the one draft in front of you.

If a request clearly calls for a different register (e.g., the user
explicitly asks for something informal, or for a deliberately different
look), that explicit instruction overrides these defaults — this skill
sets the baseline, not a hard constraint.
