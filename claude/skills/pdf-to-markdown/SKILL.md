---
name: pdf-to-markdown
description: Converts a PDF (especially table-heavy academic papers) to Markdown using the user's pinned local toolchain. Use whenever the user asks to convert a PDF to Markdown, or says to "ingest" a paper.
---

# PDF to Markdown conversion

This machine is an Intel Mac, macOS 13.7.8 — that constrains which PDF
tools actually work, so use the right one for the job rather than whatever
is fastest to reach for.

## Table-heavy papers (default for academic papers)

Use the Docling setup pinned in `~/pdf-tools/`:

```bash
source ~/pdf-tools/.venv/bin/activate && python ~/pdf-tools/pdf2md.py paper.pdf
```

This is the only tool on this machine that produces correctly-aligned
Markdown tables. It's slow (~2-3 min per PDF, CPU-only) because it loads
layout + TableFormer models each run — that's expected, not a hang.

Do not try to "upgrade" the pinned versions in that venv — `docling-parse`,
`torch`, `numpy`, `scipy`, and `opencv-python` are all pinned to specific
versions because this Intel Mac's Clang 14 toolchain can't build newer
wheels for several of Docling's dependencies. If this venv ever breaks,
check `~/pdf-tools/README.md` before changing any version pin.

## Prose-only papers (no meaningful tables)

Base `pymupdf4llm` or `markitdown` on system Python is fine and much
faster than Docling — use one of these instead for plain prose.

## Don't use

`pandoc` cannot read PDF input at all — don't suggest it for this.

## Where converted files go

If this is for the SOC 910 reading list, save the `.md` output alongside
the source PDF in `~/Desktop/SOC 910/reading articles for seminar/` (see
the `citation-filename` skill for naming both files consistently).
