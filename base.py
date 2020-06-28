

class Vertex:

    def __init__(self, name):
        self.name = name
        self.__edges = dict()

    def __str__(self):
        return self.name

    def add_edge(self, vertex, weight=1):
        self.__edges[vertex] = weight

    def get_edges(self):
        return self.__edges


class Graph:

    def __init__(self, vertices):
        self.__vertices = vertices
        self.count_edge = []
        self.init_count_edge()

    def get_vertices(self):
        return self.__vertices

    def get_index_vertex(self, vertex):
        return self.__vertices.index(vertex)

    def init_count_edge(self):
        for vertex in self.get_vertices():
            for edge in vertex.get_edges().keys():
                if not (vertex.name, edge.name) in self.count_edge and not (edge.name, vertex.name) in self.count_edge:
                    self.count_edge.append((vertex.name, edge.name))

    def print_graph(self):
        print("Graph")
        for vertex in self.__vertices:
            print('Vertex: {} edges: '.format(vertex))
            for e, w in vertex.get_edges().items():
                print('{} weight: {} '.format(e, w))
