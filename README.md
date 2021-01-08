# Lab Stuff

This repository contains general scripts to automatize routine tasks of my work at WallauLab. For some scripts, I added test files in the directory /test_files

## Usage
- To format LTR_finder output:
> python LTR_finder_to_csv.py -in <LTR_output_file>

- To assembly mitogenomes using a reference-guided approach with MITObim.
> bash mito.sh <reference_genome> <fastq1> <fastq2> <adapter_path/adapter_file> <trimmomatic_path/trimmomatic_jar> </home/user/mira_path/> <num_threads>

> example line: bash mito.sh ref_genome1.fasta sracode_1.fastq sracode_2.fastq Trimmomatic-0.36/adapters/adapter_file.fa ~/softwares/Trimmomatic-0.36/trimmomatic-0.36.jar /home/user/softwares/mira_4.0.2/ 8

- To automatize auto_mito.sh
> bash auto_mito.sh <genomes_fastq_adapters.lst> <path/trimmomatic> <path/mira> <num_threads>

> example line: bash auto_mito.sh genomes_fastq_adapters.lst ~/softwares/Trimmomatic-0.36/trimmomatic-0.36.jar /home/user/softwares/mira_4.0.2/ 8

- To download fastq files from a file with a number or SRA codes
> bash sra.sh <sra_file_list.txt>
## Disclaimer
- I'm not a computer engineer or some related profession, I'm just write this script to study python and to automatize some bioinformatics tasks. So fell free to commit changes that makes the code more efficient or more clean.
- This repository will be constantly updated