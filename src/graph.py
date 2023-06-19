class Graph:
    """
    A class used to represent a Graph using an Adjacency List
    
    Attributes
    ----------
    adjacency_list : dict
        A dictionary of all vertexes and edges in the list
    source_node : str
        Source node for the graph
    """
    def __init__(self) -> None:
        self.adjacency_list = {}
        self.source_node = None
        self.directed = False

    def clear(self) -> dict:
        """
        Clears out adjacency list and returns the original list

        Returns
        -------
        original_adjacency_list : dict
            A dictionary of all vertexes and edges in the list
        """
        original_adjacency_list = self.adjacency_list
        self.adjacency_list = {}
        return original_adjacency_list

    def add_vertex(self, vertex: str) -> None:
        """
        Adds a vertex to the graph
        
        Parameters
        ----------
        vertex : str
            Vertex to be added

        Raises
        ------
        VertexAlreadyExistsException
            Vertex already exists in graph
        """
        if(self.adjacency_list.get(vertex) != None):
            raise(VertexAlreadyExistsException)
        self.adjacency_list[vertex] = {}
            
    def delete_vertex(self, vertex: str) -> dict | None:
        """
        Deletes a vertex from the graph

        Parameters
        ----------
        vertex : str
            Vertex to be deleted

        Returns
        -------
        edges : dict
            A dictionary of all the vertexes and weights connected to the deleted vertex
        """
        return self.adjacency_list.pop(vertex, None)

    def add_edge(self, v1: str, v2: str, weight: int = 1) -> None:
        """
        Adds an edge from vertex 1 to vertex 2 with a weight

        Parameters
        ----------
        v1 : str
            First vertex
        v2 : str
            Second vertex
        weight : int
            Weight of edge between v1 and v2
        
        Raises
        ------
        EdgeAlreadyExistsException
            Edge already exists in graph
        """
        if(v1 not in self.adjacency_list):
            self.add_vertex(v1)
        if(v2 not in self.adjacency_list):
            self.add_vertex(v2)
        if(self.adjacency_list.get(v1).get(v2) != None):
            raise(EdgeAlreadyExistsException)
        self.adjacency_list.get(v1)[v2] = weight

    def edit_edge(self, v1: str, v2: str, weight: int) -> tuple[str, int] | None:
        """
        Edits an edge from vertex 1 to vertex 2

        Parameters
        ----------
        v1 : str
            First vertex
        v2 : str
            Second vertex
        weight : int
            Weight of edge between v1 and v2

        Returns
        -------
        original_edge : tuple
            Tuple containing edge modified and original weight
        """
        if(v2 not in self.adjacency_list[v1]):
            return None
        original_weight = self.adjacency_list.get(v1)[v2]
        self.adjacency_list.get(v1)[v2] = weight
        return (v1, v2, original_weight)

    def delete_edge(self, v1: str, v2: str) -> tuple[str, int] | None:
        """
        Deletes an edge from vertex 1 to vertex 2

        Parameters
        ----------
        v1 : str
            First vertex
        v2 : str
            Second vertex
        
        Returns
        -------
        original_edge : tuple
            Tuple containing edge modified and original weight
        """
        if(v1 not in self.adjacency_list):
            return None
        if(v2 not in self.adjacency_list[v1]):
            return None
        weight = self.adjacency_list.get(v1).pop(v2, None)
        return (v1, v2, weight)

    def to_string(self) -> str:
        return str(self.adjacency_list)

class VertexAlreadyExistsException(Exception):
    """
    Raised when add_vertex() is called with an already existing vertex
    """
    pass

class EdgeAlreadyExistsException(Exception):
    """
    Raised when add_edge() is called with an already existing edge
    """
    pass