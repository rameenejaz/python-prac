# graphMaze = {
#     'A': ['B'],
#     'B': ['A','C'],
#     'C': ['B','D'],
#     'D': ['C','E','Y'],
#     'E': ['D','F'],
#     'F': ['E','G','I'],
#     'G': ['F','H'],
#     'H': ['G','J'],
#     'I': ['F'],
#     'J': ['H','K'],
#     'K': ['J','L','M'],
#     'L': ['K'],
#     'M': ['K','N'],
#     'N': ['M','O'],
#     'O': ['N','P','Z'],
#     'P': ['O','Q'],
#     'Q': ['P','R'],
#     'R': ['Q','S'],
#     'S': ['R','T'],
#     'T': ['S','U'],
#     'U': ['T','V'],
#     'V': ['U','W'],
#     'W': ['V','X'],
#     'X': ['W','Y'],
#     'Y': ['X','D'],
#     'Z': ['O']
# }
# def depth_limited_dfs(graph, current, goal, depth, visited):
#     if depth < 0:
#         return False
#     print(current)
#     if current == goal:
#         print("Goal found")
#         return True
#     visited.add(current)
#     for child in graph[current]:
#         if child not in visited:
#             if depth_limited_dfs(graph, child, goal, depth - 1, visited):
#                 return True
#     return False

# def iterative_deepening_dfs(graph, start_node, goal_node, max_depth):
#     if start_node not in graph:
#         print("The node does not exist in the graph")
#         return None

#     for depth in range(max_depth + 1):
#         print(f"\nDepth limit: {depth}")
#         visited = set()
#         if depth_limited_dfs(graph, start_node, goal_node, depth, visited):
#             return True
#     print("Goal not found")
#     return False
# # Call IDDFS
# iterative_deepening_dfs(graphMaze, 'A', 'Z', max_depth=25)



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


def depth_limited_dfs(graph, current, goal, depth, path, visited):

    print("Visiting:", current, "Depth remaining:", depth)

    visited.add(current)
    path.append(current)

    if current == goal:
        return path

    if depth == 0:
        path.pop()
        return None

    for child in graph[current]:
        if child not in visited:
            result = depth_limited_dfs(graph, child, goal, depth-1, path, visited)
            if result:
                return result

    path.pop()
    return None


def iterative_deepening_dfs(graph, start, goal, max_depth):

    for depth in range(max_depth + 1):

        print(f"\nSearching with depth limit: {depth}")

        visited = set()
        path = []

        result = depth_limited_dfs(graph, start, goal, depth, path, visited)

        if result:
            print("Path found:", result)
            return result

    print("Goal not found")
    return None

# Call IDDFS
iterative_deepening_dfs(graphMaze, 'A', 'Z', 25)