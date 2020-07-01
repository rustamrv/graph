from collections import deque


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

    def bfs(self, start_node):
        visited = dict()
        for vertex in self.__vertices:
            visited[self.get_index_vertex(vertex)] = False

        queue = deque()
        queue.append(self.get_index_vertex(start_node))
        visited[self.get_index_vertex(start_node)] = True
        array = []
        while queue:
            node = queue.popleft()
            array.append(self.__vertices[node].name)
            for e, w in self.__vertices[node].get_edges().items():
                if not visited[self.get_index_vertex(e)]:
                    queue.append(self.get_index_vertex(e))
                    visited[self.get_index_vertex(e)] = True
        print('Breadth-first search for {} : {}'.format(start_node, array))

    def dijkstra(self, start_vertex, end_vertex):
        visited = dict()
        dist = dict()
        for i in self.get_vertices():
            visited[i.name] = False
            dist[i.name] = float('inf')

        dist[start_vertex.name] = 0
        visited[start_vertex.name] = True

        queue = deque()
        queue.append(start_vertex)
        while queue:
            vertex = queue.popleft()
            for edge in vertex.get_edges().keys():
                if not visited[edge.name] and not len(edge.get_edges().keys()) == 0\
                        and vertex.get_edges()[edge] + dist[vertex.name] < dist[edge.name]:
                    dist[edge.name] = vertex.get_edges()[edge] + dist[vertex.name]
                    visited[edge.name] = True
                    queue.append(edge)

        print('Shortest paths from {} to {} : {}'.format(start_vertex.name, end_vertex.name, dist[end_vertex.name]))
