import sys
import time
import graph

def run_dijkstra(run_graph, run_heap, start_node, end_node):

    start = time.time()

    num_vertices = run_graph.get_num_vertices()
    distance_heap = run_heap
    visited_nodes = {}

    for i in range(1, num_vertices + 1):
        distance_heap.insert_node(i, sys.maxsize)
        visited_nodes[i] = False

    distance_heap.decrease_key(start_node, 0)

    nearest_neighbor = distance_heap.extract_min()
    current_node = nearest_neighbor[0]
    prev = {}
    
    while not visited_nodes[end_node]:

        neighbors_weighted = run_graph.all_edges_for_vertex(current_node)
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
        
        if current_node == end_node:
            path = get_shortest_path(prev, start_node, end_node)
            return True, nearest_neighbor[1], path, time.time() - start

        # Select nearest neighbor
        nearest_neighbor = distance_heap.extract_min()

        # No solution
        if nearest_neighbor[1] >= sys.maxsize:
            return False, "infinity", prev, time.time() - start

        current_node = nearest_neighbor[0]
        
        
def get_shortest_path(prev, start_node, end_node):

    curr_node = end_node
    solution_path = [end_node]

    while curr_node != start_node:
        solution_path.insert(0, prev[curr_node])
        curr_node = prev[curr_node]

    return solution_path
        