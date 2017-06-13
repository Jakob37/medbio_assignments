#!/usr/bin/env python3

import sys


AA_DICT = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    	   "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
    	   "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
    	   "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",
    	   "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    	   "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    	   "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    	   "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    	   "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    	   "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    	   "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    	   "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    	   "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    	   "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    	   "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    	   "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}


def main():
    
    if len(sys.argv) != 2:
        print('Expected 1 argument, found {}'.format(len(sys.argv)-1))
        sys.exit(1)

    fasta_fp = sys.argv[1]
    fasta_list = read_fasta_to_list(fasta_fp)

    for i in range(len(fasta_list)):
        entry = fasta_list[i]
        all_peps = get_all_peptides(entry[1])
        longest_pep = sorted(all_peps, key=lambda x: len(x), reverse=True)[0]
        print('{}\n{}'.format(entry[0], longest_pep))
   

def read_fasta_to_list(fasta_fp):
    
    """
    Parse FASTA into list of tuples (ID, seq)
    Handles both single- and multi-line FASTA files
    """

    fasta_list = list()

    header = None
    entry_seq = ''
    with open(fasta_fp) as in_fh:
        for line in in_fh:
            line = line.rstrip()
            if line.startswith('>'):
                if header is not None:
                    fasta_list.append((header, entry_seq))
                header = line
                entry_seq = ''
            else:
                entry_seq += line.upper()
        fasta_list.append((header, entry_seq))
    return fasta_list


def get_all_peptides(dna_seq):

    """
    Retrieve all peptides for all open reading frames
    for particular DNA sequence
    """

    dna_seq_rvc = rev_comp(dna_seq)
    translations = list()

    for frame in range(3):
        fw = translate_dna_from_pos(dna_seq, frame)
        rv = translate_dna_from_pos(dna_seq_rvc, frame)
        translations += fw.split('*')
        translations += rv.split('*')

    return translations


def rev_comp(dna):

    """Generate reverse complement for provided DNA string"""
    
    trans_dict = {'A': 'T',
                  'C': 'G',
                  'G': 'C',
                  'T': 'A'}

    trans_dna = ''
    for nt in dna:
        if nt in trans_dict:
            new_nt = trans_dict[nt]
        else:
            new_nt = 'N'
        trans_dna += new_nt

    return trans_dna[::-1]


def translate_dna_from_pos(dna, start_i):

    """Translate dna sequence to amino acids, starting from given index"""

    prot_seq = ''

    for pos in range(start_i, len(dna), 3):
        triple = dna[pos:pos+3]
        if len(triple) == 3:
            if AA_DICT.get(triple) is None:
                aa = 'X'
            else:
                aa = AA_DICT[triple]
            prot_seq += aa
    return prot_seq


if __name__ == '__main__':
    main()

