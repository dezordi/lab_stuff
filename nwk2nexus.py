import argparse
from Bio import Phylo

def convert_newick_to_nexus(input_file: str, output_file: str) -> None:
    tree = Phylo.read(input_file, "newick")
    Phylo.write(tree, output_file, "nexus")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a phylogenetic tree from Newick to Nexus format.")
    parser.add_argument("-in", "--input", help="The path to the input file in Newick format.", required=True)
    parser.add_argument("-o", "--output", help="The path to the output file in Nexus format.", required=True)
    args = parser.parse_args()

    convert_newick_to_nexus(args.input, args.output)
