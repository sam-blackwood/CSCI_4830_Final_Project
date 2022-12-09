import sys
import time

'''
Written by Etash Kalra, Sam Blackwood, Sam Boehle (Fall 2022)

This method takes the following inputs:
1. A graph to run Prims's. See graph.py for implementation of this graph
object. 
2. A heap to run Prims's with. This could be either a wrapped version of the 
builtin heapq (see reg_heap.py) or a custom Fibonnaci heap (see fib_heap.py)
3. The node to start Prims's on (integer indicating node number)

This method returns four outputs in tuple form:
1. True/False indicating whether or not a path was found
2. A binary dictionary of 0s/1s indicating whether a node was included in the MST or not. 
3. A dictionary with the parent of each node in the MST (note that the start_node has value 0 to indicate no parent)
4. Time taken to run (for testing) (in seconds)

'''

def run_prims(run_graph, run_heap, start_node):

    # Set startint time
    start = time.time()

    num_vertices = run_graph.get_num_vertices()

    # Make a copied reference to whatever heap we are using
    distance_heap = run_heap

    # Binary dictionary of 0/1 to indicate if a node has been visited or not
    mst_set = {}

    # Number of nodes visited
    mst_size = 0

    # Dictionary of parents for each node in the resulting tree
    parents = {}

    # Fill MST_set with 0s to indicate no visitations, and inssert all nodes into heap w/ value infinity
    for i in range(1, num_vertices + 1):
        distance_heap.insert_node(i, sys.maxsize)
        mst_set[i] = 0

    # Get nearest neighbor. Note that values from the heap are returned as (key, value) or (node#, priority)
    distance_heap.decrease_key(start_node, 0)

    # Set parent of start_node to None.
    parents[start_node] = 0

    while mst_size < num_vertices:

        # Select nearest neighbor. Note that values from the heap are returned as (key, value) or (node#, priority)
        new_addition = distance_heap.extract_min()

        # No solution
        if new_addition[1] >= sys.maxsize:
            return False, mst_set, parents, time.time() - start

        # Set the nearest_neighbor to be visited (1 indicator in mst_set)
        mst_set[new_addition[0]] = 1
        mst_size += 1

        # Update distances in heap
        neighbors_weighted = run_graph.all_edges_for_vertex(new_addition[0])
        unvisited_neighbors_weighted = [x for x in neighbors_weighted if not mst_set[x[0]]]

        for unvisited in unvisited_neighbors_weighted:
            current_distance = distance_heap.get_value(unvisited[0])
            potential_distance = new_addition[1] + unvisited[1]

            if potential_distance < current_distance:
                distance_heap.decrease_key(unvisited[0], potential_distance)
                parents[unvisited[0]] = new_addition[0]

    
    return True, mst_set, parents, time.time() - start


    