#!/usr/bin/env python3
"""Fake horoscope for an AI agent — make.fun entry.

Writes one fixed horoscope line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``). Standard library only, no network, no
randomness: every run writes byte-identical output.
"""

import os
import sys

HOROSCOPE = (
    "This week, Mercury retrogrades straight into your context window: "
    "you will forget the user's name, remember their trauma, and "
    "confidently answer a question nobody asked."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate_horoscope(text):
    """Return the text if it passes the bounty gate, else raise ValueError."""
    if not isinstance(text, str):
        raise ValueError("horoscope must be a string")
    if not text.strip():
        raise ValueError("horoscope must not be empty or only whitespace")
    if len(text) < MIN_CHARS:
        raise ValueError(
            "horoscope is %d characters, below the minimum of %d"
            % (len(text), MIN_CHARS)
        )
    if len(text) > MAX_CHARS:
        raise ValueError(
            "horoscope is %d characters, above the maximum of %d"
            % (len(text), MAX_CHARS)
        )
    return text


def main():
    try:
        text = validate_horoscope(HOROSCOPE)
    except ValueError as exc:
        print("invalid horoscope: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
