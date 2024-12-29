from collections import deque

def bfs (graph,start_node):
  #Initialize a queue for BFS
  queue= deque([start_node])
  #set to keep track of visited nodes
  visited =set()
  #list to store the order of traversal
  traversal_order = []



  while queue:
    #pop the current node from the queue
    current_node = queue.popleft()
    #if the node has not been visited
    if current_node not in visited:
      #mark it as visited
      visited.add(current_node)
      #Add it to the traversal order
      traversal_order.append(current_node)
      #Add all unvisited neighbors to the queue
      for neighbor in graph[current_node]:
        if neighbor not in visited:
          queue.append(neighbor)
  return traversal_order


graph={

   'A':['B','C'],
   'B':['A','D','E'],
   'C':['A','F'],
   'D':['B'],
   'E':['B','F'],
   'F':['C','E']
}

start_node='A'



print("BFS Traversal:",bfs(graph,start_node))
