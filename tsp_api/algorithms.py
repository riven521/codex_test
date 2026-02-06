from __future__ import annotations

from .core import TSPInstance, TSPSolution


class NearestNeighborSolver:
    """最近邻启发式，依次选择未访问城市中最近的下一个节点。"""

    def __init__(self, start: int | None = None) -> None:
        self._start = start

    def solve(self, instance: TSPInstance) -> TSPSolution:
        start = self._start if self._start is not None else instance.start
        visited = [start]
        remaining = set(range(instance.num_nodes))
        remaining.remove(start)

        while remaining:
            current = visited[-1]
            next_city = self._next_city(current, remaining, instance)
            visited.append(next_city)
            remaining.remove(next_city)

        total_distance = instance.route_distance(visited)
        return TSPSolution(
            route=visited,
            total_distance=total_distance,
            metadata={"solver": "nearest_neighbor"},
        )

    def _next_city(
        self,
        current: int,
        candidates: set[int],
        instance: TSPInstance,
    ) -> int:
        return min(candidates, key=lambda city: instance.distance_matrix[current][city])
