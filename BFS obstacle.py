from collections import deque

def bfs(graph, start_node, obstacles):
    # Initialize a queue for BFS
    queue = deque([start_node])
    # Set to keep track of visited nodes
    visited = set()
    # List to store the order of traversal
    traversal_order = []

    while queue:
        # Pop the current node from the queue
        current_node = queue.popleft()
        # If the node has not been visited and is not an obstacle
        if current_node not in visited and current_node not in obstacles:
            # Mark it as visited
            visited.add(current_node)
            # Add it to the traversal order
            traversal_order.append(current_node)
            # Add all unvisited neighbors (that are not obstacles) to the queue
            for neighbor in graph[current_node]:
                if neighbor not in visited and neighbor not in obstacles:
                    queue.append(neighbor)
    return traversal_order

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
# Nodes to skip (obstacles)
obstacles = {'B'}

# Perform BFS
print("BFS Traversal:", bfs(graph, start_node, obstacles))
