from dijkstra_search import Graph

# file = str(input('Print the name of file with graph adjacency matrix :\n >>> '))
file = 'matrix.txt'
print("Searching in {} ...".format(file))
starting_vertex = str(input('Enter the name of starting vertex: \n >>> '))
final_vertex = str(input('Enter the name of final vertex: \n >>> '))
graph_example = Graph(file, starting_vertex, final_vertex)
try:
    graph_example.search_by_dijkstra()
    print(str(graph_example))
except KeyError:
    print('Wrong input! Try again.')