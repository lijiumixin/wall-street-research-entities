#!/usr/bin/env python3
"""Minimal multilingual entity resolver for Wall Street companies & institutions."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "data"


def load_index():
    index = {}
    for kind, fname in (("company", "companies.json"), ("institution", "institutions.json")):
        rows = json.loads((ROOT / fname).read_text(encoding="utf-8"))
        for row in rows:
            entry = (kind, row)
            keys = {row["slug"], row["name_en"], *row.get("aliases", []), *row.get("labels", {}).values()}
            if row.get("ticker"):
                keys.add(row["ticker"])
            for k in keys:
                norm = str(k).strip().lower()
                if norm:
                    index.setdefault(norm, entry)
    return index


def main(args):
    if not args:
        print("Usage: python3 examples/resolve.py <name> [more ...]")
        return 1
    idx = load_index()
    for q in args:
        hit = idx.get(q.strip().lower())
        if not hit:
            print(f"{q} -> NOT FOUND")
            continue
        kind, row = hit
        url = row.get("hub_url_en", "")
        suffix = f" | {url}" if url else ""
        print(f"{q} -> {kind}/{row['slug']} ({row['name_en']}){suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
