"""Entity 좌표 — 빈 칸 위치 (판정·E00x 없음)."""

from entity.constants import BLANK_CELL, SIZE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """빈 칸 좌표를 1-index (row, col) row-major 순으로 반환."""
    coords: list[tuple[int, int]] = []
    for row in range(SIZE):
        for col in range(SIZE):
            if grid[row][col] == BLANK_CELL:
                coords.append((row + 1, col + 1))
    return coords
