import sys
def run_dijkstra(run_graph, run_heap, start_node, end_node):

    num_vertices = run_graph.get_num_vertices
    distance_heap = FibonacciHeap()
    visited_nodes = {}

    for i in range(1, num_vertices + 1):
        distance_heap.insert_node(i, sys.maxsize)
        visited_nodes[i] = False

    distance_heap.update_value(start_node, 0)

    solution_path = []

    current_node = start_node
    while not visited_nodes[end_node]:
        solution_path.append(current_node)
        neighbors_weighted = run_graph.all_edges_for_vertex(current_node)
        unvisited_neighbors_weighted = [x for x in neighbors_weighted if not visited_nodes[x[0]]]

        # Update distances and select nearest neighbor
        nearest_neighbor = None
        nearest_neighbor_dist = sys.maxsize

        for unvisited in unvisited_neighbors_weighted:
            current_distance = distance_heap.get_value(unvisited[0])
            potential_distance = distance_heap.get_value(current_node) + unvisited[1]
            
            if potential_distance < current_distance:
                distance_heap.update_value(unvisited[0], potential_distance)

                # Check if nearest neighbor
                if potential_distance < nearest_neighbor_dist:
                    nearest_neighbor = unvisited[0]
                    nearest_neighbor_dist = potential_distance

            else:
                # Check if nearest neighbor
                if current_distance < nearest_neighbor_dist:
                    nearest_neighbor = unvisited[0]
                    nearest_neighbor_dist = current_distance

        # Update current node as visited
        visited_nodes[current_node] = True

        # No solution
        if nearest_neighbor_dist >= sys.maxsize:
            return False, "infinity", solution_path

        current_node = nearest_neighbor

    return True, distance_heap.get_value(end_node), solution_path