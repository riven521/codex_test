import sys
from pathlib import Path

import pytest

# Ensure project root is importable when tests are executed from the tests folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tsp_api import NearestNeighborSolver, TSPInstance, solve_tsp

SIMPLE_MATRIX = [
    [0.0, 1.0, 2.0],
    [1.0, 0.0, 1.0],
    [2.0, 1.0, 0.0],
]


def test_instance_validation_rejects_bad_matrix() -> None:
    with pytest.raises(ValueError):
        TSPInstance(distance_matrix=[[0.0, 1.0], [1.0, 0.0, 2.0]])


def test_route_distance_computes_full_cycle() -> None:
    instance = TSPInstance(distance_matrix=SIMPLE_MATRIX)
    route = [0, 1, 2]
    assert instance.route_distance(route) == pytest.approx(4.0)


def test_nearest_neighbor_solver_returns_valid_route() -> None:
    instance = TSPInstance(distance_matrix=SIMPLE_MATRIX)
    solver = NearestNeighborSolver()
    solution = solver.solve(instance)

    assert solution.route[0] == instance.start
    assert solution.total_distance == pytest.approx(4.0)
    assert solution.metadata.get("solver") == "nearest_neighbor"


def test_solve_tsp_helper_forwards_to_algorithm() -> None:
    instance = TSPInstance(distance_matrix=SIMPLE_MATRIX)
    solution = solve_tsp(instance)
    assert solution.total_distance == pytest.approx(4.0)
