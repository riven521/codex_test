from __future__ import annotations

from .algorithms import NearestNeighborSolver
from .core import TSPAlgorithm, TSPInstance, TSPSolution

__all__ = ["TSPInstance", "TSPSolution", "TSPAlgorithm", "NearestNeighborSolver", "solve_tsp"]


def solve_tsp(instance: TSPInstance, algorithm: TSPAlgorithm | None = None) -> TSPSolution:
    """统一接口：不传算法则使用默认最近邻启发式。"""

    if algorithm is None:
        algorithm = NearestNeighborSolver()
    return algorithm.solve(instance)
