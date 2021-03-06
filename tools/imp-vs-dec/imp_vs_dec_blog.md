title: Imperative vs. Declarative Programming - Installation Instructions
authors: Gary Downing, Mohammed El Kout, Andres Gutierrez Robledo
date: 2017-03-23
tags: Imperative, Declarative, Python, Assembly, Haskell
slug: imp-vs-dec-install

In this workshop we will attempt to clarify, by way of comparison, the differences between imperative and declarative programming styles. Moreover, how aspects of both styles can be used to improve programming productivity.

To aid with this, we will be presenting a number of exercises. Attempting these exercises requires access to a couple of different programming environments, installation instructions for which can be found below.

# Installation

The exercises in this workshop require [Python](https://www.python.org/) & [Haskell](https://www.haskell.org/) environments and [GNUSim8085](https://gnusim8085.github.io/), an assembler simulator and debugger.

## The VM Image (Recommended)

[Download the virtual machine image with the required applications pre-installed](http://www.southampton.ac.uk/~gmd1n15/LubuntuJupyterHaskellGNUSim.ova) (or [here](http://www.southampton.ac.uk/~ngcmbits/virtualmachines/LubuntuJupyterHaskellGNUSim.ova) if the first link isn't available). Then import the `.ova` image in VirtualBox (instructions for how to this can be found in an earlier [VirtualBox workshop blog post](https://computationalmodelling.bitbucket.io/tools/virtualbox-basics.html)).

To check everything is working correctly;

* Start the VM, login and password are the same.
* Open a terminal (shortcut on the desktop) and call `$ jupyter notebook`. This should open a Firefox with the Jupyter notebook working. Check you can create `New` Python 3 and Haskell notebooks.
* Try to run GNUSim8085 (shortcut on the desktop).

#
## Teaching Materials

The VM contains all the teaching materials for this workshop. They can also be downloaded separately [here]({filename}/imp-vs-dec/imp-vs-dec-teaching-materials.zip).

## Alternative Install Methods

![Python]( {filename}/imp-vs-dec/python.png "Python")
### Python 3

For the Python exercises, we recommend the [Jupyter Notebook](https://ipython.org/notebook.html):

* *Option 1*: You can [try Jupyter Notebook in your browser](https://try.jupyter.org/).
* *Option 2*: Install Jupyter Notebook with [these instructions](https://jupyter.org/install.html)
* *Option 3*: Most Linux and Mac OS installations come with Python pre-installed. Simply execute `$ python` in the command line (N.b. that these pre-installed versions are normally an older version and do not provide an editor, just a command line parser).

![Haskell]( {filename}/imp-vs-dec/haskell.png "Haskell")
### Haskell

In the Haskell exercises, we will be again using Jupyter Notebook, but this time with the [IHaskell kernel](https://github.com/gibiansky/IHaskell):

* *Option 1*: [Try the IHaskell kernel in your browser](https://try.jupyter.org/) (This webpage is somewhat unreliable, so don't expect it to work every time).
* *Option 2*: If using Linux (Mac instructions will be similar), follow these steps to install the IHaskell kernel (more information can be on the [IHaskell homepage](https://github.com/gibiansky/IHaskell));

    * Install GHC (Glasgow Haskell Compiler): `$ sudo apt-get install ghc`
    * Install git, haskell-stack (to build IHaskell with), and build dependencies: `$ sudo apt-get install git haskell-stack pkg-config libz-dev libzmq3-dev ncurses-dev`
    * Clone the IHaskell repo: `$ git clone https://github.com/gibiansky/IHaskell.git`
    * Build and install IHaskell;
    ```
    cd IHaskell;
    stack setup;
    stack install
    ```
    * Make sure IHaskell can be found (might need terminal restart): `$ ihaskell -V`. If not, you need a symbolic link to `ihaskell` executable in current `$PATH` or add it to `$PATH` itself (this should be automatic in ubuntu).
    * (Optional) cleanup: `$ sudo apt-get remove --purge libz-dev haskell-stack git pkg-config ncurses-dev`
    * Finally, install the kernel `$ ihaskell install`

* *Option 3*: You can use the GHC compiler from the command line. Just install GHC as in *Option 2*, then execute `$ ghci`. This will give you a command line interface similar to the Python one.

![GNUSim8085]( {filename}/imp-vs-dec/gnusim.png "GNUSim8085")
### GNUSim8085

The Assembler exercises will use GNUSim8085:

  * *Option 1*: On Debian and it's derivatives, this program is available via the package manager: `apt-get install gunsim8085`
  * *Option 2*: Binaries for other platforms and source code can be found on the [GNUSim8085 homepage](https://gnusim8085.github.io/).
