#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Filipe Z. Dezordi"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Filipe Z. Dezordi"
__email__ = "zimmer.filipe@gmail.com"
__date__ = "2021/16/08"
__username__ = "dezordi"

import argparse, csv, re
parser = argparse.ArgumentParser(description = 'This script format a brute txt file with DNAsp v5.1 output to ta tsv tabular file')
parser.add_argument("-in","--input_file",help="DNAsp file", required=True)
args = parser.parse_args()
input_file = args.input_file

#creating output file
outputfilewriter = open(input_file+'.tsv',"w")

#creating output header
csv_output = csv.writer(outputfilewriter,delimiter='\t')
csv_output.writerow(["Filename","Population","Number of sequences","Number of segregating sites, S","Number of haplotypes, h","Haplotype diversity, Hd","Average number of differences, K","Nucleotide diversity, Pi","Nucleotide diversity with JC, PiJC","Theta (per sequence) from S, Theta-W","Theta (per site) from S, Theta-W","Tajima's D","Tajima's D Statistical significance","Fu and Li's D* test statistic"," Fu and Li's D* Statistical significance","Fu and Li's F* test statistic","Fu and Li's F* Statistical significance","Fu's Fs statistic","Strobeck's S statistic"," Probability that [NHap = 3]"])

#creating variables
filename = ''
population = ''
number_sequences = ''
number_segregating_sites = ''
num_haplotypes = ''
haplotybe_diversity = ''
avg_differences_number = ''
nucleotide_diversity_pi = ''
nucleotide_diversity_pijc = ''
theta_from_s = ''
theta_w_from_s = ''
tajima = ''
tajima_statistic = ''
fu_and_li_d = ''
fu_and_li_d_statistic = ''
fu_and_li_f = ''
fu_and_li_f_statistic = ''
fu_fs_statistic = ''
strobeck_statistic = ''
nhap = ''


with open(input_file,'r') as inputfilereader:
    #for each line into output file, search and keep values of each metric
    for line in inputfilereader:
        if "Input Data File" in line:
            filename = re.sub(r'.*\\','',line).rstrip('\n')
        if "Population" in line:
            population = re.sub(r'.*: ','',line).rstrip('\n')
        if "Total Data" in line:
            population = filename+'_total'
            nucleotide_diversity_pijc = 'NA'
        if 'Number of sequences' in line:
            number_sequences = int(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Number of segregating sites' in line:
            number_segregating_sites = int(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Number of haplotypes' in line:
             num_haplotypes = int(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Haplotype diversity' in line:
            haplotybe_diversity = float(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Average number of' in line:
            avg_differences_number = float(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Nucleotide diversity, Pi' in line:
            nucleotide_diversity_pi = float(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Nucleotide diversity with JC' in line:
            nucleotide_diversity_pijc = float(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Theta (per sequence) from' in line:
            theta_from_s = float(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Theta (per site) from' in line:
            theta_w_from_s = float(re.sub(r'.*: ','',line).rstrip('\n'))
        if "Tajima's D" in line:
            tajima = float(re.sub(r'.*: ','',line).rstrip('\n'))
            tajima_statistic = str(re.sub(r'.*: ','',next(inputfilereader)).rstrip('\n'))
        if "Fu and Li's D" in line:
            fu_and_li_d = float(re.sub(r'.*: ','',line).rstrip('\n'))
            fu_and_li_d_statistic = str(re.sub(r'.*: ','',next(inputfilereader)).rstrip('\n'))
        if "Fu and Li's F" in line:
            fu_and_li_f = float(re.sub(r'.*: ','',line).rstrip('\n'))
            fu_and_li_f_statistic = str(re.sub(r'.*: ','',next(inputfilereader)).rstrip('\n'))
        if "Fu's Fs statistic" in line:
            fu_fs_statistic = float(re.sub(r'.*: ','',line).rstrip('\n'))
        if "Strobeck's S" in line:
            strobeck_statistic = float(re.sub(r'.*: ','',line).rstrip('\n'))
        if 'Probability that [NHap =' in line:
            nhap = str(re.sub(r'.*that ','',line).rstrip('\n'))
        if all(value != '' for value in [filename,population,number_sequences,number_segregating_sites,num_haplotypes,haplotybe_diversity,avg_differences_number,nucleotide_diversity_pi,nucleotide_diversity_pijc,theta_from_s,theta_w_from_s,tajima,tajima_statistic,fu_and_li_d,fu_and_li_d_statistic,fu_and_li_f,fu_and_li_f_statistic,fu_fs_statistic,strobeck_statistic,nhap]):        
            csv_output.writerow([filename,population,number_sequences,number_segregating_sites,num_haplotypes,haplotybe_diversity,avg_differences_number,nucleotide_diversity_pi,nucleotide_diversity_pijc,theta_from_s,theta_w_from_s,tajima,tajima_statistic,fu_and_li_d,fu_and_li_d_statistic,fu_and_li_f,fu_and_li_f_statistic,fu_fs_statistic,strobeck_statistic,nhap])
            population = number_sequences = number_segregating_sites = num_haplotypes = haplotybe_diversity = avg_differences_number = nucleotide_diversity_pi = nucleotide_diversity_pijc = theta_from_s = theta_w_from_s = tajima = tajima_statistic = fu_and_li_d = fu_and_li_d_statistic = fu_and_li_f = fu_and_li_f_statistic = fu_fs_statistic = strobeck_statistic = nhap = ''