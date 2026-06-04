"""Entity — Solver step-A 출력 int[6] (1-index, E00x emit 없음)."""

from entity.constants import BLANK_CELL, MAGIC_SUM
from entity.loc import find_blank_coords


def solve_step_a_int6(grid: list[list[int]]) -> list[int]:
    """빈 칸별 행 합 기준 채움값 → [r1,c1,n1,r2,c2,n2] (1-index)."""
    result: list[int] = []
    for row_1, col_1 in find_blank_coords(grid):
        row = grid[row_1 - 1]
        partial = sum(value for value in row if value != BLANK_CELL)
        result.extend([row_1, col_1, MAGIC_SUM - partial])
    return result


def format_solver_golden(result: list[int], error_code: str = "") -> str:
    """Golden 고정 포맷: int[6] 1-index + error_code 문자열."""
    body = ",".join(str(x) for x in result)
    return f"result_int6={body}\nerror_code={error_code}\n"
