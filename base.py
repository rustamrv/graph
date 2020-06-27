
class Graph:

    def __init__(self):
        self.__graph = dict()
        self.__vertex = []
        self.f = []

    def add_vertex_edge(self, vertex, edge):
        """
        add vertex and edge for unweighted graph
        :param vertex: vertex graph
        :param edge: edge graph
        """
        if vertex > edge:
            if not [vertex, edge] in self.__vertex:
                self.__vertex.append([vertex, edge])
        else:
            if not [edge, vertex] in self.__vertex:
                self.__vertex.append([edge, vertex])
        res = self.__graph.get(vertex)
        if res is None:
            if not edge == '':
                self.__graph[vertex] = [edge]
            else:
                self.__graph[vertex] = []
        else:
            res.append(edge)

    def print_graph(self):
        print("Graph")
        for vertex, edge in self.__graph.items():
            print('Vertex: {} edges {}'.format(vertex, edge))