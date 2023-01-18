import csv
import sys
from Bio import SeqIO

input_fasta = sys.argv[1]
tsv_file = sys.argv[2]

# Ler arquivo fasta e armazenar as sequencias em uma lista
sequences = list(SeqIO.parse(input_fasta, "fasta"))

# Ler arquivo tsv e armazenar os nomes antigos e novos em um dicionário
name_map = {}
with open(tsv_file) as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for row in tsvreader:
        name_map[row[0]] = row[1]

# Substituir o nome da sequencia pelo novo nome usando o dicionario
for seq in sequences:
    seq.id = name_map.get(seq.id, seq.id)
    seq.name = name_map.get(seq.name, seq.name)
    seq.description = name_map.get(seq.description, seq.description)

# Salvar as sequencias modificadas no arquivo fasta
SeqIO.write(sequences, f"{input_fasta}.renamed.fa", "fasta")