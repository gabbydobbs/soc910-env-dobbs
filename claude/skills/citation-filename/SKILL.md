---
name: citation-filename
description: Renames downloaded academic paper files into the user's standard citation-based filename format. Use whenever the user downloads, saves, or asks to rename/organize an academic paper/PDF, or says to "convert" or "ingest" a paper.
---

# Citation filename convention

Rename downloaded paper files to:

```
lastname_etal_year_short title_journal name
```

Underscores separate the four fields; spaces are allowed within a field.

Example: `Niranjan-Azadi_etal_2026_Well-being Assessment Instruments_J Gen Intern Med.pdf`

- **lastname** — first author's surname only (keep hyphens, e.g. `Niranjan-Azadi`)
- **etal** — literal `etal` when there is more than one author; omit it for a
  single-author paper
- **year** — publication year
- **short title** — a shortened form of the title, enough to identify it at
  a glance
- **journal name** — abbreviated journal name as it appears in the citation
  (e.g. `J Gen Intern Med`)

## When to also convert to Markdown

If the user says "ingest" (not just rename), also produce a Markdown
version via the `pdf-to-markdown` skill and drop it in
`~/Desktop/SOC 910/reading articles for seminar/`.

## After renaming

Consider saving a short `reference` memory noting the paper and its topic,
so it's easy to recall later without re-reading it.
