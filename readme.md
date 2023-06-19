# ITCS-6114 Project 2
Python-based Program to illustrate Graph Algorithms such as the Single-source Shortest Path Algorithm and Minimum Spanning Tree Algorithm.

## Getting Started

### Dependencies

* Python 3.11 or greater

### Running

1. Run main.py for both algorithms, or problem_1.py and problem_2.py for the individual algorithms.

2. Select a text file with the graph in the following format:
    ```
    [number of vertexes] [number of edges] [Directed|Undirected]
    [vertex 1] [vertex 2] [weight]
    [vertex 1] [vertex 2] [weight]
    ...
    [vertex 1] [vertex 2] [weight]
    [source vertex]
    ```
    Example:
    ```
    6 10 U
    A B 1
    A C 2
    B C 1
    B D 3
    B E 2
    C D 1
    C E 2
    D E 4
    D F 3
    E F 3
    A
    ```