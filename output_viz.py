import os 
import re
import matplotlib.pyplot as plt 
import networkx as nx
import json
import matplotlib.cm

out_filepath="C:\\Users\\centu\\OneDrive\\Documenti\\SAFA\\Project\\mesh15x15\\output\\com10_inst1.txt"
with open(out_filepath,"r") as txt:
    output=txt.read()

    
nodes1=re.findall(r"[\n\r].*From\s*([^\s]*)",output)
nodes2=re.findall(r"[\n\r].*to\s*([^\s]*)",output)
commodities=re.findall(r"[\n\r].*commodity: \s*([^\n]*)",output)
remap_filepath="C:\\Users\\centu\\OneDrive\\Documenti\\SAFA\\Project\\mesh15x15\\com10\\remap.json"
with open(remap_filepath,"r") as txt:
    remap=json.load(txt)
new_to_old=remap["mesh15x15_com10_inst1.txt"]["new_to_old"]
nodes1_old=[new_to_old[str(node1)] for node1 in nodes1]
nodes2_old=[new_to_old[str(node2)] for node2 in nodes2]
collegamenti=[(nodes1_old[idx],nodes2_old[idx])for idx in range(0,len(nodes1))]

graph_filepath="C:\\Users\\centu\\OneDrive\\Documenti\\SAFA\\Project\\mesh15x15\\com10\\mesh15x15_com10_inst1.txt"

####### mesh15x15
n=15
nodi=[]
for i in range(0,n):
    for j in range(0,15):
        nodi.append((i,j))
nodi=sorted(nodi)
nodes_lookup={k+1:v for k,v in enumerate(nodi)}

with open(graph_filepath,'r') as text:
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
opposites=[(edge[1],edge[0]) for edge in edges2]
edges2+=opposites
collegamenti2=[tuple([nodes_lookup[a] for a in list(collegamento)])for collegamento in collegamenti]
opposites=[(edge[1],edge[0]) for edge in collegamenti2]
collegamenti2+=opposites
grafo1=nx.grid_2d_graph(15,15)
grafo1.add_edges_from(edges2)
sources2=[nodes_lookup[a]for a in sources]
sinks2=[nodes_lookup[a] for a in sinks]

color_lookup={k:'#0000FF' for k in nodi}
for _ in sources2:
    color_lookup[_]='#00FF00'
for _ in sinks2:
    color_lookup[_]='#FFC0CB'

pos_15=dict( (n, n) for n in grafo1.nodes() )
unused_edges=[_ for _ in edges2 if _ not in collegamenti2]
color_lookup_edges={edge:23 for edge in unused_edges}

for idx in range(0,len(commodities)):
    color_lookup_edges[collegamenti2[idx]]=int(commodities[idx])
    print(idx)
    
for idx in range(0,len(commodities)):
    color_lookup_edges[collegamenti2[len(commodities)+idx]]=int(commodities[idx])
edge_cmap=matplotlib.cm.get_cmap('hsv')
labels={sources2[idx]: idx+1 for idx in range(0,22)}

for idx in range(0,22):
    labels[sinks2[idx]]=idx+1
node_size=[]
for node in nodi:
    if node in sources2 or node in sinks2:
        node_size.append(700)
    else:
        node_size.append(100)
fig=plt.figure(figsize=(16,16))
nx.draw(grafo1,pos_15,node_size=node_size,nodelist=color_lookup,edgelist=color_lookup_edges,
        edge_color=color_lookup_edges.values() ,node_color=color_lookup.values(),width=4.0,
        labels=labels,edge_cmap=edge_cmap,font_color='b',font_size=18)
fig.set_facecolor("#808080")
plt.savefig('example_of_paths.png',facecolor=fig.get_facecolor(), edgecolor='none')


