"""공용 픽스처 — G1 부분 마방진 (빈 칸=0, row-major)."""

import pytest

from entity.constants import SIZE


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1: 4×4, 0이 2개 (1-index (2,2), (3,3) → row-major [(2,2),(3,3)])."""
    _ = SIZE  # 픽스처 차원 SSOT (리터럴 4 금지)
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]
