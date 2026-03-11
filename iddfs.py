graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': [],
    '6': []
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