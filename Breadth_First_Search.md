# Breadth-First Search (BFS) Implementation in Python

## Overview

This project contains a Python implementation of a breadth-first search (BFS) algorithm. The BFS algorithm is used to traverse or search through graph structures. In this particular implementation, the graph is represented implicitly using nodes and actions.

### Main Components

1. **SearchNode Class**

   The `SearchNode` class is used to represent individual nodes in the search. Each node has the following attributes:
   - `state`: Represents the current position or state in the search.
   - `action`: The action taken to reach this state from the previous state.
   - `prevNode`: A reference to the previous node, allowing backtracking of the path.

   ```python
   class SearchNode:
       def __init__(self, state, action=-1, prevNode=None):
           self.state = state
           self.action = action
           self.prevNode = prevNode
   ```

2. **Path Traversal**

   The function `traversePath` is used to traverse through the path from the initial state to the current node. This is implemented recursively to backtrack and perform a specified action for each node.

   ```python
   def traversePath(node, visitFunc):
       if node == None:
           return
       traversePath(node.prevNode, visitFunc)
       visitFunc(node)
   ```

3. **Actions**

   Actions are defined as possible moves in the coordinate system:
   - `[-1, 0]`: Move left.
   - `[1, 0]`: Move right.

   The `makeAction` function takes the current state and an action ID, and calculates the new state by applying the action.

   ```python
   actions = [[-1, 0], [1, 0]]

   def makeAction(currentState, actionId):
       deltaAction = actions[actionId]
       newState = [currentState[i] + deltaAction[i] for i in range(len(currentState))]
       return newState
   ```

4. **Breadth-First Search (BFS)**

   The BFS algorithm is implemented to find a target state, where the first coordinate reaches a value of `5`. The BFS works by using two lists:
   - `openList`: Stores nodes that are yet to be expanded.
   - `closedList`: Stores nodes that have already been visited to prevent reprocessing.

   The search continues until the target state is found or all possible nodes are exhausted.

   ```python
   def isGoalFound(node):
       return node.state[0] == 5

   openList = [SearchNode([0, 0])]
   closedList = []
   goaledNode = None

   while len(openList) > 0 and goaledNode == None:
       currentNode = openList[0]
       openList.pop(0)
       if isInClosedList(currentNode):
           continue

       closedList.append(currentNode)
       if isGoalFound(currentNode):
           goaledNode = currentNode
           continue

       adjacentNodes = getNextNodes(currentNode, len(actions))
       for n in adjacentNodes:
           openList.append(n)
   ```

5. **Printing the Path**

   After finding the goal, the path is printed by traversing from the initial node to the goal node using the `traversePath` function.

### Example Output

The implementation provides an example where it creates an initial state `[0, 0]` and applies actions iteratively to reach the goal state `[5, 0]`. Each action and state change is printed along the way to visualize the path taken by the BFS algorithm.

## How to Run

- Ensure you have Python installed.
- The code is presented as a Jupyter notebook (`.ipynb` file). You can run it using Jupyter Notebook or JupyterLab.
- To execute the search, simply run all cells in the notebook.

## Requirements

- Python 3.x
- Jupyter Notebook (if running as a `.ipynb` file)

## Summary

This project demonstrates a simple breadth-first search implementation using a custom `SearchNode` class and recursive path traversal. It provides a foundation for understanding graph search algorithms and can be extended to solve more complex problems involving larger state spaces or different goal conditions.

Feel free to explore and modify the notebook to better understand the BFS process and apply it to new types of problems.
