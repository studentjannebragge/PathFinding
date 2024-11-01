# Search Algorithms for Pathfinding

This repository contains implementations of search algorithms used for pathfinding, such as Dijkstra, Greedy Search, and A*. The goal is to find the shortest or most cost-effective path in a grid environment.

## Features
- **Pathfinding Algorithms**: Implements Dijkstra, Greedy Search, and A* pathfinding algorithms.
- **Custom Heuristics**: Define your own branching and cost functions to adapt the algorithms to different use cases.
- **Grid Search Functionality**: Suitable for finding paths in a grid-based environment.

## Dependencies
The following Python packages are required to run the project:

- `jupyterlab==3.6.3`
- `ipykernel==6.21.1`
- `notebook==6.5.2`
- `nbconvert==7.2.9`
- `ipython==8.11.0`
- `ipywidgets==8.0.4`
- `numpy==1.24.0`
- `matplotlib==3.7.5`

You can install the required dependencies using pip:

```sh
pip install -r requirements.txt
```

## Usage
### Running the Notebook
The provided Jupyter Notebook (`FindPath_algorithm.ipynb`) demonstrates how to use the search algorithms to find paths in a grid environment. To start the notebook:

```sh
jupyter lab FindPath_algorithm.ipynb
```

### Python Script
Alternatively, you can use the Python script `search_algos.py` to integrate the search algorithms into your own projects. Below are descriptions of the key functions:

- `dijkstra(agentState, popBest, isGoalFound, branch)`: Implements Dijkstra's algorithm.
- `searhPathFindInGrid(initialState, endState, isLegalState, level, actions, popBest)`: Finds a path in a grid-based environment.
- **Branch Functions**: Functions like `popBestG`, `popBestH`, and `popBestF` are cost evaluation strategies for different pathfinding algorithms.

## Example
An example of using A* search algorithm:

```python
initial_state = (0, 0)  # Starting point
end_state = (5, 5)      # Goal point
level = [[0 for _ in range(10)] for _ in range(10)]  # 10x10 grid

# Define actions (e.g., moves in 2D grid)
actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Move up, right, down, left

def is_legal_state(state):
    x, y = state
    return 0 <= x < len(level[0]) and 0 <= y < len(level)  # Check if state is within grid boundaries

# Run A* algorithm
result, open_list = searhPathFindInGrid(initial_state, end_state, is_legal_state, level, actions, popBestF)

# Print result
if result:
    print("Path found!")
else:
    print("No path found.")
```

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact the project maintainer.

---
Feel free to open issues or submit pull requests for improvements or bug fixes.

