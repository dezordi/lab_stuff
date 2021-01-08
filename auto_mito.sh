#!/bin/bash
#Written by: Filipe Dezordi (https://dezordi.github.io/)
#At FioCruz/IAM - 29 Nov. 2020

#Esse script automatiza o mito.sh, evitando repetir várias linhas de análise quando trabalhamos com vários genomas

#os argumentos são passados conforme a ordem de chamada da linha de comando:
#bash auto_mito.sh genomes_fastq_adapters.lst ~/softwares/Trimmomatic-0.36/trimmomatic-0.36.jar /home/alexandre/softwares/mira_4.0.2/ 8

#Inserindo argumentos em variáveis:

files=$1 #a list file with <genome>:<fastq1>:<fastq2>:<adapters>
TRIMMO=$2 #trimmomatic program file
MIRA=$3 #mirapath
THREADS=$4 #threads

while read linha;do #para cada linha do arquivo
	genome=$(echo $linha | awk -F":" '{print $1}') #awk -F ":" quebra a linha em colunas, pelo separador ":", a coluna $1 é o nome do arquivo de genoma
	fastq1=$(echo $linha | awk -F":" '{print $2}') #a coluna $2 fastq foward
	fastq2=$(echo $linha | awk -F":" '{print $3}') #a coluna $3 fastq reverse
	adapters=$(echo $linha | awk -F":" '{print $4}') #a coluna 4 caminho e arquivo de adaptadores
	bash mito.sh $genome $fastq1 $fastq2 $adapters $TRIMMO $MIRA $THREADS #roda o mito.sh com as 4 variáveis criadas, o trimmomatic, o mira e o número de threads
done < $files #o laço será feito no arquivo files