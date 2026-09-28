#!/usr/bin/env python3
"""PostToolUse hook: warns Claude if a Read call on a PDF only covered part
of it, so a partial read never gets mistaken for the whole document.

Registered in ~/.claude/settings.json under hooks.PostToolUse (matcher: Read).
"""
import json
import re
import sys


def get_total_pages(path):
    try:
        import pymupdf  # formerly "fitz"; this import avoids its stdout
        # deprecation notice, which would otherwise corrupt this hook's
        # JSON output on stdout
        doc = pymupdf.open(path)
        return doc.page_count
    except Exception:
        pass
    # Fallback: count "/Type /Page" object occurrences in the raw PDF bytes.
    # Not exact for every PDF, but good enough as a tripwire when PyMuPDF
    # isn't available.
    try:
        with open(path, "rb") as f:
            data = f.read()
        return len(re.findall(rb"/Type\s*/Page[^s]", data))
    except Exception:
        return None


def pages_requested_count(pages_arg, total):
    if not pages_arg:
        return total  # no "pages" param = whole (short) document was read
    pages_arg = str(pages_arg).strip()
    count = 0
    for part in pages_arg.split(","):
        part = part.strip()
        if "-" in part:
            try:
                lo, hi = part.split("-")
                count += int(hi) - int(lo) + 1
            except ValueError:
                continue
        elif part.isdigit():
            count += 1
    return count


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    if payload.get("tool_name") != "Read":
        sys.exit(0)

    tool_input = payload.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "") or ""
    if not file_path.lower().endswith(".pdf"):
        sys.exit(0)

    total = get_total_pages(file_path)
    if not total:
        sys.exit(0)

    requested = pages_requested_count(tool_input.get("pages"), total)

    if requested < total:
        message = (
            f"Partial PDF read: '{file_path}' has {total} pages total, "
            f"but this call only covered about {requested}. Keep reading "
            f"the remaining pages before summarizing, answering questions "
            f"about, or drawing conclusions from this document."
        )
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "systemMessage": message,
            }
        }))

    sys.exit(0)


if __name__ == "__main__":
    main()
