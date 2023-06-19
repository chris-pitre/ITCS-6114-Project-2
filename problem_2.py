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

def find(set_list: list, vertex: str) -> set | None:
    """
    Finds the set a vertex is in

    Parameters
    ----------
    set_list : list
        List of sets to search through
    vertex : str
        Vertex to be found

    Returns
    -------
    vertex_set : set
        Set the vertex is contained in
    """
    vertex = set(vertex)
    for vertex_set in set_list:
        if vertex.issubset(vertex_set):
            return vertex_set
    return None

def union(set_list: list, v1: str, v2: str) -> None:
    """
    Combines two sets which contain given vertexes in a list of sets

    Parameters
    ----------
    set_list : list
        List of sets to combine sets in
    v1 : str
        First vertex
    v2 : str
        Second vertex
    """
    v1_set = find(set_list, v1)
    v2_set = find(set_list, v2)
    set_list.remove(v1_set)
    set_list.remove(v2_set)
    set_list.append(v1_set.union(v2_set))

def get_all_edges(graph: Graph) -> list:
    """
    Returns a list of all edges in a given graph

    Parameters
    ----------
    graph : Graph
        Graph to get edges from
    
    Returns
    -------
    edge_list : list
        List of edges in a graph
    """
    edge_list = [(v1, v2, weight) for v1, inner_dict in graph.adjacency_list.items() for v2, weight in inner_dict.items()]
    edge_list.sort(key=lambda item: item[2])
    return edge_list

def kruskal(graph: Graph) -> Graph:
    """
    Uses Kruskal's Algorithm to return a Minimum Spanning Tree

    Parameters
    ----------
    graph : Graph
        Graph to get MST from
    
    Returns
    -------
    mst : Graph
        Graph to represent an MST
    """
    mst = Graph()
    vertexes = make_set(graph.adjacency_list.keys())
    edges = get_all_edges(graph)
    for edge in edges:
        print(edge)
        print(vertexes)
        if len(vertexes) == 1:
            break
        if find(vertexes, edge[0]).isdisjoint(find(vertexes, edge[1])):
            mst.add_edge(edge[0], edge[1], edge[2])
            union(vertexes, edge[0], edge[1])
    return mst

if __name__ == "__main__":
    graph = create_graph()
    mst = kruskal(graph)
    print(mst.to_string())