import sys
import time

def run_prims(run_graph, run_heap, start_node):

    start = time.time()

    num_vertices = run_graph.get_num_vertices()
    distance_heap = run_heap
    mst_set = {}
    mst_size = 0
    parents = {}

    for i in range(1, num_vertices + 1):
        distance_heap.insert_node(i, sys.maxsize)
        mst_set[i] = 0

    distance_heap.decrease_key(start_node, 0)
    parents[start_node] = 0

    while mst_size < num_vertices:

        # Select nearest neighbor
        new_addition = distance_heap.extract_min()

        # No solution
        if new_addition[1] >= sys.maxsize:
            return False, mst_set, parents, time.time() - start

        mst_set[new_addition[0]] = 1
        mst_size += 1

        neighbors_weighted = run_graph.all_edges_for_vertex(new_addition[0])
        unvisited_neighbors_weighted = [x for x in neighbors_weighted if not mst_set[x[0]]]

        for unvisited in unvisited_neighbors_weighted:
            current_distance = distance_heap.get_value(unvisited[0])
            potential_distance = new_addition[1] + unvisited[1]

            if potential_distance < current_distance:
                distance_heap.decrease_key(unvisited[0], potential_distance)
                parents[unvisited[0]] = new_addition[0]

    
    return True, mst_set, parents, time.time() - start


    