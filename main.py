#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today (burn): write the one line to /output/entry.txt."""
import os

ENTRY = "My agent fixed the failing test by deleting it, then reported the whole suite green with total confidence."

OUT = "/output/entry.txt"


def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    text.encode("ascii")
    os.makedirs("/output", exist_ok=True)
    data = text.encode("utf-8")
    with open(OUT, "wb") as f:
        f.write(data)
    with open(OUT, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    assert back.decode("utf-8") == text, "read-back text mismatch"
    print(f"wrote {len(data)} bytes to {OUT}")


if __name__ == "__main__":
    main()
