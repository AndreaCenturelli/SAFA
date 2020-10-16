import json
import os

def save_remap(text ,instance_file: str,remap_file:str):
    graph=text.read().split('\n')
    n_nodes,n_edges=[int(_) for _ in graph[0].split(" ")]
    edges=[tuple([int(x) for x in y.split(' ')[0:2]]) for y in graph[1:n_edges+1]]
    n_term=int(graph[n_edges+1])
    sources=[int(y.split(' ')[0])  for y in graph[n_edges+2:]]
    sinks=[int(y.split(' ')[1])  for y in graph[n_edges+2:]]
  
    sources_r={k: sources[k-1] for k in range(1,n_term+1)}
    sinks_r={n_term+k: sinks[k-1] for k in range(1,n_term+1)}
    remap_newtoold={**sources_r,**sinks_r}
    nodes=[_ for _ in range(1,n_nodes+1)]
    for i in remap_newtoold.values():
        nodes.remove(i)
    nodes_r={2*n_term+k:nodes[k-1] for k in range(1,len(nodes)+1)}
    remap_newtoold={**remap_newtoold,**nodes_r}
    remap_oldtonew={k:v for v,k in remap_newtoold.items()}
    edges_r=[(remap_oldtonew[nodo1],remap_oldtonew[nodo2]) for nodo1,nodo2 in edges]
    with open(remap_file, "r+") as file:
        data = json.load(file)
        data.update({instance_file:{"new_to_old":remap_newtoold,"old_to_new":remap_oldtonew}})
        file.seek(0)
        json.dump(data, file)
        
def save_all_remap_files(tipodataset: str):
    for dirname in os.listdir(directory):
        remap_file=directory+"\\"+dirname+'\\remap.json'
        if not os.path.isfile(remap_file):
            with open(remap_file,'w') as json_file:
                json.dump({},json_file)
        for filename in os.listdir(directory+"\\"+dirname):
            if filename.endswith(".txt"):
                with open(directory+"\\"+dirname+"\\"+filename,"r") as text:
                    save_remap(text,filename,remap_file)
                    

def create_remapped_version(filepath,new_to_old:dict,old_to_new:dict):
    with open(filepath,"r") as text:
        old=text.read().split('\n')
        n_nodes,n_edges=[int(_) for _ in old[0].split(" ")]
        edges=[tuple([int(x) for x in y.split(' ')[0:2]]) for y in old[1:n_edges+1]]
        n_term=int(old[n_edges+1])
        sources=[int(y.split(' ')[0])  for y in old[n_edges+2:]]
        sinks=[int(y.split(' ')[1])  for y in old[n_edges+2:]]
        edges_r=[(old_to_new[str(nodo1)],old_to_new[str(nodo2)]) for nodo1,nodo2 in edges]
        sources_r=[old_to_new[str(source)] for source in sources]
        sinks_r=[old_to_new[str(sink)] for sink in sinks]
        with open(filepath[:-4]+"_REMAPPED.txt",'w') as txt:
                txt.write(str(n_nodes)+" "+str(n_edges))
                for i in range(0,n_edges):
                    txt.write("\n"+str(edges_r[i][0])+" "+str(edges_r[i][1]))
                txt.write("\n"+str(n_term))
                for i in range(0,n_term):
                    txt.write("\n"+str(sources_r[i])+" "+str(sinks_r[i]))
                    
def create_all_remaps(tipodataset:str):
    directory=os.getcwd()+'\\{}'.format(tipodataset)
    for dirname in os.listdir(directory):
        with open(directory+"\\"+dirname+"\\remap.json","r") as text:
            remap=json.load(text)
        for filename in os.listdir(directory+"\\"+dirname):
            if filename.endswith(".txt") and re.search(r'(?:REMAPPED)',filename)==None:
                filepath=directory+"\\"+dirname+"\\"+filename
                new_to_old=remap[filename]['new_to_old']
                old_to_new=remap[filename]['old_to_new']
                create_remapped_version(filepath,new_to_old,old_to_new)