import unittest
from src.graph import Graph, VertexAlreadyExistsException, EdgeAlreadyExistsException

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
    
    def test_constructor(self):
        self.assertDictEqual(self.graph.adjacency_list, {}, "Dictionary Improperly Created!")

    def test_add_vertex(self):
        self.graph.add_vertex("A")
        test_dict = {"A": {}}
        self.assertDictEqual(self.graph.adjacency_list, test_dict, "Vertex Improperly Created!")
    
    def test_add_vertex_existing(self):
        self.graph.add_vertex("A")
        self.assertRaises(VertexAlreadyExistsException, self.graph.add_vertex, "A")

    def test_delete_vertex(self):
        self.graph.add_vertex("A")
        removed_vertex = self.graph.delete_vertex("A")
        self.assertDictEqual(self.graph.adjacency_list, {}, "Graph Not Empty!")
        self.assertDictEqual(removed_vertex, {}, "Return Value is Incorrect!")

    def test_delete_vertex_empty(self):
        removed_vertex = self.graph.delete_vertex("A")
        self.assertDictEqual(self.graph.adjacency_list, {}, "Graph Not Empty!")
        self.assertEqual(removed_vertex, None, "Return Value is Incorrect!")
    
    def test_delete_vertex_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        removed_vertex = self.graph.delete_vertex("A")
        self.assertDictEqual(self.graph.adjacency_list, {"B": {}}, "Graph Incorrectly Edited!")
        self.assertDictEqual(removed_vertex, {"B": 1}, "Return Value is Incorrect!")

    def test_add_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        test_dict = {"A": {"B": 1}, "B": {}}
        self.assertDictEqual(self.graph.adjacency_list, test_dict, "Edge Not Created Properly!")

    def test_add_edge_existing(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        self.assertRaises(EdgeAlreadyExistsException, self.graph.add_edge, "A", "B")

    def test_edit_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        original_edge = self.graph.edit_edge("A", "B", 2)
        test_dict = {"A": {"B": 2}, "B": {}}
        self.assertTupleEqual(original_edge, ("A", "B", 1))
        self.assertDictEqual(self.graph.adjacency_list, test_dict, "Edge Not Edited Properly!")
    
    def test_edit_edge_empty(self):
        self.graph.add_vertex("A")
        original_edge = self.graph.edit_edge("A", "B", 2)
        self.assertEqual(original_edge, None, "Return Value is Incorrect!")

    def test_delete_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        removed_edge = self.graph.delete_edge("A", "B")
        test_dict = {"A": {}, "B": {}}
        self.assertDictEqual(self.graph.adjacency_list, test_dict, "Edge Not Deleted Properly!")
        self.assertTupleEqual(removed_edge, ("A", "B", 1), "Return Value is Incorrect")
    
    def test_delete_edge_empty_vertex(self):
        removed_edge = self.graph.delete_edge("A", "B")
        self.assertEqual(removed_edge, None, "Return Value is Incorrect!")    
    
    def test_delete_edge_empty_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        removed_edge = self.graph.delete_edge("A", "B")
        self.assertEqual(removed_edge, None, "Return Value is Incorrect!")    

    def test_to_string(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")
        graph_string = self.graph.to_string()
        test_string = "{'A': {'B': 1}, 'B': {}}"
        self.assertEqual(graph_string, test_string, "String Do Not Match!")

    def tearDown(self) -> None:
        self.graph.clear()

if __name__ == "__main__":
    unittest.main()
