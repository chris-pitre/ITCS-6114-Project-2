import tkinter as tk
from tkinter import filedialog
from src.graph import Graph
from src.file_to_graph import create_graph

def shortest(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    shortest_paths = {}

    while graph:
        # Find the node with the smallest distance from the start node
        min_node = None
        for node in graph:
            if min_node is None:
                min_node = node
            elif distances[node] < distances[min_node]:
                min_node = node

        # Calculate the distance to the neighbors of the minimum node
        for neighbor, weight in graph[min_node].items():
            if weight + distances[min_node] < distances[neighbor]:
                distances[neighbor] = weight + distances[min_node]
                shortest_paths[neighbor] = min_node

        # Remove the minimum node from the graph
        graph.pop(min_node)

    return distances, shortest_paths

graph = create_graph()
test = graph.adjacency_list["A"]
print (test)
#All the stuff below this is currently the manual input stuff, I'm gonna try to figure out how to just use the read info shit
# Read the graph from input
n, m, _ = input().split()
n, m = int(n), int(m)
graph = {chr(ord('A') + i): {} for i in range(n)}

for _ in range(m):
    u, v, w = input().split()
    graph[u][v] = int(w)

start_node = input().strip()

# Print the graph
print("Graph:")
for node, neighbors in graph.items():
    print(node + ":")
    for neighbor, weight in neighbors.items():
        print("  ->", neighbor + ":", weight)

# Apply algorithm
distances, shortest_paths = shortest(graph, start_node)
print(distances)
print(shortest_paths)

# Print the results
print("\nShortest distances from node", start_node + ":")
for node, distance in distances.items():
    print("Node:", node, "- Distance:", distance)

print("\nShortest paths from node", start_node + ":")
for node, path in shortest_paths.items():
    print("Node:", node, "- Path:", [node] + list(shortest_paths[node])[::-1])    