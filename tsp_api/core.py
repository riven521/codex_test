from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Protocol


@dataclass
class TSPInstance:
    """旅行商问题的输入定义。

    包含对称或非对称的距离矩阵、起始节点索引与可选元数据。
    """

    distance_matrix: list[list[float]]
    start: int = 0
    metadata: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        node_count = len(self.distance_matrix)
        if node_count == 0:
            raise ValueError("距离矩阵不能为空")

        for row in self.distance_matrix:
            if len(row) != node_count:
                raise ValueError("距离矩阵必须为方阵")

        if not (0 <= self.start < node_count):
            raise ValueError("起点索引必须在 0 与节点数-1 之间")

    @property
    def num_nodes(self) -> int:
        return len(self.distance_matrix)

    def route_distance(self, route: Iterable[int]) -> float:
        """计算按 route 顺序的完整回路距离。"""

        route_list = list(route)
        if not route_list:
            return 0.0

        total = 0.0
        for current, nxt in zip(route_list, route_list[1:]):
            total += self.distance_matrix[current][nxt]

        total += self.distance_matrix[route_list[-1]][route_list[0]]
        return total


@dataclass
class TSPSolution:
    route: list[int]
    total_distance: float
    metadata: dict[str, str] = field(default_factory=dict)


class TSPAlgorithm(Protocol):
    def solve(self, instance: TSPInstance) -> TSPSolution:
        ...
