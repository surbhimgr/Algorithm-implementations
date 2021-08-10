# Python program to print all paths from a source to destination.

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def addEdge(self, u, v, w):
        self.graph[u].append([v,w])

    def printAllPathsUtil(self, u, d, visited, path,w,m):
        global k
        visited[u]= True
        path.append(u)
        if u == d:
            print(path)
            print(w)
            m.append(sum(w[:len(w)-k]))
            print(min(m))
        else:
            for i in self.graph[u]:
                if visited[i[0]]== False:
                    w.append(i[1])
                    self.printAllPathsUtil(i[0], d, visited, path,w,m)
        path.pop()
        w.pop()
        visited[u]= False
    def printAllPaths(self, s, d):
        visited =[False]*(self.V)
        path = []
        w=[0]
        m=[]
        global k
        self.printAllPathsUtil(s, d, visited, path,w,m)

g = Graph(5)
g.addEdge(0, 1,1)
g.addEdge(0, 4,1)
g.addEdge(1, 2,2)
g.addEdge(2, 3,4)
g.addEdge(4, 3,7)

s = 0 ; d = 3 ; k=1
print ("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d )

