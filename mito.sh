#!/bin/bash
#Written by: Filipe Dezordi (https://dezordi.github.io/)
#At FioCruz/IAM - 29 Nov. 2020

##USAGE:
#bash mito.sh <REFERENCEGENOME> <001.fastq.gz> <002.fastq.gz> <PATH/ADAPTERS> <PATH/trimmomatic-0.36.jar> <PATH_mira> <INT:THREADS>


#os argumentos são passados conforme a ordem de chamada da linha de comando:

#Arguments
FASTA=$1 #reference genome
FASTQ1=$2 #foward reads
FASTQ2=$3 #reverse reads
ADAPTER=$4 #adapter path/file from ~/trimmomatic/adapters/file.fa
TRIMMO=$5 #trimmomatic program file from ~/trimmomatic/trimmomatic.jar
MIRA=$6 #mirapath from /home/user/mira
THREADS=$7 #threads

#creating prefix name and directory to store results
PREFIXOUT=$(echo $FASTQ1 | awk -F "_" '{print $1}') #printar o nome do fastq1 separar por "_" e pegar apenas a primeira coluna, ou seja, o código SRR
DIR_NAME=${PREFIXOUT}_${FASTA}
DIR_NAME=${DIR_NAME/.fasta/_results}
REF_name=${FASTA/.fasta/}

mkdir $DIR_NAME
cd $DIR_NAME

#Trimmomatic
java -jar $TRIMMO PE -threads $THREADS ../$FASTQ1 ../$FASTQ2 -baseout $PREFIXOUT ILLUMINACLIP:$ADAPTER:2:30:10:2:keepBothReads LEADING:3 TRAILING:3 MINLEN:36 SLIDINGWINDOW:4:20

#fastqc
fastqc ../$FASTQ1 ../$FASTQ2 $PREFIXOUT"_1P" $PREFIXOUT"_2P" $PREFIXOUT"_1U" $PREFIXOUT"_2U"

cat $PREFIXOUT"_1P" $PREFIXOUT"_2P" $PREFIXOUT"_1U" $PREFIXOUT"_2U" > $PREFIXOUT"_TRIMMED.fastq"

#RUN MITOBIM
MITObim_1.9.1.pl -end 100 -sample $PREFIXOUT -ref $REF_name -readpool $PREFIXOUT"_TRIMMED.fastq" -quick ../$FASTA -clean -mirapath $MIRA &> log
cd ..