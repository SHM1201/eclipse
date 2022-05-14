from collections import deque


vert=int(input("Enter the number of vertices: "))
graph={}
for i in range(vert):
    ver=input("Enter the name of vertex: ")
    edges=set(map(int,input("Enter space separated adjacent vertices: ").split()))
    graph[ver]=edges
print(graph)
def dfs(start):
    visited=set()
    visited.add(start)
    l=[]
    l.append(start)
    while len(l) > 0:
        x=l.pop()
        visited.add(x)
        print(x,end=" ")
        l+=list(graph[x]-visited)
    print()

def bfs(start):
    visited=set()
    visited.add(start)
    q=deque()
    q.append(start)
    while (len(q) > 0):
        v=q.popleft()
        # visited.add(v)
        print(v,end=" ")
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)
    print()

start=input("Enter start vertex: ")
bfs(start)
dfs(start)