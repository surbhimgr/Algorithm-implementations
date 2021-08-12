from collections import defaultdict
g=defaultdict(list)
g={0:[1,2],1:[2],2:[0,3],3:[3]}
s=2
v=[False]*(max(g)+1)
qu=[]
qu.append(s)
v[s]=True
while qu:
    s=qu.pop(0)
    print(s,end=" ")
    for i in g[s]:
        if v[i]==False:
            qu.append(i)
            v[i]=True
