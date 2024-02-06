def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Initialize visited set
    visited = set()
    
    while len(visited) < len(graph):
        # Find the node with the smallest distance that has not been visited yet
        min_distance = float('inf')
        min_node = None
        for node, distance in distances.items():
            if node not in visited and distance < min_distance:
                min_distance = distance
                min_node = node
        
        # Add the node to the visited set
        visited.add(min_node)
        
        # Update distances to neighbors of the current node
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Example usage
start_node = 'A'
print("Shortest distances from node", start_node, ":", dijkstra(graph, start_node))
