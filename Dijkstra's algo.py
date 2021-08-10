#prints minimum weighted path from root to all other nodes
def dij(nodes,edges,source_index=0):
    path_lengths={v:float('inf') for v in nodes}
    path_lengths[source_index]=0
    adjacent_nodes={v:{} for v in nodes}
    for (u,v),w in edges.items():
        adjacent_nodes[u][v]=w
        adjacent_nodes[u][v]=w
    temporary_nodes=[v for v in nodes]
    while len(temporary_nodes)>0:
        upper_bounds={v:path_lengths[v] for v in temporary_nodes}
        u=min(upper_bounds,key=upper_bounds.get)
        temporary_nodes.remove(u)
        for v,w in adjacent_nodes[u].items():
            path_lengths[v]=min(path_lengths[v],path_lengths[u]+w)
    print(path_lengths)
nodes=[0,1,2,3,4]
edges={(0,1):1.0,(0,4):1.0,(1,2):2.0,(2,3):4.0,(4,3):7.0}
dij(nodes,edges,0)

#output--> {0: 0, 1: 1.0, 2: 3.0, 3: 7.0, 4: 1.0}
