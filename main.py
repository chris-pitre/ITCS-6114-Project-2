import tkinter as tk
from tkinter import filedialog
from src.graph import Graph
from src.file_to_graph import create_graph

def make_set(vertexes: list) -> list:
    """
    Makes a set from a list of given vertexes

    Parameters
    ----------
    vertexes : list
        List of vertexes
    
    Returns
    -------
    set_list : list
        List of sets of vertexes
    """
    set_list = [set(vertex) for vertex in vertexes]
    return set_list

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
test2 = graph.adjacency_list["B"]
print (test2)
test3 = graph.adjacency_list["C"]
print (test3)
vertexes = make_set(graph.adjacency_list.keys())


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to, weight):
        self.graph[frm].append([to, weight])

        if self.directed is False:
            self.graph[to].append([frm, weight])
        elif self.directed is True:
            self.graph[to] = self.graph[to]

    def find_min(self, dist, visited):
        minimum = float('inf')
        index = -1
        for v in self.graph.keys():
            if visited[v] is False and dist[v] < minimum:
                minimum = dist[v]
                index = v

        return index
    
def dikstra(graph, src):
    visited = {i: False for i in graph}
    dist = {i: float('inf') for i in graph}
    parent = {i: None for i in graph}

    dist[src] = 0

    # find shortest path for all vertices
    for i in range(len(graph) - 1):
        u = find_min(dist, visited, graph)
        visited[u] = True
        for v, w in graph[u]:

            if visited[v] is False and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
    return parent, dist  