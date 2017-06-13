---
title: "Python course, assignment 2: Python scripts"
author: "Jakob Willforss"
output: "pdf_document"
---

# Script 1: Generate random sequences

Short and sweet script. No need for higher structuring in
this case. The use of `random.choice` rather than random
index in the range provided slightly cleaner code.

## Code

```
#!/usr/bin/env python3

import random

dna_len = int(input("Length: "))
allowed_nts = ['A', 'C', 'G', 'T']
seq = ''

for _ in range(dna_len):
    nt = random.choice(allowed_nts)
    seq += nt

print('>random_seq_{}nts'.format(dna_len))
print(seq)
```

## Testrun

```
python3 randomdna.py
Length: 45
# >random_seq_45nts
# GGTACCCGTCCTAATACGGTACCGGGCTCGCCTGTAGGGTGCTCG
```

# Reading FASTQ files

Header is expected to be present on every fourth line. These IDs
are extracted and appended to a list. Finally, resulting count and
exact IDs are shown.

## Code

```
#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print('Error, wrong number of input arguments. Found {}, expected 1'
            .format(len(sys.argv)-1))
    print('Run program as follows: python3 read_fastq.py target.fq')
    sys.exit(1)

in_fq = sys.argv[1]
headers = list()

with open(in_fq) as in_fh:
    line_nbr = 1
    for line in in_fh:
        line = line.rstrip()
        if line_nbr % 4 == 1:
            headers.append(line[1:])
        line_nbr += 1

print(len(headers))
for header in headers:
    print(header)
```

## Testrun

```
python3 read_fastq.py SP1.fq
# 250
# cluster_2:UMI_ATTCCG
# cluster_8:UMI_CTTTGA
# cluster_12:UMI_GGTCAA
# cluster_21:UMI_AGAACA
# cluster_29:UMI_GCAGGA
# cluster_34:UMI_AGCTCA
# cluster_36:UMI_AACAGA
# cluster_37:UMI_GAGGAG
# cluster_39:UMI_GAACCG
# ... continues to 250 ids
```

# Translate DNA

Code was broken down into conceptually distinct units, where
functions represent conceptual steps in the processing algorithm.

I decided against using a class entry for representing the entries
due to the limited scope of the script, but would definitely implemented it
if the script would have grown further. This was the reason for the somewhat clunky
tuple representation of FASTA IDs and their sequences. The reason this was chosen
over a dictionary was that I wanted to retain the original ordering of the file
in the output.

The following function declarations were used:

* main - High-level point executing major steps in algorithm
* read_fasta_to_list - Input step reading and processing input into preferred format
* get_all_peptides - High-level function executing translate_dna_from_pos on all reading frames in order to get collection of all present peptides
* rev_comp - Simple function to retrieve reverse complement of strand of DNA
* translate_dna_from_pos - Translate all codons starting in desired frame
* contains_unknown_nt - Util function to check whether codons are unknown

## Testrun

### one.fa

```
>one_codon
K
```

### two.fa

```
>one_codon
K
>one_stop_codon
S
```

### an_exon.fa

```
>where_is_the_exon
FIQGMVYIKDSQIKLCRRRKKTDFGGSIFQRQATGTCSPGLSLWLLMNPMGREGSCP
QSRVETERSASLEQECHPVFPLPSHLGPTAGEPGVYGLAGPCHVGQAGQQGAIASLP
PPAPPQAWGSPLYLPAFKGCHSWTRKNRREQGGNWTTLETWRGRKKTEEGPQGKGTT
AFTQRVWGAGQVGEGSRQPEAWVQGCTSPNIKPPSFTQVPQEVPDSPRAGPQLAPIH
TSGKTANF
```

### translationtest.dna

```
>single_stop_codon
L
>stopcodons
SLLSLLSLLSLLSLLSLLSLLSLLSLL
>ambiguities  This is a comment, just here to remind you that Fasta sequences have description strings.
XXXXXXXXXXXXXXXXXX
>proteinalphabet This silly DNA string should translate to 'ARNDCQEGHILKMFPSTWYV'
ARNDCQEGHILKMFPSTWYV
>proteinalphabet2
ARNDCQEGHILKMFPSTWYV
>proteinalphabet3
ARNDCQEGHILKMFPSTWYV
>tooshort  No open reading frame here!

>short   The longest reading frame is two codons, "NS" or "TV"
LLL
```

## Code

```
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

```



























