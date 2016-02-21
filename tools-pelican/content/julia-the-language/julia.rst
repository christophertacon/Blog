Julia: The Language
###################

:date: 2015-05-07 16:00
:tags: Productivity, Efficiency, Outreach
:category: Languages
:authors: Josh Greenhalgh, Jonothan Waters
:slug: Julia

.. figure:: {filename}/julia-the-language/julia-images/julia.png
   :width: 15%
   :alt: Julia: The Language
   :align: center

Introduction
============

Julia is a newish programming language designed to provide high-level and high performance technical computing. It has a syntax that should be familiar to users of Matlab and Python. The languge is rapidly evolving and has a signigicantly increasing popultion of contributors. Julia is based around a LLVM (low level virtual machine) JIT (just-in-time) complier which allows for high performance at usually around 2-3x C speed and in some cases vitually equal to C speed. Unlike the usual strategy of vectorising code to increase speed, as found in python, Julia works extreamly rapidly when just using standard for loops. The main developers of the Julia language are based at MIT and have written an in depth description of the design philosophy of the language which can be found `here`_.

.. _here: http://arxiv.org/pdf/1411.1607v3.pdf

Installation
============

For this workshop a virtual machine has been set up with Julia allready installed - the image can be found at this `link`_. However if you wish to install Julia on your own machine their are various routes available. The easiest possible route is to follow the instructions, for your operating system, found on the `Julia website`_. It may be necassary to add the Julia executable to your path in order to run the REPL from the terminal. If you would like to live on the bleeding edge of Julia development then you can install from source by following the instructions on the `Julia Github`_ - be aware that when following this method you will have to wait a very very long time (expect upto 3 hours!!) and there will probably be various errors because of dependencies that you lack (`cmake`_ and `m4`_ were needed when installing on mac). 

Julia can be used via the REPL or by running scripts, however an excellent working enviroment is provided by the IJulia kernal for the Jupyter (formally IPython) notebook. In order to install IJulia you will first need a version of Python, version 2.7 is recomended, along with IPython and the IPython notebook. IPython and the notebook can be installed using pip;

.. _link: https://www.dropbox.com/s/n0fkh7p5p534t6x/Julia.ova?dl=0
.. _Julia website: http://julialang.org/downloads/platform.html
.. _Julia Github: https://github.com/JuliaLang/julia
.. _m4: https://www.gnu.org/software/m4/
.. _cmake: http://www.cmake.org/install/

.. code-block:: bash

	$ pip install 'ipython[notebook]'

Once the Python dependencies have been installed you will need to open up a Julia REPL and use the following command;

.. code-block:: julia

	julia> Pkg.add("IJulia")

The IJulia package will then be installed and should be available in Jupyter by running the following in the terminal;

.. code-block:: bash

	$ ipython notebook

A new browser window should appear in which the local file structure will be displayed, selecting new in the top right corner and then picking the julia kernal from the dropdown menu should start a new notebook file. 

Workshop Content
================

The Basics
----------

`DL Notebook-The-Basics.ipynb`_ (right click and save as..)

`View Notebook-The-Basics.ipynb`_


.. _DL Notebook-The-Basics.ipynb: {filename}/julia-the-language/julia-files/The-Basics.ipynb
.. _View Notebook-The-Basics.ipynb: http://nbviewer.ipython.org/url/raw.githubusercontent.com/josh-gree/juliafiles/master/The-Basics.ipynb

Julia types
-----------

`DL Notebook-Julia-Types.ipynb`_ (right click and save as..)

`View Notebook-Julia-Types.ipynb`_


.. _DL Notebook-Julia-Types.ipynb: {filename}/julia-the-language/julia-files/Julia-Types.ipynb
.. _View Notebook-Julia-Types.ipynb: http://nbviewer.ipython.org/url/raw.githubusercontent.com/josh-gree/juliafiles/master/Julia-Types.ipynb


Parallelism in Julia
--------------------

`DL Notebook-Parallel.ipynb`_ (right click and save as..)

`View Notebook-Parallel.ipynb`_

.. _DL Notebook-Parallel.ipynb: {filename}/julia-the-language/julia-files/Parallel.ipynb
.. _View Notebook-Parallel.ipynb: http://nbviewer.ipython.org/url/raw.githubusercontent.com/josh-gree/juliafiles/master/Parallel.ipynb

More to learn....
=================

Some links to find out more about julia;

`Tutorial`_

.. _Tutorial : https://www.youtube.com/watch?v=vWkgEddb4-A

`Plotting`_ 

.. _Plotting : http://en.wikibooks.org/wiki/Introducing_Julia/Plotting

`Package Listing`_

.. _Package Listing: http://pkg.julialang.org/

`Documentation`_

.. _Documentation : http://docs.julialang.org/en/release-0.3/

`Google Group`_

.. _Google Group: https://groups.google.com/forum/#!forum/julia-users
