state_space = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6'],
  '4' : [],
  '5' : [],
  '6' : []
}

def bfs(graph, start_node, end_node):

    solution = []
    frontier = []  # a queue holding nodes that should be explored next.
    visited = [] # keeps track of nodes already visited, so we don’t revisit them.

    frontier.append(start_node)
    visited.append(start_node)
 # Main BFS Loop: 
 # The BFS loop runs as long as there are nodes in the frontier queue.

    while frontier:
        selected_node = frontier.pop(0)   # Dequeue from frontier. 
        # While there are nodes left in the frontier, remove the first element (queue behavior = FIFO).
# Goal Checking
        if selected_node == end_node:
            solution.append(selected_node)
            break
        
        solution.append(selected_node)
# The current node is added to the solution path.
# The algorithm iterates through all unvisited neighbors:
# Adds them to frontier (for future exploration).
# Marks them as visited.
        for neighbour in graph[selected_node]:
            if neighbour not in visited:
                frontier.append(neighbour)
                visited.append(neighbour)


    return solution

start_state = "1"
goal_state = "5"
solution = bfs(state_space, start_state, goal_state)

print("Solution:", solution)

