
graph={
    'Arad':['Zerind','Timisora','Sibiu'],
    'Zerind':['Oradea','Arad'],
    'Oradea':['Sibiu','Zerind',],
    'Sibiu':['Arad','Oradea','Fagaras','Rimnicu Vilcea'],
    'Fagaras':['Sibiu','Bucharest'],
    'Rimnicu Vilcea':['Sibiu','Craiova','Pitesti'],
    'Timisora':['Arad','Lugoj'],
    'Lugoj':['Timisora','Mehadia'],
    'Mehadia':['Lugoj','Dobreta'],
    'Dobreta':['Mehadia','Craiova'],
    'Craiova':['Dobreta','Rimnicu Vilcea','Pitesti'],
    'Pitesti':['Rimnicu Vilcea','Craiova','Bucharest'],
    'Bucharest':['Fagaras','Pitesti','Giurgiu','Urziceni'],
    'Giurgiu':['Bucharest'],    
    'Urziceni':['Bucharest','Hirsova','Vaslui'],
    'Hirsova':['Urziceni','Eforie'],
    'Vaslui':['Urziceni','Iasi'],
    'Iasi':['Vaslui','Neamt'],
    'Neamt':['Iasi'],
    
}
def dfs(graph, start_node, goal_node):
    visited = set()
    if start_node not in graph:
        print("The node does not exist in the graph")
        return None
    stack = [start_node]
    while stack:
        current = stack.pop()  #it removes and returns the last node pushed onto the stack.
 #And ensures DFS explores the deepest node first.
        if current not in visited:
            print(current)
            visited.add(current) # Adds the current node to the visited set. 
            if current == goal_node:
                print("Goal found")
                return True
#for loop is used to retrieve all children of the current node.
#reversed() is used because stack is LIFO. and ensures left-to-right DFS traversal order
            for i in reversed(graph[current]):
                if i not in visited:
                    stack.append(i)

    print("Goal not found")
    return False
dfs (graph,'Arad','Bucharest');
            