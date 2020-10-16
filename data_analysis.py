import os 
from os.path import isfile, join
import re
import matplotlib.pyplot as plt 
import networkx as nx
import json
import matplotlib.cm
import numpy as np
import pandas as pd 
import statistics

out_dir="C:\\Users\\centu\\OneDrive\\Documenti\\SAFA\\Project\\mesh15x15\\output"
onlyfiles = [f for f in os.listdir(out_dir) if isfile(join(out_dir, f)) and f.endswith(".txt")]
out_data={}
for out_file in onlyfiles:    ####################### TOGLI 0:14 ############
    file_path=join(out_dir,out_file)
    with open(file_path,"r") as txt:
        output=txt.read()
        times=[float(_) for _ in re.findall(r"[\n\r].*Time: ;*([^;]*)",output)]
        new_sols=[int(_) for _ in re.findall(r"[\n\r].*New sol: ;*([^;]*)",output)]
        improvements=[new_sols[i+1]-new_sols[i] for i in range(0,len(new_sols)-1)]
        abs_gaps=[float(_) for _ in re.findall(r"[\n\r].*ABS_GAP: ;*([^;]*)",output)]
        rel_gaps=[float(_) for _ in re.findall(r"[\n\r].*REL_GAP: \s*([^\s]*)",output)]
        total_time=float(re.findall(r"[\n\r].*Total time: \D*([^\D]*)",output)[0])
        best_bound=float(re.findall(r"[\n\r].*Best bound: \D*([^\D]*)",output)[0])
        objective_value=int(re.findall(r"[\n\r].*Objective value: \s*([^\s]*)",output)[0])
        active_nodes=int(re.findall(r"[\n\r].*Active nodes: \s*([^\s]*)",output)[0])
        solved_nodes=int(re.findall(r"[\n\r].*Solved nodes: \s*([^\s]*)",output)[0])
        if re.search(r"Stopping search for min GAP",output)!=None:
            stop_for_gap=True
        else:
            stop_for_gap=False
        out_data[out_file]={"Times": times,"New solutions": new_sols,
                            "Improvements": improvements,
                            "Absolute gaps": abs_gaps,"Relative gaps":rel_gaps,
                            "Total time":total_time,"Best bound":best_bound,
                            "Objective value":objective_value,"Active nodes":active_nodes,
                            "Solved value":solved_nodes,"Interrupted":stop_for_gap}
        out_data_file="output_data.json"
        with open(join(out_dir,out_data_file),"w") as txt:
            json.dump(out_data,txt)
        
    
        x = np.arange(10)
        width=0.35
        fig, (ax1,ax2) = plt.subplots(2)
        ax1.grid(axis='y',zorder=0)
        ax2.grid(axis='y',zorder=0)

        rects1 = ax1.bar(x - width/2, [out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[10:20]], width, 
                        color=(0.2, 0.4, 0.6, 0.6),label='Best solution',zorder=3)
        rects2 = ax1.bar(x + width/2, [out_data[inst]["Best bound"] for 
                                      inst in list(out_data.keys())[10:20]], width,
                        color='black',label='Best bound',zorder=3)
        ax1.plot([0-width,9+width],[56]*2,label="Number of commodities")
        ax1.set_ylabel('Commodities',fontsize='xx-large')
        ax1.set_title('Com25',fontsize='xx-large')
        ax1.set_xticks(x)
        ax1.set_xticklabels([str(i) for i in range(1,11)])
        ax1.legend(loc=1,fontsize='xx-large')
        rects1 = ax2.bar(x - width/2, [out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[20:]], width, 
                        color=(0.2, 0.4, 0.6, 0.6),label='Best solution',zorder=3)
        rects2 = ax2.bar(x + width/2, [out_data[inst]["Best bound"] for 
                                      inst in list(out_data.keys())[20:]], width,
                        color='black',label='Best bound',zorder=3)
        ax2.plot([0-width,9+width],[90]*2)
        ax2.set_ylabel('Commodities',fontsize='xx-large')
        ax2.set_title('Com40',fontsize='xx-large')
        ax2.set_xticks(x)
        ax2.set_xticklabels([str(i) for i in range(1,11)])
        fig.tight_layout()
        fig.tight_layout()
        plt.show()     
        ############################################################
        
        x = np.arange(10)
        width=0.35
        fig, (ax0,ax1,ax2) = plt.subplots(3)
        ax0.grid(axis='y',zorder=0)
        ax1.grid(axis='y',zorder=0)
        ax2.grid(axis='y',zorder=0)
        rects1 = ax0.bar(x - width/2, [out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[:10]], width, 
                        color=(0.2, 0.4, 0.6, 0.6),label='Best solution',zorder=3)
        rects2 = ax0.bar(x + width/2, [out_data[inst]["Best bound"] for 
                                      inst in list(out_data.keys())[:10]], width,
                        color='black',label='Best bound',zorder=3)
        ax0.plot([0-width,9+width],[22]*2,label="Number of commodities")
        ax0.set_ylabel('Commodities',fontsize='xx-large')
        ax0.set_title('Com25',fontsize='xx-large')
        ax0.set_xticks(x)
        ax0.set_xticklabels([str(i) for i in range(1,11)])
        
        
        
        rects1 = ax1.bar(x - width/2, [out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[10:20]], width, 
                        color=(0.2, 0.4, 0.6, 0.6),label='Best solution',zorder=3)
        rects2 = ax1.bar(x + width/2, [out_data[inst]["Best bound"] for 
                                      inst in list(out_data.keys())[10:20]], width,
                        color='black',label='Best bound',zorder=3)
        ax1.plot([0-width,9+width],[56]*2,label="Number of commodities")
        ax1.set_ylabel('Commodities',fontsize='xx-large')
        ax1.set_title('Com25',fontsize='xx-large')
        ax1.set_xticks(x)
        ax1.set_xticklabels([str(i) for i in range(1,11)])
        rects1 = ax2.bar(x - width/2, [out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[20:]], width, 
                        color=(0.2, 0.4, 0.6, 0.6),label='Best solution',zorder=3)
        rects2 = ax2.bar(x + width/2, [out_data[inst]["Best bound"] for 
                                      inst in list(out_data.keys())[20:]], width,
                        color='black',label='Best bound',zorder=3)
        ax2.plot([0-width,9+width],[90]*2)
        ax2.set_ylabel('Commodities',fontsize='xx-large')
        ax2.set_title('Com40',fontsize='xx-large')
        ax2.set_xticks(x)
        ax2.set_xticklabels([str(i) for i in range(1,11)])
        # fig.tight_layout()
        plt.show()     
        
        
        print([out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[:10]],
              [out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[10:20]],
              [out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[20:30]])
        
        com10_mean=round(statistics.mean([out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[:10]]),2)
        
        com25_mean=round(statistics.mean([out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[10:20]]),2)
        
        com40_mean=round(statistics.mean([out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[20:30]]),2)
        
        com10_variance=round(statistics.variance([out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[:10]]),2)
        
        com25_variance=round(statistics.variance([out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[10:20]]),2)
        
        com40_variance=round(statistics.variance([out_data[inst]["Objective value"] for 
                                      inst in list(out_data.keys())[20:30]]),2)
        
        
        data=np.array(['Terminals number','Instance number','Best bound','Best solution','Total time'])
        
        for out_file in out_data.keys():
            diz=out_data[out_file]
            inst_n=re.findall(r"_inst*([^.]*)",out_file)[0]
            data=np.vstack((data,[out_file[:5],inst_n,diz['Best bound'],
                                 diz['Objective value'],diz['Total time']]))
        df=pd.DataFrame(data)
        excel_path='datas.xlsx'
        df.to_excel(excel_path,index=False)