from src.graph import Graph
from src.file_to_graph import create_graph
import math

def dijkstra(graph: Graph, source: str) -> tuple:
    """
    Performs Dijkstra's Algorithm on a given graph and start vertex

    Parameters
    ----------
    graph : Graph
        Graph to be used
    source : str
        Starting Vertex

    Returns
    -------
    dist : dict
        Dictionary of distances from start node
    prev : dict
        Previous node 
    """
    dist = {}
    prev = {}
    unvisited_vertexes = []
    for vertex in graph.adjacency_list.keys():
        dist[vertex] = math.inf
        prev[vertex] = None
        unvisited_vertexes.append(vertex)
    dist[source] = 0 

    while unvisited_vertexes:
        unvisited_dist = [vertex for vertex in dist if vertex in unvisited_vertexes]
        min_dist = min(unvisited_dist, key=dist.get)
        print(min_dist)
        vertex_u = min_dist
        unvisited_vertexes.remove(min_dist)
        print(graph.adjacency_list[vertex_u].items())

        for neighbor, weight in graph.adjacency_list[vertex_u].items():
            alt = dist[vertex_u] + int(weight)
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = vertex_u

    return dist, prev

if __name__ == "__main__":
    graph = create_graph()
    dist, prev = dijkstra(graph, graph.source_node)
    print(dist)
    print(prev)