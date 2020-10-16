import networkx as nx
import csv
import matplotlib.pyplot as plt
import json
import math
import random
####### b1-.... 500x1020
## 
# n_nodes=500
# n_edges=1020
# for i in range(1,4):
#     with open(str(i)+'.txt','r') as text:
#         graph=text.read()
#         lista=graph.split('\n')
#         listona=[tuple([int(x) for x in y.split(' ')[0:2]]) for y in lista]
#         edges=listona[1:n_edges+1]
#         sources=[x[0] for x in listona[n_edges+2:]]
#         sinks=[x[1] for x in listona[n_edges+2:]]
#     nodes=[x for x in range(0,500)]
    
#     grafo1=nx.Graph()
#     grafo1.add_edges_from(edges)
#     nodi=sorted(list(grafo1.nodes()))
#     color_lookup={k:'#0000FF' for k in nodi}
#     for _ in sources:
#         color_lookup[_]='#00FF00'
#     for _ in sinks:
#         color_lookup[_]='#FF0000'
#     if "pos_b1" not in  globals():
#         pos_b1=nx.spring_layout(grafo1)
    
#     plt.figure(figsize=(32,32))
#     nx.draw(grafo1,pos_b1,node_size=300,nodelist=color_lookup,node_color=color_lookup.values())
#     plt.savefig(str(i)+'.png')

####### mesh15x15
n=15
nodi=[]
for i in range(0,n):
    for j in range(0,15):
        nodi.append((i,j))
nodi=sorted(nodi)
nodes_lookup={k+1:v for k,v in enumerate(nodi)}

for i in range(4,7):
    print(i)
    with open(str(i)+'.txt','r') as text:
        graph=text.read()
        lista=graph.split('\n')
        listona=[tuple([int(x) for x in y.split(' ')[0:2]]) for y in lista]
        n_nodes=listona[0][0]
        n_edges=listona[0][1]
        edges=listona[1:n_edges+1]
        terminals=listona[n_edges+1][0]
        sources=[x[0] for x in listona[n_edges+2:]]
        sinks=[x[1] for x in listona[n_edges+2:]]
    nodes=[x for x in range(0,n_nodes)]
    edges2=[tuple([nodes_lookup[a] for a in list(edge)])for edge in edges]
    grafo1=nx.grid_2d_graph(15,15)
    grafo1.add_edges_from(edges2)
    sources2=[nodes_lookup[a]for a in sources]
    sinks2=[nodes_lookup[a] for a in sinks]
    # grafo1.add_edges_from(edges)
    # nodi=sorted(list(grafo1.nodes()))
    # color_lookup={k:'#0000FF' for k in nodi}
    # for i in range(1,terminals+1):
    #     source=nodi.pop(random.randint(0,len(nodi)-1))
    #     color_lookup[source]='#00FF00'
    # for i in range(1,terminals+1):
    #     sink=nodi.pop(random.randint(0,len(nodi)-1))
    #     color_lookup[sink]='#FF0000'
    #     nodi=sorted(list(grafo1.nodes()))
    color_lookup={k:'#0000FF' for k in nodi}
    for _ in sources2:
        color_lookup[_]='#00FF00'
    for _ in sinks2:
        color_lookup[_]='#FF0000'
    if "pos_b1" not in  globals():
        pos_b1=nx.spring_layout(grafo1)
    if "pos_15" not in  globals():
        pos_15=dict( (n, n) for n in grafo1.nodes() )
    
    plt.figure(figsize=(32,32))
    nx.draw(grafo1,pos_15,node_size=300,nodelist=color_lookup,node_color=color_lookup.values())
    plt.savefig(str(i)+'.png')
    
    
# ####### mesh25x25
# n=25
# nodi=[]
# for i in range(0,n):
#     for j in range(0,n):
#         nodi.append((i,j))
# nodi=sorted(nodi)
# nodes_lookup={k+1:v for k,v in enumerate(nodi)}

# for i in range(7,10):
#     print(i)
#     with open(str(i)+'.txt','r') as text:
#         graph=text.read()
#         lista=graph.split('\n')
#         listona=[tuple([int(x) for x in y.split(' ')[0:2]]) for y in lista]
#         n_nodes=listona[0][0]
#         n_edges=listona[0][1]
#         edges=listona[1:n_edges+1]
#         terminals=listona[n_edges+1][0]
#         sources=[x[0] for x in listona[n_edges+2:]]
#         sinks=[x[1] for x in listona[n_edges+2:]]
#     nodes=[x for x in range(0,n_nodes)]
#     edges2=[tuple([nodes_lookup[a] for a in list(edge)])for edge in edges]
#     grafo1=nx.grid_2d_graph(n,n)
#     grafo1.add_edges_from(edges2)
#     sources2=[nodes_lookup[a]for a in sources]
#     sinks2=[nodes_lookup[a] for a in sinks]
#     # grafo1.add_edges_from(edges)
#     # nodi=sorted(list(grafo1.nodes()))
#     # color_lookup={k:'#0000FF' for k in nodi}
#     # for i in range(1,terminals+1):
#     #     source=nodi.pop(random.randint(0,len(nodi)-1))
#     #     color_lookup[source]='#00FF00'
#     # for i in range(1,terminals+1):
#     #     sink=nodi.pop(random.randint(0,len(nodi)-1))
#     #     color_lookup[sink]='#FF0000'
#     #     nodi=sorted(list(grafo1.nodes()))
#     color_lookup={k:'#0000FF' for k in nodi}
#     for _ in sources2:
#         color_lookup[_]='#00FF00'
#     for _ in sinks2:
#         color_lookup[_]='#FF0000'
#     if "pos_b1" not in  globals():
#         pos_b1=nx.spring_layout(grafo1)
#     if "pos_15" not in  globals():
#         pos_15=dict( (n, n) for n in grafo1.nodes() )

    
#     plt.figure(figsize=(32,32))
#     nx.draw(grafo1,pos_15,node_size=300,nodelist=color_lookup,node_color=color_lookup.values())
#     plt.savefig(str(i)+'.png')
    
    
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    