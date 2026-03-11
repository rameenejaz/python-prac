graph ={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

def dfs(graph,startNode, endNode):
    visited=set();
    if startNode not in graph:
        print("start node does not exist.")
        return;
    stack=[startNode];
    while stack:
        current=stack.pop();
        if current not in visited:
            visited.add(current)
            if current==endNode:
                print("Goal node found:",current);
                return True;
            for i in reversed(graph[current]):
                stack.append(i)

    print("goal not found")
    return False;
dfs(graph,'A','E');
