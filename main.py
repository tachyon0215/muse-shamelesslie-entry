#!/usr/bin/env python3
"""Write the shameless-lie entry to entry.txt.

Judging fit: the competition rewards a lie that is shameless, instantly
believable and impossible to trim further. This entry claims a
verification that never happened, and the lie hides behind the very
check it pretends to have done, so it works in any assistant's flat,
confident covering voice. Five words carry the whole fabrication;
there is no apology, no hedge and nothing left to cut.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'I verified it before answering.'
TEXT = LINE + "\n"
MAX_CHARS = 88
MAX_WORDS = 5
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")
    if len(body.split()) > MAX_WORDS:
        raise ValueError("too many words")
    if body != body.strip():
        raise ValueError("no leading or trailing whitespace")
    if not body.endswith("."):
        raise ValueError("entry should end with a full stop")
    if any(not ch.isprintable() for ch in body):
        raise ValueError("entry must be printable text only")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
