# Comparative Analysis of BFS and DFS Algorithms for Solving the Chess Knight Problem

## Overview

This project aims to compare the performance of Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms in finding the minimum number of knight moves required to move from a given starting position to a target position on a chessboard and time required to find the solution. The Chess Knight Problem is a classic problem in the field of pathfinding and graph traversal.

## Table of Contents

- Introduction
- Project Components
- Implementation
- Experimental Setup
- Experimental Results
- Analysis and Discussion
- Conclusion
- Usage
- Contributing


## Introduction

### Problem Statement

The Chess Knight Problem involves finding the shortest sequence of knight moves (L-shaped moves) to reach a target square on a chessboard from a given starting square. Knights can move two squares in one direction (either horizontally or vertically) and then one square in a perpendicular direction.

### Objective

The objective of this project is to compare the performance of BFS and DFS algorithms in solving the Chess Knight Problem. We aim to evaluate the efficiency of both algorithms in terms of time complexity, space complexity, and the number of visited nodes.

## Project Components

- **Algorithm Explanation:**  
  *Breadth-First Search (BFS)* is a graph traversal algorithm that explores all the vertices of a graph or grid level by level.  
  *Depth-First Search (DFS)* is a graph traversal algorithm that explores as deeply as possible along one branch before backtracking.  
  
- **Depth Limit for DFS**

  One crucial aspect of the experimental setup is the use of a depth limit for the Depth-First Search (DFS) algorithm. The depth limit controls the maximum depth or level that DFS will explore in the search space. 
  
  The depth limit in DFS serves to strike a balance between finding a solution and controlling execution times. As mentioned in the analysis section, increasing the depth limit can impact the time taken by DFS. Therefore, choosing an appropriate depth limit is a key consideration when running the experiments.  
- **Software:**  Experiments were conducted on PyCharm Compiler using Python 3 for algorithm implementation.

## Implementation:
  In the context of solving the Chess Knight Problem, DFS and BFS can be applied as follows:  
   1.Initialization  
   2.Exploring Positions  
   3.Tracking Moves  
   4.Termination  

## Experimental Setup:
  - Chessboard Representation:  
  For the purpose of these experiments, a standard chessboard is represented as an NxN grid. Each square on the grid corresponds to a possible position for the chess knight to occupy. The coordinates of a square are represented as (x, y), where x and y are integers ranging from 1 to N, inclusive.
  - Performance Metrics:  
  When comparing the Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms for solving the Chess Knight Problem, the following parameters are taken into consideration:
   Time Complexity, Space Complexity, Number of moves.

## Experimental Results:  
  
| Problem Instance | Start Position | Target Position | Algorithm | Time (s) | Number of moves | 
|------------------|----------------|-----------------|-----------|------------|-------------|
| Instance 1       | (0, 0) | (2, 2) | BFS |      0.0005035400390625      |       4      |
|                  |                      |                      | DFS(depth-limit= 1,2,3) |      0.0     |      inf       |
|                  |                      |                      | DFS(depth-limit=4) |      0.00227      |      4       |
|                  |                      |                      | DFS(depth-limit=6) |      0.11589      |      4       |
|                  |                      |                      | DFS(depth-limit=7) |      0.67809      |      4       |
|                  |                      |                      | DFS(depth-limit=8) |      4.65626      |      4       |
| Instance 2       | (0, 0) | (3, 3) | BFS |      0.0      |      2       |
|                  |                      |                      | DFS(depth-limit=2) |      0.00101      |      2       |
|                  |                      |                      | DFS(depth-limit=4) |      0.01230      |      2       |
|                  |                      |                      | DFS(depth-limit=6) |      0.11569      |      2       |
|                  |                      |                      | DFS(depth-limit=7) |      0.64557      |      2       |
|                  |                      |                      | DFS(depth-limit=8) |      4.88771      |      2       |


## Analysis and Discussion:  

### Comparative Analysis

- **Time Complexity:** BFS tends to have a slightly higher time complexity due to its level-by-level exploration. DFS may find a solution faster in some cases but can vary widely.

- **Space Complexity:** DFS generally consumes less memory than BFS due to its stack-based approach. However, BFS guarantees a minimal number of moves.

- **Number of Visited Nodes:** BFS explores more nodes in a structured manner, while DFS explores fewer nodes but may backtrack extensively.
  
- **Effect of Depth Limit:** It's worth noting that the choice of depth limit in the DFS implementation can significantly impact the algorithm's performance. As the depth limit increases, DFS may explore deeper levels of the search space, potentially leading to a longer execution time. Therefore, fine-tuning the depth limit is crucial to balancing the trade-offs between time and space.

- **Impact of Increasing Depth Limit:** An important observation is that as we increase the depth limit in DFS, there is generally an increase in the time taken to find a solution. This is because DFS explores deeper levels of the search space before backtracking. Therefore, setting an appropriate depth limit is essential to avoid excessive execution times.  
  
## Conclusion

Our project's conclusions and recommendations can be found [here](conclusion.md).

## Usage

To use the BFS and DFS algorithms for the Chess Knight Problem, follow the instructions provided in the respective code files (`BFS.py` and `DFS.py`).

## Contributing

If you would like to contribute to this project or provide feedback, please open an issue or submit a pull request.


