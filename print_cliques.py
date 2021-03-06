import argparse
from term_grouping import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path',type=str,default=None,help='Path to hamiltonian')
    args = parser.parse_args()
    return args

def print_cliques(f):
    #for f in filelist:
    print('--------------')
    print(f)
    H = parseHamiltonian(f)

    # For some qubit encodings, there isn't a single term acting on all qubits
    # so this will report the wrong qubit#
    # Instead, look for the largest index being operated on.
    ops = [term[1] for term in H]
    #Nq = max([len(op) for op in ops])
    Nq = max([int(op[-1][1:]) for op in ops]) + 1
    print('{} qubits'.format(Nq))
    print('{} total terms\n'.format(len(H)))
    for commutativity_type, type_str in zip([QWCCommutativity, FullCommutativity],['QWC','FULL']):
        print(type_str + 'Commutation:')
        cliques = genMeasureCircuit(H, Nq, commutativity_type)
        print()


def main():

    #Hfiles = ['hamiltonians/H2O_6-31g_{}_104_AS6.txt'.format(e) for e in ['JW','BK','BKSF','BKT','PC']]
    args = parse_args()
    print_cliques(args.path)


if __name__ == '__main__':
    main()
