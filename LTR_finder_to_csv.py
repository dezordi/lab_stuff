#!/usr/bin/python3
# -*- coding: utf-8 -*-
###############################>GENERAL-INFORMATIONS<###############################
"""
Build in Python 3.6
Authors:
Filipe Dezordi
zimmer.filipe@gmail.com
https://github.com/dezordi
Yago Dias
yag.dias@gmail.com
08 Jan. 2021
"""
####inserir input, argumentos
import argparse, csv, re
parser = argparse.ArgumentParser(description = "This script convert the LTR-Finder output to a CSV file")
parser.add_argument("-in", "--input", help="LTR-Finder output", required=True)
args = parser.parse_args()
input_file = args.input


####cria o arquivo de output e o cabeçaho cabeçalho
csv_output = open(input_file+'.csv','w')
csv_output_writer = csv.writer(csv_output,delimiter=',')
csv_output_writer.writerow(["Sequence","Location","Element Length","Strand","LTR-similarity","5'LTR_pos","5'LTR_length","3'LTR_pos","3'LTR_length","TSR","Sharpness","PPT"])

####o arquivo é lido linha por linha
with open(input_file,'r') as ltr_finder_output:
  ####toda montagem da tabela é feita por listas, armazenando os valores e depois transformando em tabela
  list_lists = []
  sequence = ''
  location = ''
  length = ''
  strand = ''
  ltr_similarity = ''
  ltr5_pos = ''
  ltr5_len = ''
  ltr3_pos = ''
  ltr3_len = ''
  tsr = ''
  sharpness = ''
  ppt = ''
  for line in ltr_finder_output:
    if '>'in line:
      sequence = re.sub(r'>Sequence: ','',line)
      sequence = re.sub(r'\sLen:.*','',sequence).rstrip('\n')
    if 'No LTR Retrotransposons Found' in line:
      location = 'na'
      length = 'na'
      ltr_similarity = 'na'
      ltr5_pos = 'na'
      ltr5_len = 'na'
      ltr3_pos = 'na'
      ltr3_len = 'na'
      tsr = 'na'
      sharpness = 'na'
      strand = 'na'
      ppt = 'na'
      list_lists.append([sequence,location,length,strand,ltr_similarity,ltr5_pos,ltr5_len,ltr3_pos,ltr3_len,tsr,sharpness,ppt])
    else:
      if 'Location' in line:
        location = re.sub(r'\sLen:.*','',line).rstrip('\n')
        location = re.sub(r'Location\s:\s','',location)
        location = re.sub(r'\s-\s',':',location)
        length = re.sub(r'.*\sLen:','',line).rstrip('\n')
        length = re.sub(r'\sStrand:.*','',length)
        strand = re.sub(r'.*\sStrand:','',line).rstrip('\n')
      if 'Score' in line:
        ltr_similarity = re.sub(r'.*:','',line).rstrip('\n')
        ltr_similarity = re.sub(']','',ltr_similarity)
      if "5'-LTR " in line:
        ltr5_pos = re.sub(r'\sLen:.*','',line).rstrip('\n')
        ltr5_pos = re.sub(r'.*:\s','',ltr5_pos)
        ltr5_pos = re.sub(r'\s-\s',':',ltr5_pos)
        ltr5_len = re.sub(r'.*Len:\s','',line) .rstrip('\n')
      if "3'-LTR " in line:
        ltr3_pos = re.sub(r'\sLen:.*','',line).rstrip('\n')
        ltr3_pos = re.sub(r'.*:\s','',ltr3_pos)
        ltr3_pos = re.sub(r'\s-\s',':',ltr3_pos)
        ltr3_len = re.sub(r'.*Len:\s','',line) .rstrip('\n')
      if "TSR" in line:
        tsr = re.sub(r'.*:\s','',line).rstrip('\n')
        tsr = re.sub(r'\[.*\]','',tsr)
        tsr = re.sub(r'\s,\s','/',tsr)
        tsr = re.sub(r'\s-\s',':',tsr)
        tsr = re.sub(r'\s','',tsr)
      if "Sharpness" in line:
        sharpness = re.sub(r'.*:\s','',line).rstrip('\n')
        sharpness = re.sub(',','/',sharpness)
      if "PPT " in line:
        ppt = re.sub(r'.*\]\s','',line).rstrip('\n')
        ppt = re.sub(r'\s-\s',':',ppt)
        list_lists.append([sequence,location,length,strand,ltr_similarity,ltr5_pos,ltr5_len,ltr3_pos,ltr3_len,tsr,sharpness,ppt]) 
csv_output_writer.writerows(list_lists)