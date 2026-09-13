#!/usr/bin/env python3
"""Validate completeness and link safety for both CSG reference catalogs."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "data/reference-map.json"
SHA = r"[0-9a-f]{40}"
TREE_OR_COMPARE = re.compile(rf"/(?:tree/{SHA}(?:/|$)|compare/{SHA}\.\.\.{SHA}(?:/|$))")
CURRENT_GUIDE_PREFIX = "https://github.com/Code-School-of-Guam-Alumni/Resources/tree/main/"
CATALOG_URLS = {
    "alumni": "CATALOG.md#alumni-lesson-",
    "lance": "LANCE.md#lance-lesson-",
}


def validate_collection(name: str, records: list[dict], expected: int, id_key: str) -> None:
    assert len(records) == expected, f"{name}: expected {expected}, got {len(records)}"
    ids = [record[id_key] for record in records]
    assert len(ids) == len(set(ids)), f"{name}: duplicate lesson IDs"

    for record in records:
        lesson_id = record[id_key]
        status = record.get("status")
        references = record.get("references", [])
        assert status, f"{name} {lesson_id}: missing status"
        assert record.get("reason"), f"{name} {lesson_id}: missing reason"
        assert references or status == "not-applicable", (
            f"{name} {lesson_id}: applicable lesson has no reference"
        )
        assert not references or status != "not-applicable", (
            f"{name} {lesson_id}: not-applicable lesson unexpectedly has references"
        )

        for reference in references:
            url = reference.get("url", "")
            assert url.startswith("https://"), f"{name} {lesson_id}: unsafe URL {url!r}"
            assert reference.get("label"), f"{name} {lesson_id}: missing reference label"
            assert reference.get("kind"), f"{name} {lesson_id}: missing reference kind"
            parsed = urlparse(url)
            assert parsed.netloc == "github.com", f"{name} {lesson_id}: unexpected host {parsed.netloc}"

            if url.startswith(CURRENT_GUIDE_PREFIX):
                assert reference["kind"] == "current guide"
                continue

            assert TREE_OR_COMPARE.search(url), (
                f"{name} {lesson_id}: recorded/reference code is not pinned to an immutable commit: {url}"
            )


def validate_catalog_anchors(records: list[dict], catalog: Path, prefix: str, id_key: str) -> None:
    body = catalog.read_text()
    for record in records:
        anchor = f'<a id="{prefix}{record[id_key]}"></a>'
        assert body.count(anchor) == 1, f"{catalog.name}: expected exactly one {anchor}"


def main() -> None:
    data = json.loads(MAP_PATH.read_text())
    validate_collection("alumni", data["alumni"], 79, "lesson_id")
    validate_collection("lance", data["lance"], 106, "id")
    validate_catalog_anchors(data["alumni"], ROOT / "CATALOG.md", "alumni-lesson-", "lesson_id")
    validate_catalog_anchors(data["lance"], ROOT / "LANCE.md", "lance-lesson-", "id")

    all_records = data["alumni"] + data["lance"]
    with_references = sum(bool(record["references"]) for record in all_records)
    not_applicable = sum(record["status"] == "not-applicable" for record in all_records)
    assert with_references == 161
    assert not_applicable == 24
    print("Validated 185 lesson mappings: 161 reference-backed and 24 explicitly not applicable.")


if __name__ == "__main__":
    main()
