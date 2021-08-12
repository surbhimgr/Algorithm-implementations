#DFS
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v,end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)
    def DFS(self,v):
        visited=set()
        self.DFSUtil(v,visited)
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.DFS(2)


#Another approach
from collections import defaultdict
def DFS(v,s):
    v.add(s)
    print(s,end=" ")
    for i in g[s]:
        if i not in v:
            DFS(v,i)
g=defaultdict(list)
g={0:[1,2],1:[2],2:[0,3],3:[3]}
s=2
v=set()
DFS(v,s)
