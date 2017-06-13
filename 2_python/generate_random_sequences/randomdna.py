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
