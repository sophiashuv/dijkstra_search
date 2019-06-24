class Graph:
    """
    Class for Graph representation.
    """
    def __init__(self, filename, starting_vrt, final_vrt):
        """
        Initialization of Graph.
        :param filename: str
        :param starting_vrt: str
        :param final_vrt: str
        """
        self.filename = filename
        self.starting = starting_vrt
        self.final = final_vrt
        self.vertices = []
        self.weights = dict()
        self.read_matrix()
        
    def read_matrix(self):
        """
        Reads a file with matrix and initializes it as a Graph attribute.
        """
        try:
            file = open(self.filename, "r").readlines()
            self.vertices = file[0].split()
            for line in file[2:]:
                list_of_weights = line.split()
                if len(list_of_weights) > 1:
                    num = 1
                    adjacency = {}
                    while num < len(self.vertices) + 1:
                        if list_of_weights[num] != "-":
                            adjacency[self.vertices[num - 1]] = int(list_of_weights[num])
                        num += 1
                    self.weights[list_of_weights[0]] = adjacency
        except FileNotFoundError:
            print('Wrong filename!')

    @staticmethod
    def extract(vertices_list, weight_list):
        """
        Returns the index, weight of vertex with minimal weight in list given.
        :param vertices_list:lst
        :param weight_list:lst
        :return:(int, str)
        """
        m = 0
        minimum = weight_list[0]
        for i in range(len(weight_list)):
            if weight_list[i] < minimum:
                minimum = weight_list[i]
                m = i
        return m, vertices_list[m]

    def search_by_dijkstra(self):
        """
        Returns shortest path vertices and their weight.
        :return: (dict, dict)
        """
        curr_graph = self.weights
        curr_vertices_list = [self.starting]
        path_dict = {self.starting: "-"}
        w = [0]
        curr_weight_dict = {}
        for v in curr_graph:
            curr_weight_dict[v] = float('inf')
            curr_vertices_list.append(v)
            w.append(curr_weight_dict[v])
        curr_weight_dict[self.starting] = 0
        path_vertices = []
        while curr_vertices_list:
            u = self.extract(curr_vertices_list, w)[1]
            path_vertices.append(u)
            curr_vertices_list.remove(u)
            for v in curr_graph[u]:
                if curr_weight_dict[v] >= curr_weight_dict[u] + curr_graph[u][v]:
                    curr_weight_dict[v] = curr_weight_dict[u] + curr_graph[u][v]
                    path_dict[v] = u
        return dict(sorted(curr_weight_dict.items())), dict(sorted(path_dict.items()))

    def min_distance(self, str_vertex, fin_vertex):
        """
        Returns the shortest path from starting ro final vertex and the summary weight of this path.
        :param str_vertex: str
        :param fin_vertex: str
        :return: (int, lst)
        """
        distance = self.result[0][fin_vertex]
        path = []
        while fin_vertex != str_vertex:
            path.insert(0, fin_vertex)
            fin_vertex = self.result[1][fin_vertex]
        path.insert(0, str_vertex)
        return distance, path

    def __str__(self):
        """
        Returns string representation of dijkstra  algorithm result.
        :return: str
        """
        self.result = self.search_by_dijkstra()
        min_dis = self.min_distance(self.starting, self.final)
        length = len(self.result[0]) * 9
        s = "\n" + " " * ((length - 19) // 2 + 2) + "Dijkstra's Algorithm" + " " * ((length - 20) // 2)
        s += "\n   " + "-" * length + "\n"
        s += "   | v:  |"
        for i in self.vertices:
            s += "   {}   |".format(i)
        s += "\n   " + "-" * length + "\n"
        s += "   | l:  |"
        for i in self.result[0]:
            s += "   {}".format(self.result[0][i]) + " " * (4 - len(str(self.result[0][i]))) + "|"
        s += "\n   " + "-" * length + "\n"
        s += "   | p:  |"
        for i in self.result[1]:
            s += "   {}   |".format(self.result[1][i])
        s += "\n   " + "-" * length + "\n"
        s += "\n > The shortest distance from {} to {} is: {}.\n".format(self.starting, self.final, min_dis[0])
        s += " > The path is: {}.".format(' -> '.join(min_dis[1]))
        return s