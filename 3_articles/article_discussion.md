---
title: "Python course: Article discussion"
author: "Jakob Willforss, 5th June 2017"
output: pdf_document
geometry: margin=3cm
---

# How does the authors agree?

A variety of points were covered in the articles. Several was discussed
by two or more articles, but due to their different emphasis not by all five.
I have here selected some points I found interesting that were discussed by
two or more of the articles.

Loman, N., Sandve, G. and Noble, W. highlights version control as a highly
valuable tool as it both helps facilitate the actual development by providing
a central point and clear location for all versions of the code,
but perhaps more importantly, by ensuring that each used version
of a script always will be available by allowing the script to be
rerun in the exact same state at any later point.

Both Loman, N. and Prlić, A. emphasizes that the actual problem that we
are trying to solve is a biological one. In the end, it is the science that
matters, not how efficiently and elegantly we can perform the analysis.

Noble, W. and Loman, N. discuss that during development of scripts it is
unavoidable for bugs to be introduced. They comment that it is preferable
to stop execution of a program in its track instead of allowing errors to
propagate, potentially silently, throughout the system and the analysis.

Sandve, G., and Noble, W. agrees on the importance of maintaining a lab
notebook clearly showing the steps performed in the analysis. Preferably, the
notebook could be produced using tools that also provide the utilities to
combine code execution and documentation.

# What does each paper contribute relative to the others?

## Ten simple rules for reproducible computational research (Sandve, G.K.)

This article promoted a variety of habits for reproducible research and ways to allow
exact regeneration of your results, both by you and other interested in your
analysis. Examples are allowing regeneration of plots by providing the raw
data behind them, and keeping track of components needed for fully reproducible
analysis such as exact commands used, software versions and randomness seeds.

## A quick guide to organizing computational biology projects (Noble, W.S.)

The primary focus of this article was on how to organize and work with a
project and its analyses as a whole. It provided deeper reflection of
potentially workable folder structures and how you could categorize different
files and scripts used during your analysis.

## Best practices for scientific computing (Wilson, G.)

This article took a more computationally focused approach compared to the
other articles (together with Sandve, G.K.). It provides a variety of concrete
advice on how to approach the actual software development, such as the
Don't Repeat Yourself-principle, and delaying optimization of software
until later in the development.

## So you want to be a computational biologist? (Loman, N.)

The main distinguishing characteristic of this article is how it to a higher degree emphasizes that the actual problem being solved is a biological one, not a computational. It seems to promote a philosophy of laying a minimal groundwork of good computational habits, while never losing the sight of the biological question.

When discussing pipelines, it goes directly contrarily to Wilson, G. by being very hesitant about their usage, saying that overuse could inhibit the scientific curiousity. It also emphasizes
that a computational biologist isn't a programmer, but a biologist.

## Ten simple rules for the open development of scientific software (Prlić, A.)

This paper reflects over potential strengths of providing open
source software. It talks more about the social aspects of development,
such as gaining a user base and marketing the project.

It also reflects over some useful coding habits such as investigating in advance
whether a software solving a particular task is already available before setting
of reinventing another wheel, which lies close to using and contribution
to the open source community. It also encourages you to try striking the right balance between
solid and straight-forward code and never putting your code out there due to perfectionism.
