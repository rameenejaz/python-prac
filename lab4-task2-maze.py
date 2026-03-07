graph = {
'A': ['B','F'],
'B': ['A','C'],
'C': ['B','D'],
'D': ['C','E'],   # goal
'E': ['D','G'],
'F': ['A','H'],
'G': ['E','L'],
'H': ['F','M'],
'I': ['N'],       # start
'J': ['K'],
'K': ['J','L'],
'L': ['G','K','Q'],
'M': ['H','R'],
'N': ['I','S'],
'O': ['P'],
'P': ['O','Q'],
'Q': ['L','P','W'],
'R': ['M','S'],
'S': ['R','T','N'],
'T': ['S','U'],
'U': ['T','V'],
'V': ['U','W'],
'W': ['V','Q']

}
def depth_limited_dfs(graph, current, goal, depth, visited):
    if depth < 0:
        return False
    print(current)
    if current == goal:
        print("Goal found")
        return True
    visited.add(current)
    for child in graph[current]:
        if child not in visited:
            if depth_limited_dfs(graph, child, goal, depth - 1, visited):
                return True
    return False

def iterative_deepening_dfs(graph, start_node, goal_node, max_depth):
    if start_node not in graph:
        print("The node does not exist in the graph")
        return None

    for depth in range(max_depth + 1):
        print(f"\nDepth limit: {depth}")
        visited = set()
        if depth_limited_dfs(graph, start_node, goal_node, depth, visited):
            return True
    print("Goal not found")
    return False
# Call IDDFS
iterative_deepening_dfs(graph, '1', '3', max_depth=5)