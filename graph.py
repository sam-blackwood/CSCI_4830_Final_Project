import numpy as np
from random import randint
from itertools import count, filterfalse # ifilterfalse on py2

class Graph:

    '''
    TO INITIALIZE: g = Graph(x) # where x is the number of nodes you want
    TO ADD AN EDGE: g.add_edge(2, 4, 10) # adding an edge between vertex 2 and vertex 4 with weight 10.

    A sample adjacency list for a graph with 4 nodes would look like this:
    self.adjacency_list = 
        {
            0: [(1, 24), (2, 12)],
            1: [(0, 24), (3, 5)],
            2: [(0, 12), (3, 50)],
            3: [(1, 5), (2, 50)]
        }

    NOTE: This graph is undirected, so an edge from 0 to 1 does imply an edge from 1 to 0 as well!
    NOTE: In the adjacency list for a node, there are tuples with the first element as the edge destination 
    and the second element being the weight of that edge
    '''


    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_edges = 0
        self.adjacency_list = {i : [] for i in range(1,num_vertices+1)} # label vertices 1,...,n

    def add_edge(self, v1, v2, weight):
        # add this check for purposes in random graph generation
        if not self.check_edge_exists(v1, v2):
            self.adjacency_list[v1].append((v2, weight))
            self.adjacency_list[v2].append((v1, weight))
            self.num_edges += 1
            return True
        return False

    def all_edges_for_vertex(self, vertex):
        return self.adjacency_list[vertex]
    
    def check_edge_exists(self, v1, v2):
        for edge in self.adjacency_list[v1]:
            if v2 == edge[0]:
                return True
        return False
    
    def add_prufer_sequence_edges(self, ps, max_weight):
        min_lst = [x for x in range(1,self.num_vertices+1)]
        n = len(ps)
        for _ in range(n):
            # find min node not in the Prufer sequence
            min = next(filterfalse(set(ps).__contains__, count(1)))
            min_lst.remove(min)
            edge_weight = randint(1, max_weight)
            self.add_edge(ps[0], min, edge_weight)
            # remove the first element of the Prufer sequence and add the min node
            ps.pop(0)
            ps.append(min)
            
        assert(len(min_lst)==2)
        self.add_edge(min_lst[0], min_lst[1], randint(1, max_weight))

    
def generate_prufer_sequence(n):
    return [randint(1,n) for _ in range(n-2)]

def generate_edge_pair(n):
    v1 = randint(1,n)
    v2 = randint(1,n)
    while v2 == v1:
        v2 = randint(1,n)
    return v1, v2

def generate_random_graph(n, max_weight):
    '''
    Parameters: n, the number of nodes in the random graph
                max_weight, the maximum allowed weight of an edge.
    Main idea: choose the number of edges in the graph according to a binomial distribution with 
    parameter N being the number of "extra" edges in the graph (i.e. n choose 2 - min_num_edges and 
    parameter p being 1/n. To ensure the graph is one connected component, construct a Prufer sequence that
    encodes a spanning tree of the graph. Adding these edges to the graph guarantees its connectedness.
    '''
    num_possible_edges = n*(n-1)/2 # n choose 2
    min_num_edges = n-1 # must have at least n-1 edges to have one connected component
    p = 1/n
    # choose an additional number of edges according to a binomial with p = 1/n
    num_edges = min_num_edges + np.random.binomial(num_possible_edges - min_num_edges, p)
    
    g = Graph(n)
    for _ in range(num_edges):
        v1, v2 = generate_edge_pair(n)
        edge_weight = randint(1,max_weight)
        while not g.add_edge(v1, v2, edge_weight):
            v1, v2 = generate_edge_pair(n)
    
    # now add prufer sequence edges to ensure it is one connected component
    g.add_prufer_sequence_edges(generate_prufer_sequence(n), max_weight)
    
    return g
            

def main():
    N = 6
    MAX_WEIGHT = 25
    rg = generate_random_graph(N, MAX_WEIGHT)
    print(rg.num_edges)
    print(rg.adjacency_list)

if __name__=="__main__":
    main()