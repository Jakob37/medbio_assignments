#!/usr/bin/env python3

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
