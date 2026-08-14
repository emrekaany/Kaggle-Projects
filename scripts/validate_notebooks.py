#!/usr/bin/env python3
"""Validate notebook structure and report committed execution evidence.

This script is intentionally offline and uses only the Python standard library.
It never executes notebook cells, downloads data, or contacts an API.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKEN_PATTERNS = {
    "Google API key": re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
    "GitHub token": re.compile(r"gh[pousr]_[0-9A-Za-z]{30,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
}


def main() -> int:
    notebooks = sorted(ROOT.glob("*.ipynb"))
    if not notebooks:
        print("ERROR: no root-level notebooks found", file=sys.stderr)
        return 1

    failures: list[str] = []
    totals = {"code": 0, "executed": 0, "outputs": 0}

    print("notebook\tcode_cells\texecuted_cells\toutput_objects")
    for path in notebooks:
        raw = path.read_text(encoding="utf-8")
        try:
            notebook = json.loads(raw)
        except json.JSONDecodeError as exc:
            failures.append(f"{path.name}: invalid JSON ({exc})")
            continue

        cells = notebook.get("cells")
        if notebook.get("nbformat") != 4 or not isinstance(cells, list):
            failures.append(f"{path.name}: expected nbformat 4 with a cells list")
            continue

        code_cells = [cell for cell in cells if cell.get("cell_type") == "code"]
        executed = [cell for cell in code_cells if cell.get("execution_count") is not None]
        outputs = sum(len(cell.get("outputs", [])) for cell in code_cells)
        totals["code"] += len(code_cells)
        totals["executed"] += len(executed)
        totals["outputs"] += outputs
        print(f"{path.name}\t{len(code_cells)}\t{len(executed)}\t{outputs}")

        for label, pattern in TOKEN_PATTERNS.items():
            if pattern.search(raw):
                failures.append(f"{path.name}: possible committed {label}")

    print(
        "TOTAL"
        f"\t{totals['code']}"
        f"\t{totals['executed']}"
        f"\t{totals['outputs']}"
    )

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print("Notebook integrity check passed; no notebook cells were executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
