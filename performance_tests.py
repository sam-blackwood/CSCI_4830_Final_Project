import numpy as np
import matplotlib.pyplot as plt

import graph
from fib_heap import FibonacciHeap
from dijkstras import run_dijkstra, get_shortest_path
from prims import run_prims
from reg_heap import MinHeap

def test_dijkstra(n_vals):
    
    t_vals = []
    
    for n in n_vals:    
        rg = graph.generate_random_graph(n, 1/n, 50)
        start_node = 1
        is_connected, end_node = graph.verify_connected_component(rg, start_node)

        if not is_connected:
            return False
        
        _, _, _, t = run_dijkstra(rg, FibonacciHeap(), start_node, end_node)
        t_vals.append(t)
        
    return t_vals


def main():
    
    # n_vals = [100*i for i in range(1,11)]
    # t_vals_dijkstra = test_dijkstra(n_vals)
    # plt.plot(n_vals, t_vals_dijkstra, label = 'Fibonacci Dijkstra')
    # plt.plot(n_vals, t_vals_dijkstra, 'o', color = 'black', markersize = 4)
    # plt.xlabel('Number of nodes')
    # plt.ylabel('Milliseconds')
    # plt.legend()
    # plt.show()
    
    g = graph.Graph(6)
    g.add_edge(1,2,3)
    g.add_edge(1,3,5)
    g.add_edge(2,4,2)
    g.add_edge(2,5,1)
    g.add_edge(3,4,1)
    g.add_edge(3,5,4)
    g.add_edge(5,6,9)
    g.add_edge(4,6,7)
    
    success, dist, shortest_path, t = run_dijkstra(g, FibonacciHeap(), 1, 6)
    print("distance: {}, path: {}".format(dist, shortest_path))

    success, dist, shortest_path, t = run_dijkstra(g, MinHeap(), 1, 6)
    print("distance: {}, path: {}".format(dist, shortest_path))
    
    # g = graph.Graph(4)
    # g.add_edge(1,2,1)
    # g.add_edge(2,3,1)
    # g.add_edge(3,4,1)
    # g.add_edge(1,4,2)
    
    # success, dist, prev, t = run_dijkstra(g, FibonacciHeap(), 1, 4)
    # print("distance: {}, path: {}".format(dist, get_shortest_path(prev,1,4)))
    

if __name__=='__main__':
    main()