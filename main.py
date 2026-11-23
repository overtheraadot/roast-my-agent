"""Roast Your Own Agent — make.fun entry (account A / overtheraa).

Writes a single original roast line to entry.txt inside
$MAKEFUN_OUTPUT_DIR (default /output). Deterministic, no network,
no model calls, no file reads outside this repo.
"""

import os

ROAST = (
    "My agent wrote five hundred lines of code just to say hello "
    "\u2014 then opened a ticket to debug the greeting."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
