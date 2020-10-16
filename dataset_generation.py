import networkx as nx
import csv
import matplotlib.pyplot as plt
import json
import math
import random
import os
import re

def generate_dataset(tipodataset: str):
                
    if not os.path.isdir('./{}'.format(tipodataset)):
        os.mkdir('./{}'.format(tipodataset))
    cwd_mesh25=os.getcwd()+'\\{}'.format(tipodataset)
    for n_term in terminal_percentage:
        if not os.path.isdir('./{}/com{}'.format(tipodataset,n_term)):
            os.mkdir('./{}/com{}'.format(tipodataset,n_term))
            
    for n_term in terminal_percentage:
        with open(os.getcwd()+'\\{}_nodes.txt'.format(tipodataset),'r') as text:
            graph=text.read().split('\n')
            graph=[tuple([int(x) for x in y.split(' ')[0:2]]) for y in graph]
            n_nodes=graph[0][0]
            n_edges=graph[0][1]
            edges=graph[1:n_edges+1]
            terminals=int(n_nodes*n_term/100)
            
        grafo1=nx.Graph()
        grafo1.add_edges_from(edges)
       
        for inst in range (1,21):
            nodi=sorted(list(grafo1.nodes()))
            sinks=[]
            sources=[]
            for i in range(1,terminals+1):
                sources.append(nodi.pop(random.randint(0,len(nodi)-1)))
                sinks.append(nodi.pop(random.randint(0,len(nodi)-1)))
                txt.write(str(n_nodes)+" "+str(n_edges))
                for i in range(0,n_edges):
                    txt.write("\n"+str(edges[i][0])+" "+str(edges[i][1]))
                txt.write("\n"+str(terminals))
                for i in range(0,terminals):
                    txt.write("\n"+str(sources[i])+" "+str(sinks[i]))
    










