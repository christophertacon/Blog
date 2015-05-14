Introducing C++
###############

:date: 2015-05-14 16:00
:tags: Productivity, Efficiency, Outreach
:category: Programming-languages
:authors: Jan Kamenik, Shriram Sunder, Stephen Gow
:slug: cpp



------------------------------------------------

.. figure:: {filename}/C++/C++_logo.jpg
   :width: 15%
   :alt: The C++ programming language
   :align: center

This entry accompanies a presentation for the module 'Advanced Computational Methods Part II'; it can also be viewed as a stand-alone exercise for those not present at the workshop. The material presented here consists of tutorials and exercises designed to introduce the programming language C++.

These exercises are designed for use on the virtual machine provided for this tutorial. To download this machine image, `click here`_. The presentation slides associated with this tutorial can be found on `Github`_.

.. _click here: http://www.southampton.ac.uk/~ngcmbits/virtualmachines/feeg6003lubuntu_C++.ova
.. _Github: https://github.com/jankamenik/Cplusplus-presentation/blob/master/presentation.pdf

Prerequisites
=============

The virtual machine contains the text editor Sublime Text 3. For all of these exercises and examples, code should be written and run in this editor. When you are ready to run the code you have written, simply press Ctrl-B and the program will compile using the in-built C++ build system.

Pre-written source files providing examples of some of the concepts discussed can be found in the 'C++' folder located on the desktop. A small number of these examples run using the newer C++11 system; in order to build these examples, you will need to select Tools>Build>C++11 from the Sublime Text 3 toolbar.

In order to make your code run correctly, include these lines at the top of each new program:

.. code-block:: cpp

	#include<iostream>
	using namespace std;

Tutorial 1: object-oriented programming
=======================================

The slides provide an introduction to creating new classes and objects in C++. Let's apply these ideas to a more interesting problem. Suppose we wish to create a database of footballers (a standard task for a fantasy football league, for instance). Attributes such as name, club, games played, goals scored and goal assists will be common to all players. Goals conceded and number of clean sheets are relevant only to defenders and goalkeepers; the number of saves made applies to goalkeepers and no other players. Object orientation in general, and inheritance in particular, provides us with the tools needed to do this.

Step 1: create the classes
--------------------------

We need a general "Footballer" class:

.. code-block:: cpp

	class Footballer
	{
  		protected:
  			string name, club;
  			int games, goals_scored, assists;

  		public:
  			void setValues (string nm, string cb, int gms, int gls, int asts) {name = nm; club = cb; games = gms; goals_scored = gls; assists = asts;}
    		string getName() {return name;}
    		string getClub() {return club;}
    		int getGames() {return games;}
    		int getGoalsScored() {return goals_scored;}
    		int getAssists() {return assists;}
	};

(Optional exercise: rewrite this to use a constructor methods instead of the setValues routine.)

"Defender" should be a subclass of "Footballer", inheriting all of its parent class's attributes and adding its own:

.. code-block:: cpp

	class Defender: public Footballer
	{
		protected:
			int clean_sheets, goals_conceded;

		public:
			void set_Values (string nm, string cb, int gms, int gls, int asts, int clnshts, in glscon) {name = nm; club = cb; games = gms; goals_scored = gls; assists = asts; clean_sheets = clnshts; goals_conceded = glscon;}
			int getCleanSheets() {return clean_sheets;}
    		int getGoalsConceded() {return goals_conceded;}
	};

Notice how we have to call the 'set_Values' function in the subclass by a different name to the 'setValues' function in the parent class. If they had the same name, the function call would be ambiguous and could call the parent class's function instead of the subclass's function. This could be avoided using virtual functions, which are discussed later.

* Exercise: create a "Goalkeeper" subclass, inheriting the "Footballer" class with additional integer variables for clean sheets, goals conceded and saves.

Now we can easily create players and input their statistics:

.. code-block:: cpp

	Footballer PeterCrouch ; PeterCrouch.setValues("Peter Crouch", "Stoke City", 31, 7, 3) ;
	Defender GarethMcAuley ; GarethMcAuley.setValues("Gareth McAuley", "West Bromwich Albion", 22, 0, 0, 11, 27) ;

Try this for your Goalkeeper class as well. 

Tutorial 2: Operator overloading
================================

The slides introduce the concept of overloading functions and operators.

* Exercise: rewrite your "Defender" and "Goalkeeper" code from tutorial 1 to overload the 'setValues' function in the subclasses using virtual functions.

In the example in the slides, we overloaded the * operator to extend its functionality to include matrix multiplication. Let's see how this works in practice. First, we need to create a matrix class:

.. code-block:: cpp

	class matrix
	{
    	public:
        	int a[3][3];

        	matrix() { // default constructor
            	for(int i=0;i<3;i++) {
                	for(int j=0;j<3;j++) {
                    	a[i][j]=0;
                	}
            	}
        	}

        	void set(){// to set matrix elements 
            	for(int i=0;i<3;i++) {
                	for(int j=0;j<3;j++) {
                    	cout<<"\n Enter "<<i<<","<<j<<" element=";
                    	cin>>a[i][j];
                	}
                	cout<<"\n";
            	}
        	}

        	void show() { // to show matrix elements
            	cout<<"\n Matrix is=\n";
            	for(int i=0;i<3;i++) {
                	for(int j=0;j<3;j++) {
                    	cout<<a[i][j]<<",";
                	}
                	cout<<"\n";
            	}
        	}

Don't worry too much about how this code works - the principles are more important the specifics. Now we need to include our new matrix multiplication operator (still inside the public methods of the class):

.. code-block:: cpp

		matrix operator*(matrix x)// overloading * for multiplication
        	{
            	matrix c;// this will hold our result
            	for(int i=0;i<3;i++)
            	{
                	for(int j=0;j<3;j++)
                	{
                    	c.a[i][j]=0;
                    	for(int k=0;k<3;k++)
                    	{
                        	c.a[i][j]=c.a[i][j]+a[i][k]*x.a[k][j];        
                    	}
                	}
            	}
            	return(c);

        	}
	};

Now we can see how the operator works. Try generating two matrices (note that you will have to enter each entry of the matrix separately), and multiply them together:

.. code-block:: cpp

	matrix a,b,c;
    a.set();
    b.set();

    c = a * b;
    a.show();
    b.show();
    c.show();

Additional resources
====================

* `A useful tutorial`_ on the use of C++.

.. _A useful tutorial: http://www.tutorialspoint.com/cplusplus/
