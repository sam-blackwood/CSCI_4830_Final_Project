import numpy as np
import matplotlib.pyplot as plt

import graph
from fib_heap import FibonacciHeap
from dijkstras import run_dijkstra
from prims import run_prims
from reg_heap import MinHeap

class Result:
    
    def __init__(self, s, d, p, t):
        self.success = s
        self.distance = d
        self.path = p
        self.time = t

def test_dijkstra(n_vals, sparse):
    
    solution_lst_fib = []
    solution_lst_min = []
    
    if sparse:
    
        for n in n_vals:
                
            rg = graph.generate_random_graph(n, 1/n, 50)

            start_node = 1
            is_connected, end_node = graph.verify_connected_component(rg, start_node)

            if not is_connected:
                return False
            
            s1, dist1, path1, t1 = run_dijkstra(rg, FibonacciHeap(), start_node, end_node)
            s2, dist2, path2, t2 = run_dijkstra(rg, MinHeap(), start_node, end_node)
            
            solution_lst_fib.append(Result(s1, dist1, path1, t1))
            solution_lst_min.append(Result(s2, dist2, path2, t2))
            
    else:
        
        for n in n_vals:
                
            rg = graph.generate_random_graph(n, 0.1, 50)

            start_node = 1
            is_connected, end_node = graph.verify_connected_component(rg, start_node)

            if not is_connected:
                return None, None
            
            s1, dist1, path1, t1 = run_dijkstra(rg, FibonacciHeap(), start_node, end_node)
            s2, dist2, path2, t2 = run_dijkstra(rg, MinHeap(), start_node, end_node)
            
            solution_lst_fib.append(Result(s1, dist1, path1, t1))
            solution_lst_min.append(Result(s2, dist2, path2, t2))
            
        
    return solution_lst_fib, solution_lst_min


def test_prim(n_vals):
    
    t_vals_fib = []
    t_vals_min = []
    
    for n in n_vals:
        
        rg = graph.generate_random_graph(n, 1/n, 50)
        start_node = 1
        
        _, _, _, t1 = run_prims(rg, FibonacciHeap(), start_node)
        _, _, _, t2 = run_prims(rg, MinHeap(), start_node)
        
        t_vals_fib.append(t1)
        t_vals_min.append(t2)
        
    return t_vals_fib, t_vals_min


def main():
    
    sparse_n_vals = [1000*i for i in range(1,21)]
    # soln_fib, soln_min = test_dijkstra(n_vals=sparse_n_vals, sparse=False)
    # t_vals_fib = [res.time for res in soln_fib]
    # t_vals_min = [res.time for res in soln_min]
    
    t_vals_fib, t_vals_min = test_prim(sparse_n_vals)
    
    plt.figure(figsize=(8,6))
    plt.semilogy(sparse_n_vals, t_vals_fib, label = 'Fibonacci Prim')
    plt.semilogy(sparse_n_vals, t_vals_fib, 'o', color = 'black', markersize = 4)
    plt.semilogy(sparse_n_vals, t_vals_min, label = 'Min Heap Prim')
    plt.semilogy(sparse_n_vals, t_vals_min, 'o', color = 'black', markersize = 4)
    plt.xlabel('Number of nodes')
    plt.ylabel('Milliseconds')
    plt.title('Performance of Prim\'s Algorithm on Sparse Graph')
    plt.legend()
    plt.show()
    

if __name__=='__main__':
    main()