import tkinter as tk
from tkinter import filedialog
from src.graph import Graph

def create_graph() -> Graph:
    """
    Creates a graph from a given file

    Returns
    -------
    graph : Graph
        Graph Data Structure
    """
    root = tk.Tk()
    root.withdraw()
    graph = Graph()

    file_path = filedialog.askopenfilename()

    with open(file_path, "r") as graph_file:
        text_matrix = [line.split() for line in graph_file]
    
    print("Creating Graph!")
    for count, line in enumerate(text_matrix):
        print(count, line)
        if count == 0:
            graph.directed = True if line[2] == "D" else False
        elif len(line) == 1:
            graph.source_node = line[0]
        else:
            if graph.directed:
                graph.add_edge(line[0], line[1], line[2])
            else: 
                graph.add_edge(line[0], line[1], line[2])
                graph.add_edge(line[1], line[0], line[2])
    
    print(f"Graph: {graph.to_string()}")
    print(f"Graph Source Node: {graph.source_node}")
    print(f"Directed: {graph.directed}")
    return graph
