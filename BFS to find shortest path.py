from collections import deque

def bfs_shortest_path(graph, start_node, target_node):
    # Initialize a queue for BFS, each element is a tuple (node, path)
    queue = deque([start_node])
    # Set to keep track of visited nodes
    visited = set()
    # Dictionary to track the parent of each node (for reconstructing the path)
    parent = {}

    # Mark the start node as visited
    visited.add(start_node)
    parent[start_node] = None  # Start node has no parent

    while queue:
        # Pop the current node from the queue
        current_node = queue.popleft()

        # If the target node is found, reconstruct the path
        if current_node == target_node:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]  # Reverse the path to get it from start to target

        # Add all unvisited neighbors to the queue
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node  # Track the parent of the neighbor
                queue.append(neighbor)

    # If we exit the loop without finding the target, return None (no path)
    return None

# Graph representation
graph = {
   'A': ['B', 'C'],
   'B': ['A', 'D', 'E'],
   'C': ['A', 'F'],
   'D': ['B'],
   'E': ['B', 'F'],
   'F': ['C', 'E']
}

# Starting node
start_node = 'A'
# Target node
target_node = 'F'

# Perform BFS to find the shortest path
shortest_path = bfs_shortest_path(graph, start_node, target_node)
if shortest_path:
    print("Shortest Path:", shortest_path)
else:
    print(f"No path exists from {start_node} to {target_node}.")
