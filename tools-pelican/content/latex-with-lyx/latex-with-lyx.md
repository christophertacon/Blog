title: Introduction to LaTeX using LyX
authors: Jack Saywell, Juraj Mihalik
date: 2017-03-16
tags: Lyx, Latex, document creation

![LyX]( {filename}/latex-with-lyx/lyx.png "LyX")

#Introduction

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

# LyX

To get LyX, simply download from their website or use the virtual machine provided.

* [LyX](https://www.lyx.org/)

Both LyX and LaTeX require a TeX distribution is installed on your machine. Popular options include TeXLive or MiKTeX:

* [TeXLive](https://www.tug.org/texlive/)
* [MiKTeX](https://miktex.org/)

The beauty of LyX lies in its ease of use. Instead of writing LaTeX commands to insert tables/titles/sections/etc, one simply selects from drop down menus. LyX also has a user-friendly equation editor.

After you've played around with LyX and written a document, you can view the resulting pdf by clicking on the 'eyes' icon in the toolbar. If you make further changes to your document, clicking the 'cyclic arrows' icon button just to the right of the 'eyes' icon updates the pdf with any changes.

The best way to discover the features of LyX is by experimentation, and for those in search of a more complete tutorial more details can be found [here](http://wiki.lyx.org/LyX/Tutorials).

# LaTeX

We now present a brief introduction on how to construct a document using LaTeX. For a more thorough introduction to LaTeX, we refer to an excellent previous workshop which can be found [here](https://computationalmodelling.bitbucket.io/tools/introduction-to-latex.html).

To get started with LaTex you will need a text editor/IDE (eg. Emacs, Sublime or TeXMaker) and a PDF viewer (eg. Evince, Adobe) in addition to a TeX distribution.

##Document structure

Begin by using a preferred text editor, or LaTeX IDE. A LaTeX document is formed around commands:

```tex
\command[option]{argument}
```

The document should begin by defining the document class. Different classes have different purposes and properties. The most common for scientific documents will be the article class. Note the options provided to the command.

```tex
\documentclass[a4paper,12pt]{article}
```

Packages can be added to extend basic functionality,

```tex
\usepackage[opt1, opt2, ...]{package_name}
```
Two useful such packages are *amsmath* and *graphicx*, which allow for inclusion of a wide range of mathematical expressions and the importing of figures, respectively.

The body of the document must be contained between the following:

```tex
\begin{document}

\end{document}
```

##Creating a title
To specify the title, author and date, use the following commands at the beginning of the document:

```tex
\begin{document}
\title{Proof of Fermat’s Last Theorem}
\author{Andrew Wiles}
\date{December 1994}
\maketitle
\end{document}
```

##Sections
Just like LyX we have sections and subsections. Unlike LyX, we define them using commands. For example,

```tex
\section{Calculus}
\subsection{Differentiation}
\section*{Integration}        (this will be unnumbered)
\section{Calculus}\label{sec:Calculus}
```

We can then refer to the *'Calculus'* section by using the following command within text:

```tex
\ref{sec:Calculus}
```

##Equations and Figures
At the most basic level, equations can be included inline or separately to allow for numbering. To include inline simply include the following within text:

```tex
$equation$
```
The alternative is to use the equation environment:

```tex
\begin{equation}
  y = x_0 + \frac{1}{\displaystyle x_1
          + \frac{1}{\displaystyle x_2
          + \frac{1}{\displaystyle x_3 + x_4}}} \nonumber
\end{equation}
```

To include figures, the basic code structure is:
```tex
\begin{figure}
\centering
  \includegraphics[scale=0.8]{image.png}
  \caption{A caption.}
  \label{fig:image}
\end{figure}
```
Note that we have centered the image and added a suitable caption and label, which can be referred to within the text.

##Bibliography
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

#References and useful links
* [LyX](https://www.lyx.org/)
* [Introduction to LaTeX and BibTeX](https://computationalmodelling.bitbucket.io/tools/Bibtex.html)
* [Introduction to LaTeX](https://computationalmodelling.bitbucket.io/tools/introduction-to-latex.html)
* [Latex Wiki](http://en.wikibooks.org/wiki/LaTeX)
* [The Not So Short Introduction to Latex](https://tobi.oetiker.ch/lshort/lshort.pdf)

#Exercise

Try to recreate the following pdf as close as you can, you can use either LyX or, if you are more comfortable, LaTeX to do this. Feel free to be creative, there's no need to laboriously recreate the exercise pdf exactly, as long as you can demonstrate the main features.

* Exercise: [pdf]({filename}/latex-with-lyx/Exercise_latex.pdf)
* Cheat sheet: [pdf]({filename}/latex-with-lyx/cheat_sheet_2.pdf)

The aim here is to both show that LyX is far quicker to reproduce the basic document structure needed for scientific reports and also allow people to gain familiarity with LaTeX.

* Solutions in LyX: [lyx]({filename}/latex-with-lyx/Exercise_lyx.lyx)
* Solutions in LaTeK: [tex]({filename}/latex-with-lyx/Exercise_latex.tex)
* .bib file for bibliography: [bib]({filename}/latex-with-lyx/Exercise_bibliography.bib)
* Image for exercise: [png]({filename}/latex-with-lyx/file_extensions.png)
