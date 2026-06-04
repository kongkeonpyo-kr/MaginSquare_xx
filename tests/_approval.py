"""Golden Master 승인 비교 (UPDATE_GOLDEN=1 시 기준 파일 갱신)."""

import os
from pathlib import Path

_GOLDEN_ROOT = Path(__file__).resolve().parent / "golden"


def assert_matches_golden(actual: str, relative: str) -> None:
    """actual 문자열을 tests/golden/{relative} 와 비교."""
    path = _GOLDEN_ROOT / relative
    if os.environ.get("UPDATE_GOLDEN") == "1":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(actual, encoding="utf-8", newline="\n")
        return

    if not path.is_file():
        raise AssertionError(f"Golden file missing: {path}")

    expected = path.read_text(encoding="utf-8")
    if actual != expected:
        raise AssertionError(
            f"Golden mismatch: {relative}\n"
            f"--- expected ---\n{expected!r}\n"
            f"--- actual ---\n{actual!r}"
        )
