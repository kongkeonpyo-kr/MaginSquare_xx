"""GREEN + Golden — D-SOL-01 G1 step-A success (int[6] 1-index)."""

import pytest

from entity.solve import format_solver_golden, solve_step_a_int6
import sys
from pathlib import Path

_TESTS_DIR = Path(__file__).resolve().parents[1]
if str(_TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(_TESTS_DIR))

from _approval import assert_matches_golden

_GOLDEN_REL = "d_sol_01_g1_step_a.approved.txt"


@pytest.mark.entity
def test_d_sol_01_step_a_success(grid_g1: list[list[int]]) -> None:
    # Given: G1 부분 보드
    # When: step-A solver
    result = solve_step_a_int6(grid_g1)
    # Then: int[6] golden (1-index)
    assert len(result) == 6
    actual = format_solver_golden(result, error_code="")
    assert_matches_golden(actual, _GOLDEN_REL)
