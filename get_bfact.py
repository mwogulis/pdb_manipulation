from Bio import PDB
import numpy as np

def get_structure(file):
    parser = PDB.PDBParser(QUIET=True)
    return parser.get_structure('', file)

def get_ca_atoms(structure):
    b_factors = []
    for model in structure:
        for chain in model:
            for residue in chain:
                try:
                    b_factors.append(residue['CA'].get_bfactor())
                except KeyError:
                    continue
    return b_factors



def main(file):
    structure1 = get_structure(file)
    ca_b_factors = get_ca_atoms(structure1, positions)
    return ca_b_factors
    

bfs=main('yta7_AF.pdb')
print(bfs)
