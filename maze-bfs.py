graphMaze = {
    'A': ['B'],
    'B': ['A','C'],
    'C': ['B','D'],
    'D': ['C','E','Y'],
    'E': ['D','F'],
    'F': ['E','G','I'],
    'G': ['F','H'],
    'H': ['G','J'],
    'I': ['F'],
    'J': ['H','K'],
    'K': ['J','L','M'],
    'L': ['K'],
    'M': ['K','N'],
    'N': ['M','O'],
    'O': ['N','P','Z'],
    'P': ['O','Q'],
    'Q': ['P','R'],
    'R': ['Q','S'],
    'S': ['R','T'],
    'T': ['S','U'],
    'U': ['T','V'],
    'V': ['U','W'],
    'W': ['V','X'],
    'X': ['W','Y'],
    'Y': ['X','D'],
    'Z': ['O']
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
        if start_node not in graph:
            print("Node does not exist in the graph")
            return;
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

start_state = "A"
goal_state = "A"
solution = bfs(graphMaze, start_state, goal_state)

print("Solution:", solution)