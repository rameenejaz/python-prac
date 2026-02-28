graph={
    '1':['2','3'],
    '2':['4','5'],
    '3':['6'],
    '4':[],
    '5':[],
    '6':[]
}
def dfs(graph, start_node, end_node):
    visited=set();
    if start_node not in graph:
        print("node does not exist in the graph");
        return;
    stack=[start_node];
    while stack:
        current=stack.pop();
        if current not in visited:
            visited.add(current);
            if current==end_node:
                print("goal node found: ",current);
                return True;
            for i in reversed(graph[current]):
                if i not in visited:
                    stack.append(i);
    print("goal node not found");
    return False;
dfs (graph,'1','6');
            