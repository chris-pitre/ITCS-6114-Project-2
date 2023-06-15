class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertex(self, id) -> None:
        self.adjacency_list[id] = []

    def add_edge(self, v1, v2, weight=1) -> None:
        edge = [v2, weight]
        self.adjacency_list.get(v1).append(edge)

    def to_string(self) -> str:
        return str(self.adjacency_list)