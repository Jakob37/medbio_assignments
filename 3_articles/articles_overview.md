# Synthesis of benefit for me

* Consider making fully reproducible preprocessing of data
  * If files not there - Regenerate, otherwise use as they are
  * What software to use? Simply Python?
* Attempt further link documentation and automation
* When using graphical software, use screen shots to record settings, and put those in markdown document
* Make basic tools (like command line aliases) easy to integrate in different environments
  * Put them to use
  * Make sure to have clear Git organizational structure SO THAT I KNOW WHERE TO LOOK FOR THE STUFF. THINK ABOUT THIS ONE!!!

# Splitting points

* Version control
* Degree of rigorousness
* Degree of focus on solving biological question
* Unit test
* Whether to push out software in open early
* Complete reproducibility
* Degree of organization

# A Quick Guide to Organizing Computational Biology Projects

Discussing how clear project organization helps navigating in project
and helps promoting reproducible research.

Emphasis on clarity.

## Key points

* Someone unfamiliar with your work should be able to look at files and get idea of what you did.
* You will need to repeat stuff, so you will be the one needing to reuse stuff.
* Clear directory structure is ground pillar.
* The lab notebook
  * Need to keep track of analysis, AND CONCLUSIONS
* Carrying out a single experiment
  * Record every operation
  * Comment and annotate generously
  * *Avoid editing intermediate files by hand* - This is reproducibility killer
  * Use relative pathnames to access files in project
  * Make script restartable - "if files doesn't exist - regenerate"

# Ten Simple Rules for the Open Development of Scientific Software

More emphasis on getting software out in the open, and sharing
it with other people.

## Key points

* Don't reinvent the wheel
* Code well
* Be your own user
* Be transparent
* Be simple
* Don't be a perfectionist
* Nurture and grow your community
* Promote your project
* Find sponsors
* Science counts
  * Risk with that scientific software has no motivation for maintenance
  * Open source communities can ensure persistence of project

# Best Practices for Scientific Computing

Slightly more computational take. Discussing risks of developing
your own software.

## Key points

* Write program for people, not computers
* Let the computer do the work
* Make incremental changes
* Don't repeat yourself (or others)
* Plan for mistakes
* Optimize software only after it works
* Document design and purpose, not mechanics
* Collaborate

# So you want to be a computational biologist?

Slightly different emphasis here. Software is tools used to perform
the research, not an end in itself. OK to tab slightly on quality
for the sake of research (carefully worded).

Slightly hippy 'you can do it!' approach, rather than more heavy
and rigorous 'it needs a lot of work to get it right'.

Not much discussion on risks with own developed software.

## Key points

* Understand your goals and choose appropriate methods
  * Important to have understanding of algorithms underlying software
* Set traps for your scripts
  * Create test datasets
* You're a scientist, not a programmer
  * Quality of research more important than look of code
* Use version control software
* Pipelineitis is nasty disease
  * Avoid becoming locked in into procedure by built pipeline
* An Obama frame of mind
  * It is possible to learn, even for a biologist
* Be suspicios and trust noone
  * P-hacking is a thing
* The right tool for the job
  * UNIX is powerful tool, use it
* Be a detective
  * Much time will go to poking around into data
* Someone has done it - find them
  * Ask online
  * Join local meetings

# Ten Simple Rules for Reproducible Computational Research

Focusing on making it possible to reproduce the entire analysis.
Provides minimum guidelines, as well as more in-depth recommended
practices.

## Key points

* Every created result should be possible to trace
  * Risk of manual noting is that it can get out of sync
  * Documentation used for analysis more solid way
* Avoid manual data manipulation steps
  * Use scripting rather than copy-paste and manual editing
* Archive versions of used external program
* Version control all custom scripts
* Record all intermediate steps, when possible in standardized formats
* For randomness, note random seeds
* Always store raw data behind plots
* Generate hierarchical analysis output
  * Example: Allow digging into underlying data for plot
* Connect textual statements to underlying results
  * Keep track of interpretations of data
  * Sweave and similar solid alternative
* Provide public access to scripts, runs and results
  * Strong documentation sends signal of quality and trustworthiness
