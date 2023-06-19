from src.file_to_graph import create_graph
from problem_1 import dijkstra
from problem_2 import kruskal

graph = create_graph()

print("Problem 1: Single-source Shortest Path Algorithm")
dist, prev = dijkstra(graph, graph.source_node)
print(f"Distance Dictionary: {dist}")
print(f"Reverse Path: {prev}")

print("Problem 2: Minimum Spanning Tree Algorithm")
mst, cost = kruskal(graph)
print(f"Minimum Spanning Tree: {mst.to_string()}")
print(f"Total Cost: {cost}")