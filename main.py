"""Write one warm, funny, heartfelt family scene to /output/entry.txt.

Stdlib only. The scene must stay within the competition gate:
1 to 280 characters, one or two lines, not only whitespace.
"""

import os

ENTRY = (
    "When Dad fixed the wobbly table leg with a folded coaster, "
    "Mom declared it a family heirloom, and my little brother now "
    "guards it like a museum piece at every dinner."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 280):
        raise ValueError(
            "entry must be 1-280 characters, got %d" % len(text)
        )
    if len(text.splitlines()) > 2:
        raise ValueError("entry must be one or two lines")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the scene exactly as counted: no trailing newline, so the
    # file's character count is the scene's character count.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
