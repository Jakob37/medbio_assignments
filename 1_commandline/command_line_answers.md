---
title: "Python course, assignment 1: Command line"
author: "Jakob Willforss"
output: pdf_document
---

# Exercise 1

Figure out what the following Unix commands do. You should feel familiar with all of these

* cd - Change directory
* ls - List files in directory
* mkdir - Create empty directory
* rm - Remove files
* cat - Output content of one or multiple files (concatenated)
* less - Open and view text files in the viewer `less`
* head - Print the initial part of a file to the STDOUT
* tail - Print the last part of a file to the STDOUT
* wc - Count number of lines, words and/or characters in a file
* grep - Extract parts of files matching given patterns
* sort - Sort provided input
* uniq - Remove adjacent identical lines
* cut - Cut out particular columns from a file

# Exercise 2

Create a directory structure for this course in your home directory using `mkdir` and `cd`. There should be a directory for the course, and within it a directory for each assignment

Directory structure:

```
course_root
    1_commandline
    2_python
    3_articles
    4_modules
    5_databases
    Documents
```

# Exercise 3

* What does `ls -l` do? Long listing, providing information about permissions, file owner, file size and time of use.
* How to delete directory with rm? Need to use `-r` flag for recursive removal.

# Exercise 4

The tab-delimited file `gpcr.tab` was retrieved.

(1) By the look of the header, the file seems to have 7 columns.

(2) The command `wc -l` tells me that it contains 29305 lines.

(3) How many human GPCRs?



```
grep -P -c '.*\t.*_HUMAN' gpcr.tab
# 2244
grep -c "Homo sapiens" gpcr.tab
# 2244
grep "Human" gpcr.tab | grep -v "Homo sapiens" | cut -f6
# Human cytomegalovirus (strain AD169) (HHV-5) (Human herpesvirus 5)
# Human herpesvirus 6A (strain Uganda-1102) (HHV-6 variant A) (Human B lymphotropic virus)
# Human herpesvirus 7 (strain JI) (HHV-7) (Human T lymphotropic virus)
# Human cytomegalovirus (strain AD169) (HHV-5) (Human herpesvirus 5)
# Human cytomegalovirus (strain AD169) (HHV-5) (Human herpesvirus 5)
# Human cytomegalovirus (strain AD169) (HHV-5) (Human herpesvirus 5)
# Human cytomegalovirus (strain Towne) (HHV-5) (Human herpesvirus 5)
# Human herpesvirus 8 (HHV-8) (Kaposi's sarcoma-associated herpesvirus)
# Human herpesvirus 6A (strain Uganda-1102) (HHV-6 variant A) (Human B lymphotropic virus)
# Human herpesvirus 6B (strain Z29) (HHV-6 variant B) (Human B lymphotropic virus)
# Human herpesvirus 7 (strain JI) (HHV-7) (Human T lymphotropic virus)
```

Grepping for only 'human' provided a higher number of hits, as it included hits for viruses
targeting human. To be on the safe side, I would target the UNIPROT ID column showing from
were the entry was retrieved.

(4) How long is the shortest sequence listed in the same file?

```
cut -f7 gpcr.tab | sort -n | head -5
# 10
# 12
# 13
# 14
# 20
```

The shortest is 10 amino acids long. Interestingly, to get the longest,
one need to be careful with using the `-n` flag to get natural sorting.

(5) How many species are named in gpcr.tab?

```
cut -f6 gpcr.tab | sort | uniq | wc -l
# 3493 unique entries
```

These 3493 entries include the header, so 3492 unique species.

# Exercise 5

Download and extract a directory with Fasta files, that contains 88 Fasta files.
Write a shell script that applies a multi alignment software like Muscle or MAFFT
on each gene family in the directory.

* Muscle (v3.8.31) was retrieved from `http://www.drive5.com/muscle/downloads.htm`
* Processing was performed in the `1_commandline` directory.

```
for fa in yeast_genes/*; do
    muscle -in ${fa} -out ${fa#*/}.aligned
done
```


















