import sys
import time


'''
Written by Etash Kalra, Sam Blackwood, Sam Boehle (Fall 2022)

This method takes the following inputs:
1. A graph to run Dijkstra's. See graph.py for implementation of this graph
object. 
2. A heap to run Dijkstra's with. This could be either a wrapped version of the 
builtin heapq (see reg_heap.py) or a custom Fibonnaci heap (see fib_heap.py)
3. The node to start Dijkstra's on (integer indicating node number)
4. The node to start Dijkstra's on (integer indicating node number)

This method returns four outputs in tuple form:
1. True/False indicating whether or not a path was found
2. The last node visited in the algorithm (if successful, this should be the end_node)
3. The path taken to get from start_node to end_node (if not successful, this returns a
dictionary of all of the parent nodes of each visited node)
4. Time taken to run (for testing) (in seconds)

'''

def run_dijkstra(run_graph, run_heap, start_node, end_node):

    # Set startint time
    start = time.time()

    num_vertices = run_graph.get_num_vertices()

    # Make a copied reference to whatever heap we are using
    distance_heap = run_heap

    # Binary Dictionary of False/True dictating if a node is visited or not
    visited_nodes = {}

    # Fill visited_nodes with False values, and insert all nodes into heap w/ value infinity
    for i in range(1, num_vertices + 1):
        distance_heap.insert_node(i, sys.maxsize)
        visited_nodes[i] = False

    # Set starting node heap value to 0
    distance_heap.decrease_key(start_node, 0)

    # Get nearest neighbor. Note that values from the heap are returned as (key, value) or (node#, priority)
    nearest_neighbor = distance_heap.extract_min()
    current_node = nearest_neighbor[0]
    prev = {}
    
    while not visited_nodes[end_node]:

        neighbors_weighted = run_graph.all_edges_for_vertex(current_node)
        # Note that values from the heap are returned as (key, value) or (node#, priority)
        unvisited_neighbors_weighted = [x for x in neighbors_weighted if not visited_nodes[x[0]]]

        # Update distances
        for unvisited in unvisited_neighbors_weighted:
            current_distance = distance_heap.get_value(unvisited[0])
            potential_distance = nearest_neighbor[1] + unvisited[1]
            
            if potential_distance < current_distance:
                distance_heap.decrease_key(unvisited[0], potential_distance)
                prev[unvisited[0]] = current_node

        # Update current node as visited
        visited_nodes[current_node] = True
        
        # Solution found
        if current_node == end_node:
            path = get_shortest_path(prev, start_node, end_node)
            return True, nearest_neighbor[1], path, time.time() - start

        # Select nearest neighbor
        nearest_neighbor = distance_heap.extract_min()

        # No solution
        if nearest_neighbor[1] >= sys.maxsize:
            return False, nearest_neighbor[1], prev, time.time() - start

        # For continuing to next iteration
        current_node = nearest_neighbor[0]
        
        
def get_shortest_path(prev, start_node, end_node):

    curr_node = end_node
    solution_path = [end_node]

    while curr_node != start_node:
        solution_path.insert(0, prev[curr_node])
        curr_node = prev[curr_node]

    return solution_path
        