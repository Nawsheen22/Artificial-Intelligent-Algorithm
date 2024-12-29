def dfs(graph, start_node, visited):
    # Initialize a stack for DFS
    stack = [start_node]
    # List to store the order of traversal for the current component
    traversal_order = []

    while stack:
        # Pop the last node from the stack
        current_node = stack.pop()

        # If the node has not been visited
        if current_node not in visited:
            # Mark it as visited
            visited.add(current_node)
            # Add it to the traversal order
            traversal_order.append(current_node)

            # Add all unvisited neighbors to the stack
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


def check_connected_and_count_components(graph):
    visited = set()
    connected_components = 0
    all_components = []

    for node in graph:
        if node not in visited:
            # Perform DFS for each unvisited component
            component = dfs(graph, node, visited)
            all_components.append(component)
            connected_components += 1

    # Check if the graph is connected
    if connected_components == 1:
        print("The graph is connected.")
    else:
        print(f"The graph is not connected. It has {connected_components} connected components.")

    print("Connected Components:", all_components)
    return connected_components


# Example usage:
graph = {
    '5': ['9'],
    '6': ['2', '3'],
    '3': ['6','7'],
    '1': [],
    '2':['6'],
    '7':['3'],
    '9':['5']

}

check_connected_and_count_components(graph)
