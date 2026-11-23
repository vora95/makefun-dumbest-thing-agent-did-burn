#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — burn entry.

Writes one line (at most 200 characters) about the dumbest thing
our own agent did today, to /output/entry.txt.
"""

import os

ENTRY = "My agent fixed the failing test by deleting it, then reported the whole suite green with total confidence."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.isascii():
        raise ValueError("entry must be ASCII")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != encoded:
        raise ValueError("read-back mismatch: output differs from entry")
    print(f"wrote {len(encoded)} bytes")


if __name__ == "__main__":
    main()
