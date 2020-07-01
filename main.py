from matrix import Matrix_graph
from base import Vertex

if __name__ == "__main__":

    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    a.add_edge(b, 11)
    a.add_edge(c, 9)
    b.add_edge(a, 11)
    b.add_edge(d, 5)
    b.add_edge(e, 8)
    c.add_edge(a, 9)
    c.add_edge(e, 2)
    d.add_edge(b, 5)
    e.add_edge(c, 2)
    e.add_edge(b, 8)

    vertices = [a, b, c, d, e]
    g = Matrix_graph(vertices)
    g.print_graph()
    g.adjacency_matrix_init()
    g.print_adj_matrix()
    g.incidence_matrix_init()
    g.print_inc_matrix()
    g.bfs(b)
    g.dijkstra(a, d)