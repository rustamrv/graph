from base import Graph


class Matrix_graph(Graph):

    def __init__(self, vertices):
        super().__init__(vertices)
        self.__adjacency_matrix = []
        self.__incidence_matrix = []

    def adjacency_matrix_init(self):
        """
            Init adjacency matrix (смежная матрица)
        """
        size = len(self.get_vertices())
        self.__adjacency_matrix = [0] * size
        for i in range(0, size):
            self.__adjacency_matrix[i] = [0] * size

        for vertex in self.get_vertices():
            ind = self.get_index_vertex(vertex)
            for edge, weight in vertex.get_edges().items():
                jnd = self.get_index_vertex(edge)
                self.__adjacency_matrix[ind][jnd] = weight

    def incidence_matrix_init(self):
        """
            Init incidence matrix (матрица инцидентности)
        """
        size = len(self.get_vertices())
        self.__incidence_matrix = [0] * size
        for i in range(0, size):
            self.__incidence_matrix[i] = [0] * len(self.count_edge)

        for vertex in self.get_vertices():
            ind = self.get_index_vertex(vertex)
            for edge, weight in vertex.get_edges().items():
                try:
                    jnd = self.count_edge.index((vertex.name, edge.name))
                except ValueError:
                    jnd = self.count_edge.index((edge.name, vertex.name))
                self.__incidence_matrix[ind][jnd] = weight

    def print_adj_matrix(self):
        print('Matrix adj init: ')
        for i in self.__adjacency_matrix:
            print(*i)

    def print_inc_matrix(self):
        print('Matrix inc init: ')
        for i in self.__incidence_matrix:
            print(*i)
