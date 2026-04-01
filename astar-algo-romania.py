import heapq 
# Graph representation with cities as nodes and edges with weights (distances)
graph = {
    'Arad':[('Zerind',75), ('Timisora',118), ('Sibiu',140)],
    'Zerind':[('Oradea',71), ('Arad',75)],
    'Oradea':[('Sibiu',151), ('Zerind',71)],
    'Sibiu':[('Arad',140), ('Oradea',151), ('Fagaras',99), ('Rimnicu Vilcea',80)],
    'Fagaras':[('Sibiu',99), ('Bucharest',211)],
    'Rimnicu Vilcea':[('Sibiu',80), ('Craiova',146), ('Pitesti',97)],
    'Timisora':[('Arad',118), ('Lugoj',111)],
    'Lugoj':[('Timisora',111), ('Mehadia',70)],
    'Mehadia':[('Lugoj',70), ('Dobreta',75)],
    'Dobreta':[('Mehadia',75), ('Craiova',138)],
    'Craiova':[('Dobreta',138), ('Rimnicu Vilcea',146), ('Pitesti',138)],
    'Pitesti':[('Rimnicu Vilcea',97), ('Craiova',138), ('Bucharest',101)],
    'Bucharest':[('Fagaras',211), ('Pitesti',101), ('Giurgiu',90), ('Urziceni',85)],
    'Giurgiu':[('Bucharest',90)],
    'Urziceni':[('Bucharest',85), ('Hirsova',98), ('Vaslui',142)],
    'Hirsova':[('Urziceni',98), ('Eforie',86)],
    'Vaslui':[('Urziceni',142), ('Iasi',92)],
    'Iasi':[('Vaslui',92), ('Neamt',87)],
    'Neamt':[('Iasi',87)],
    
}

heuristic = {'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Fagaras': 178, 'Rimnicu Vilcea': 193, 'Timisora': 329, 'Lugoj': 244, 'Mehadia': 241, 'Dobreta': 242, 'Craiova': 160, 'Pitesti': 100, 'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80, 'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234}

def AStarSearch(start, goal):
    """A* search algorithm to find the optimal path from start to goal."""
    
    # Priority queue (min-heap) for opened nodes
    opened = []
    heapq.heappush(opened, (heuristic[start], 0, start, []))  # (f(n), g(n), node, path)

    # Cost dictionary (tracks actual cost g(n))
    cost = {start: 0}

    while opened:
        _, g, node, path = heapq.heappop(opened)  # Get node with lowest f(n)

        path = path + [node]  # Add current node to path
        
        if node == goal:  # Goal found
            return path, g  # Return optimal path and cost

        for neighbor, weight in graph.get(node, []):
            new_cost = g + weight  # g(n) = cost so far + edge weight

            if neighbor not in cost or new_cost < cost[neighbor]:  # Found better path
                cost[neighbor] = new_cost
                f = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(opened, (f, new_cost, neighbor, path))  # Push updated path

    return None, float('inf')  # No path found

# Run A* Search from 'A' to 'G'
optimal_path, total_cost = AStarSearch('Arad', 'Neamt')

# Print results
if optimal_path:
    print(f"Optimal Path: {' → '.join(optimal_path)}")
    print(f"Total Cost: {total_cost}")
else:
    print("No path found!")