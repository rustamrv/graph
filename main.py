from base import Graph

if __name__ == "__main__":
    g = Graph()
    g.add_vertex_edge('1', '2')
    g.add_vertex_edge('1', '3')
    g.add_vertex_edge('2', '1')
    g.add_vertex_edge('2', '3')
    g.add_vertex_edge('2', '4')
    g.add_vertex_edge('3', '1')
    g.add_vertex_edge('3', '2')
    g.add_vertex_edge('3', '5')
    g.add_vertex_edge('4', '2')
    g.add_vertex_edge('4', '5')
    g.add_vertex_edge('5', '4')
    g.add_vertex_edge('5', '3')
    g.print_graph()