Here's a `README.md` that explains the provided code, covering each class and method with usage examples and explanations. This document should serve as a comprehensive guide for users looking to understand and run the code.

```markdown
# Graph Visualization and Pathfinding with Dijkstra's Algorithm

This project demonstrates how to represent, visualize, and find paths in a directed graph using Dijkstra's algorithm and the `NetworkX` library for Python. The primary classes are `Dijkstra` for calculating the shortest paths and `GraphHelper` for visualizing the graph.

## Prerequisites

Before running the code, make sure you have the required libraries installed:

```bash
pip install numpy networkx matplotlib
```

## Classes and Functions

### Dijkstra Class

The `Dijkstra` class is responsible for calculating the shortest path between nodes in a weighted directed graph using Dijkstra's algorithm.

#### Constructor

```python
Dijkstra(input)
```

- **Parameters**:
  - `input`: A 2D list (matrix) representing the adjacency matrix of the graph, where `input[i][j]` holds the weight of the edge from node `i` to node `j`. A weight of `0` means no direct edge exists between the nodes.

#### Methods

1. **`calculate()`**  
   Calculates the shortest paths from each node to all other nodes using Dijkstra's algorithm.

   - **Returns**: A list where each element is a list representing the minimum distances from that node to all others.

2. **`calculateFromOrigin(origin)`**  
   Calculates the shortest paths from a specific origin node to all other nodes.

   - **Parameters**:
     - `origin`: The starting node for the calculation.
   - **Returns**: A list of minimum distances from the origin node to all other nodes.

3. **`getPath()`**  
   Returns the computed path matrix after running the `calculate` method.

4. **`getBestPath(frm, to)`**  
   Retrieves the shortest path from node `frm` to node `to` based on the previous calculations.

   - **Parameters**:
     - `frm`: Starting node.
     - `to`: Destination node.
   - **Returns**: A list of nodes representing the shortest path from `frm` to `to`.

#### Example Usage

```python
# Create an adjacency matrix for the graph
input = [
    [0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]
]

# Initialize the Dijkstra object
dj = Dijkstra(input)

# Calculate shortest paths from all nodes
result = dj.calculate()

# Get the best path between nodes 2 and 4
best_path = dj.getBestPath(2, 4)
print("Shortest path from 2 to 4:", best_path)
```

### GraphHelper Class

The `GraphHelper` class provides a static method to visualize a directed graph with optional highlighting of a specific path.

#### Methods

1. **`printGraph(input, featured=None)`**  
   Visualizes the graph based on an adjacency matrix. It optionally highlights a specific path.

   - **Parameters**:
     - `input`: A 2D list (matrix) representing the adjacency matrix of the graph, with weights representing edge distances.
     - `featured`: An optional list of nodes representing a path to highlight in the visualization.

#### Example Usage

```python
# Visualize the entire graph
GraphHelper.printGraph(input)

# Visualize the graph with the shortest path from node 2 to node 4 highlighted
GraphHelper.printGraph(input, dj.getBestPath(2, 4))
```

### Code Explanation

- **Creating the Graph**: The adjacency matrix `input` defines edges and weights between nodes. A value of `0` implies no edge.
- **Finding Shortest Paths**: The `Dijkstra` class is used to find the shortest paths. The method `calculate` computes paths for all nodes, and `getBestPath` extracts a path between two nodes.
- **Visualizing the Graph**: `GraphHelper.printGraph` uses `NetworkX` to visualize the graph, with an optional `featured` path highlighted in red.

### Example Code

To see everything in action, run the following code:

```python
# Define the adjacency matrix
input = [
    [0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]
]

# Initialize and calculate paths
dj = Dijkstra(input)
result = dj.calculate()

# Get the best path from node 2 to node 4 and visualize
best_path = dj.getBestPath(2, 4)
print("Shortest path from 2 to 4:", best_path)
GraphHelper.printGraph(input, best_path)
```

## Notes

[Source](https://github.com/thiagolcks/dijkstra)
