---
title: "Python course: Evaluating MUSCLE as command line software"
author: "Jakob Willforss, 5th June 2017"
output: pdf_document
geometry: margin=3cm
---

# Introduction

MUSCLE is a popular alignment software developed by Robert Edgar. It is used to perform
multiple alignments and is claimed to have better accuracy and speed than other leading
tools in the field, such as CLUSTALW.

# The command line interface

MUSCLE runs nicely from the command line, and is downloaded as a single binary. Here, I evaluate
it point-by-point following the outline provided in the article *Ten recommendations for creating
usable bioinformatics command line software*.

## Print something if no parameters are supplied

When running `muscle` without parameters an informative output providing version number,
web page, article to cite, basic usage instructions and commonly used flags are provided
(see below).

```
> muscle
# MUSCLE v3.8.31 by Robert C. Edgar
#
# http://www.drive5.com/muscle
# This software is donated to the public domain.
# Please cite: Edgar, R.C. Nucleic Acids Res 32(5), 1792-97.
#
# Basic usage
#
#    muscle -in <inputfile> -out <outputfile>
#
#    Common options (for a complete list please see the User Guide):
#
#    -in <inputfile>    Input file in FASTA format (default stdin)
#    -out <outputfile>  Output alignment in FASTA format (default stdout)
#    ... more flags
```


The information is clear, concise and quickly provides a great insight into its interface.
This output is exemplary.

## Always have a "-h" or "-help" switch

There is no help flag available for `muscle`. This is partly remedied by the clear default output
(which also is printed when attempting to use invalid flags, such as `-h`), but would still be
preferable if its more extensive documentation was available through the command line. Now,
the interested user has to navigate to the web page to find the full 'User Guide'.

## Have a "-v" or "-version" switch

The version number can be obtained by using the flag `-version`. This provides the version number together with descriptive text of the software:

```
> muscle -version
MUSCLE v3.8.31 by Robert C. Edgar
```

This information is also provided in the default output for the software. The short form of the flag `-v` is not available.

The needed information is available, but could have been further improved by allowing the commonly tried shortform `-v`, as well as only printing the version number when using the flag ('3.8.31') to ease the processing when used in pipelines.

## Do not use stdout for messages and errors

`muscle` provides plenty of output information when processing. This is directed to STDERR. Furthermore,
even though it allows specifying the input and output files using the `-in` and `-out` flags, it does by default read input from STDIN and write its output to STDOUT. This allows it to easily be integrated in UNIX pipelines.

## Always raise an error if something goes wrong

When purposefully failing `muscle` by providing a directory as input, it both provided a clear and descriptive error message, as well as specifying a non-zero exit code. `muscle` seems to behave similar to the preference of the article at this point.

```
> muscle -in my_directory
# *** ERROR ***  No sequences in input file
> echo $?
# 2
```

## Validate your parameters

Overall, `muscle` provides some feedback when providing illogical input before stopping the processing. I tried supplying it with numbers and files in wrong formats, and it overall handled it well.

```
> muscle -in 2
# *** ERROR ***  Cannot open '2' errno=2  
```

I decided to push it a bit further, and supplied an alphabetic argument using the `-maxiters` flag which clearly asks for a numeric number of iterations. In this case, `muscle` initially happily started processing. Then, it froze, and the RAM usage spiked until the full 32GB RAM of the computer was in use, threatening to crash analyses simultaneously running on the computer, and in worst cases forcing a reboot. Fortunately, the kill command finally got through after a few tense minutes and `muscle` stopped in its tracks.

Verdict: It seems to me like `muscle` have an overall solid validation of the more common inputs, but could benefit from further basic checking of arguments to its flags.

```
muscle -in yeast_genes/10.fasta -maxiters a
# 10 32 seqs, max length 716, avg  length 548
# 00:00:00    10 MB(-1%)  Iter   1  100.00%  K-mer dist pass 1
# 00:00:00    10 MB(-1%)  Iter   1  100.00%  K-mer dist pass 2
# 00:00:01    24 MB(-2%)  Iter   1  100.00%  Align node       
# 00:00:01    24 MB(-2%)  Iter   1  100.00%  Root alignment
# 00:00:01    24 MB(-2%)  Iter   2  100.00%  Refine tree   
# 00:00:01    24 MB(-2%)  Iter   2  100.00%  Root alignment
# 00:00:01    24 MB(-2%)  Iter   2  100.00%  Root alignment
# Killed
```

## Remaining points

The final points *Don't hard-code any paths*, *Don't pollute the PATH*, *Check that your dependencies are installed* and *Don't distribute bare JAR files* are all less applicable to `muscle` as it is distributed as a single-unit binary with no direct dependencies. It isn't using any other files, omitting the need for managing paths to for example config files. It is not written in Java, so the JAR-point is not applicable. Also, as no installation procedure is performed, the only risk for namespace pollution is if you yourself add the `muscle` binary to the PATH.

# Conclusion

Overall, `muscle` appears to have a well throught through interface, which also very likely have been iterated upon after receiving feedback from its extensive user base. It is also well designed for usage in processing pipelines due to its handling of standard input and output. Still, it isn't strictly adhering to the expected UNIX interface style having its own design for its flags.

It might be a one-off, but it also seems like it would benefit from a bit more thorough testing of its input flags.
