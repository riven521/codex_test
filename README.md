# codex_test

本项目是一个 Python 实现的旅行商问题（TSP）求解 API 框架，旨在提供清晰的输入契约、可插拔的求解器接口和可靠的测试支撑。

## 项目结构
- `tsp_api/`
  - `core.py`：定义 `TSPInstance`、`TSPSolution`、`TSPAlgorithm` 协议与输入校验/距离计算。
  - `algorithms.py`：包含默认的最近邻启发式求解器，可在此扩展更多算法。
  - `__init__.py`：导出核心类/函数并提供 `solve_tsp` 入口。
- `tests/`：使用 `pytest` 测试核心契约，确保输入验证、距离计算与求解器行为不变。
- `pyproject.toml`：项目元数据与开发依赖配置。

## 快速上手
```bash
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

```python
from tsp_api import TSPInstance, solve_tsp

matrix = [
    [0.0, 1.0, 2.0],
    [1.0, 0.0, 1.0],
    [2.0, 1.0, 0.0],
]
instance = TSPInstance(distance_matrix=matrix)
solution = solve_tsp(instance)
print(solution.route, solution.total_distance)
```

```bash
pytest
```

## 扩展指南
1. 实现新的求解器时继承 `TSPAlgorithm` 协议，返回 `TSPSolution`。  
2. 所有求解器应接收 `TSPInstance`，确保复用同一套验证/距离计算逻辑。  
3. 变更后加新测试，并在 `city-vrp3` Conda 环境中跑 `python -m pytest` 验证。
