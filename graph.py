class Graph:

    '''
    TO INITIALIZE: g = Graph(x) # where x is the number of nodes you want
    TO ADD AN EDGE: g.add_edge(2, 4, 10) # adding an edge from vertex 2 to vertex 4 with weight 10.

    A sample adjacency list for a graph with 4 nodes would look like this:
    self.adjacency_list = 
        {
            0: [(1, 24), (2, 12)],
            1: [(0, 20), (3, 5)],
            2: [],
            3: [(2, 50)]
        }

    NOTE: This graph is directed, so an edge from 0 to 1 does not imply an edge from 1 to 0
    NOTE: In the adjacency list for a node, there are tuples with the first element as the edge destination 
    and the second element being the weight of that edge
    '''


    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = {i : [] for i in range(num_vertices)}

    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append((destination, weight))

    def all_edges_for_vertex(self, vertex):
        return self.adjacency_list[vertex]