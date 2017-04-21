title: Introduction to LaTeX using LyX
authors: Jack Saywell, Juraj Mihalik
date: 2017-03-16
tags: Lyx, Latex, document creation

![LyX]( {filename}/latex-with-lyx/lyx.png "LyX")

# Introduction

This workshop serves as an introduction to LaTeX, using the graphical user interface LyX. We explain the advantages of using LyX, and provide an exercise with the aim of producing a basic template of a scientific report.

Our motivation is to allow people to quickly gain familiarity with LaTeX.

LaTeX is the way to write academic literature in the sciences. This means it’s essential to learn at some point. Previous workshops have introduced the topic in a theoretical and rigorous way, which doesn’t lend itself to people who want to quickly gain familiarity, and so for this reason we are adopting a slightly different approach.

It is often remarked that LaTeX is the antithesis to the mantra WYSIWYG (What You See Is What You Get), and this is very true. LaTeX is essentially code (a .tek file), which is compiled to form a document (e.g. pdf). The beauty of LaTeX comes from its customisability and how it can represent completely general mathematical equations in a beautiful and consistent way.

We are going to introduce LyX, a piece of software which is based on the philosophy WYSIWYM (What You See Is What You Mean) and is more akin to a word processing suite e.g. MS Word than writing bare LaTeX. However, it encourages a structured approach to document creation and allows combination of flexibility of LaTeX with the ease of a word processor. Its main advantage is that you see how the document appears in a clear way as you write it, and don't need to repeatedly re-compile into a pdf. This makes the document writing process more fluid.

Why LaTeX?

* Equations
* Figures
* Consistent formatting
* Cross referencing
* Bibliography

Why LyX?

* Open source GUI
* Cross-platform
* Multiple online resources
* Ease of formatting
* Version control
* Spellchecker
* Export to LaTeX

# Installation

## VirtualBox
A virtual machine image is provided that has the required packages preinstalled, as well as the workshop content. This is the recommended install as it's the quickest and easiest to get up and running.

## On Your Own machine
The packages and workshop content can be easily installed on your own machine if that is preferred to running from a virtual machine.

### Full Install
The easiest way to install all the required packages on your own machine is to install install the packages as follows:

* Anaconda: Download Anaconda [here](https://www.continuum.io/downloads) and install it.

* Git: If not already installed, either download git and install it from [here](https://git-scm.com/) or install it using a package manager.

* TensorFlow: Install TensorFlow for Python by using pip, "pip install tensorflow".

* Graphviz: Install Graphviz for Python by using pip, "pip install graphviz".

Anaconda, git, Tensorflow, and Graphviz

### Minimal Install
## Document structure


## Bibliography
If you have a small number of references you can use LaTeX's bibliography environment as follows:

```tex
\begin{thebibliography}{99}

\bibitem{ref1} Person A, Person A's Paper,
Journal A (Date A).

\bibitem{ref2} Person B,
Person B's Book, Publisher B (Date B).

\end{thebibliography}
```

Items are added using the '\bibitem{label}' command. You can use the '\cite{}' command in text to refer to particular entries in the bibliography.

For instructions on how to use BibTeX for referencing, we refer to the excellent previous workshop by Gabriele Boschetto and Alejandra Vergara, which can be found [here](https://computationalmodelling.bitbucket.io/tools/Bibtex.html).

# References and useful links
* [LyX](https://www.lyx.org/)
* [Introduction to LaTeX and BibTeX](https://computationalmodelling.bitbucket.io/tools/Bibtex.html)
* [Introduction to LaTeX](https://computationalmodelling.bitbucket.io/tools/introduction-to-latex.html)
* [Latex Wiki](http://en.wikibooks.org/wiki/LaTeX)
* [The Not So Short Introduction to Latex](https://tobi.oetiker.ch/lshort/lshort.pdf)

# Exercise

Try to recreate the following pdf as close as you can, you can use either LyX or, if you are more comfortable, LaTeX to do this. Feel free to be creative, there's no need to laboriously recreate the exercise pdf exactly, as long as you can demonstrate the main features.

* Exercise: [pdf]({filename}/latex-with-lyx/Exercise_latex.pdf)
* Cheat sheet: [pdf]({filename}/latex-with-lyx/cheat_sheet_2.pdf)

The aim here is to both show that LyX is far quicker to reproduce the basic document structure needed for scientific reports and also allow people to gain familiarity with LaTeX.

* Solutions in LyX: [lyx]({filename}/latex-with-lyx/Exercise_lyx.lyx)
* Solutions in LaTeK: [tex]({filename}/latex-with-lyx/Exercise_latex.tex)
* .bib file for bibliography: [bib]({filename}/latex-with-lyx/Exercise_bibliography.bib)
* Image for exercise: [png]({filename}/latex-with-lyx/file_extensions.png)
