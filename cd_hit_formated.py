#!/usr/bin/python3
# -*- coding: utf-8 -*-
###############################>GENERAL-INFORMATIONS<###############################
"""
Build in Python 3.6

Author:
Filipe Dezordi
zimmer.filipe@gmail.com
https://github.com/dezordi

Dependencies:
CD-HIT version 4.7
"""
###############################>LIBRARIES<###############################

import pandas as pd
import numpy as np
import argparse, csv, os, subprocess, shlex, sys, time, re

###############################>ARGUMENTS<###############################
parser = argparse.ArgumentParser(description = 'This scripts receives a fasta file and execute a cd-hit-est analysis and formats the cd-hit output',formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-in", "--input", help="Fasta file", required=True)
parser.add_argument("-p","--threads",help="Threads for cd-hit-est analyze. Default = 1", default = str(1), type=str)
parser.add_argument("-m","--memory",help="Memory in MB for cd-hit-est analyze. Default = 2000",default = str(2000), type=str)
parser.add_argument("-md","--mode",help="CD-hit mode, options: nucl or prot. Default = nucl",type=str, choices=['nucl','prot'], default='nucl')
parser.add_argument("-cd","--cdhit",help="CD-hit line arguments eg. '-c 0.8 -aL 0.8 -g 1 -n 8 -d 200'",type=str)
#Storing argument on variables
args = parser.parse_args()
input_file = args.input
var_threads = args.threads
var_memory = args.memory
cd_mod = args.mode
cd_line = args.cdhit
print(cd_line)
###############################>EXECUTION<###############################
#Creating lists to store genome assemblies and viral taxonomy
if cd_mod == 'nucl':
    with open(input_file+'.cd-hit-est.log','w') as cd_hit_log:
        cd_hit_out = input_file+'.cd'
        cd_hit_est_cmd = 'cd-hit-est -i '+input_file+' -o '+cd_hit_out+' '+cd_line+' -M '+var_memory+' -T '+var_threads
        cd_hit_est_cmd = shlex.split(cd_hit_est_cmd)
        cd_hit_est_cmd_process = subprocess.Popen(cd_hit_est_cmd,stdout = cd_hit_log)
        cd_hit_est_cmd_process.wait()
elif cd_mod == 'prot':
    with open(input_file+'.cd-hit.log','w') as cd_hit_log:
        cd_hit_out = input_file+'.cd'
        cd_hit_est_cmd = 'cd-hit -i '+input_file+' -o '+cd_hit_out+' '+cd_line+' -M '+var_memory+' -T '+var_threads
        cd_hit_est_cmd = shlex.split(cd_hit_est_cmd)
        cd_hit_est_cmd_process = subprocess.Popen(cd_hit_est_cmd,stdout = cd_hit_log)
        cd_hit_est_cmd_process.wait()
with open(input_file+'.cd.clstr','r') as cluster_file, open(input_file+'.cd.clstr.tsv','w') as cluster_formated:
    cluster_file_reader = cluster_file.readlines()
    cluster_formated_writer = csv.writer(cluster_formated,delimiter='\t')
    cluster_formated_writer.writerow(['Sequence','Cluster','Representative','Copies'])
    cluster_list = []
    for line in cluster_file_reader:
        line = line.rstrip('\n')
        if 'Cluster' in line:
            cluster_number = re.sub(r'>Cluster ','',line)
        else:
            if 'at ' in line:
                representative = 'FALSE'
            else:
                representative = 'TRUE'
            sequence_name = re.sub(r'.*>','',line)
            sequence_name = re.sub(r'\.\.\..*','',sequence_name)
            cluster_list.append([sequence_name,cluster_number,representative])
    cluster_formated_writer.writerows(cluster_list)
df = pd.read_csv(input_file+'.cd.clstr.tsv',sep='\t')
count_clusters = df.pivot_table(index=['Cluster'], aggfunc='size')
df_count_cluster = count_clusters.to_frame()
df_count_cluster = df_count_cluster.reset_index()
df_count_cluster.columns = ['Cluster','Copies']
df2 = pd.merge(df.drop('Copies',1), df_count_cluster, on=['Cluster'])
df2.to_csv(input_file+'.cd.clstr.tsv',index=False,sep='\t')
