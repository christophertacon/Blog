Fortran programming languadge
#############################

:date: 2015-04-30 16:00
:tags: f2pye,outreach, FORTRAN
:category: Programming-languages
:authors: Ioannis Begleris, Hao Wang
:slug: FORTRAN

.. figure:: {filename}/FORTRAN/FORTRAN.jpg
   :width: 25%
   :alt: Programmer's first Reference Manual for Fortran
   :align: center

FORTRAN (or FORmula TRANslator) can be considered the first widely used programming language. With the first compiler released in 1957, FORTRAN has been around and still going for almost 60 years with the next release expected in 2015. The purpose for this session is to firstly present the basic principles needed to read and write FORTRAN codes in scientific computing, and secondly introduce the Fortran to Python interface (f2py) that allows the creation of Python modules from FORTRAN.

Detailed slides of the workshop can be found at: `presentation slides.pdf`_

Further reading about f2py and a FORTRAN manual can be found in the resources section.

Practical Session
=================


In order to run through this session either download the `Lubuntu_ova_fortran`_ virtualbox image and load it to your virtual-box or simply run these commands (if you haven’t already) on your Debian operating system:

.. code-block:: bash

	$ sudo apt-get update
	$ sudo apt-get install python ipython gfortran python-dev python-numpy gedit



When compiling and running use:

.. code-block:: bash

	$ gfortran program.f90 -o program
	$ ./program

Exercise 1: Writing your first FORTRAN program
===============================================

Write a FORTRAN program "*Fibonacci*" that dynamically calculates a given number (N) of the Fibonacci numbers and stores them in a real vector of size N. The program should then write the elements of the array in a dat file using the default format. You can use the Python code provided as guidance.


.. code-block:: python
	
	for i in range(N):
		if i==0:
			A[i]=0.
		elif i==1:
			A[i]=1.
		else:
			A[i]=A[i-1]+A[i-2] 


Note: In order to declare the array variable, N needs to be defined before declaration. One way to do this is to introduce it as a constant before the array is declared. Example:



	integer, parameter :: N=9



When running ignore the floating point errors that arise for high N. 
Note you are advised to use the lecture slides as reference.
The solution can be found in: `Exercise1.f90`_


Exercise 2: Converting to a subprogram
======================================
Convert your previous code to a program that:

.. Bullet lists:

* Initialised the number N and an array of size N
* Calls the subroutine "*fib*" while Passing in the array and the number of elements N 
* The subroutine should then do the calculation previously done in exercise 1
* The main program then prints them to a file as done in exercise 1

Solutions are found in: `Exercise2.f90`_


Exercise 3: Making a python module
==================================
Take your subroutine and place it in a new file, fibonacci_sub.f90, without the main program and make sure it compiles without errors using:

.. code-block:: bash

	$ gfortran -Wall -c fibonacci_sub.f90


Then compile the FORTRAN to python interface command:

.. code-block:: bash

	$ f2py -c fibonacci_sub.f90 -m fibonacci

A file containing the subroutine can be found: `fibonacci_sub.f90`_

If no errors are visible then make shure that your module is correct by using the python program:

.. code-block:: python

	import numpy as np
	import fibpnacci_sub
	a =np.zeros(10)
	fibpnacci_sub.fib(a)
	print a

You can copy and paste the above python program in a terminal that is running python or Ipython.

Even though the subroutine taken in two variable in FORTRAN the beauty of f2py is that it it is clever enough to know that, allowing you to enter only the array itself. 

Note: If you are finding errors from calling the module its maybe because you are sending an array with 64-bit floating point precision elements to a module that only understands 32-bit. This is the difference between REAL and DOUBLE PRECISION declarations.


Resources
=========

`FORTRAN Manual`_
`f2py`_


.. _FORTRAN Manual: http://www-eio.upc.edu/lceio/manuals/Fortran95-manual.pdf
.. _f2py: https://sysbio.ioc.ee/projects/f2py2e/
.. _Exercise1.f90: {filename}/FORTRAN/Solution1.f90
.. _Exercise2.f90: {filename}/FORTRAN/solution2.f90
.. _fibonacci_sub.f90: {filename}/FORTRAN/subroutine.f90

.. _Lubuntu_ova_fortran: http://www.southampton.ac.uk/~ngcmbits/virtualmachines/feeg6003lubuntu_fortran.ova
.. _presentation slides.pdf: {filename}/FORTRAN/FORTAN_beamer.pdf
