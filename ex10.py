from collections import defaultdict
def add_edge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)
def dfs_util(graph,v,visited):
    visited.add(v)
    print(v,end=' ')
    for neighbour in graph[v]:
        if neighbour not in visited:
            dfs_util(graph,neighbour,visited)
def dfs(graph,v):
    visited=set()
    dfs_util(graph,v,visited)

def bfs(graph,v):
    visited=set()
    queue=[v]
    visited.add(v)
    while queue:
        v=queue.pop(0)
        print(v,end=' ')
        for neighbour in graph[v]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
graph=defaultdict(list)
add_edge(graph,0,1)
add_edge(graph,0,2)
add_edge(graph,1,2)
add_edge(graph,2,3)
add_edge(graph,3,3)
print("dfs")
dfs(graph,2)
bfs(graph ,2)
