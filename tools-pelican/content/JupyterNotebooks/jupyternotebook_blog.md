title: Jupyter Notebooks
date: 2017-03-13
authors: James Bailey, Marian Daogaru
tags: Jupyter, Jupyter Notebook, nbdime, nbval, nbconvert, Python, Python3, pytest

## Introduction
<hr>
Jupyter Notebooks are a web based application that enables users to create and share documents containing code, data visualisations, text, etc, in different programming languages. This workshop presents an introduction to Jupyter Notebooks and three packages which extend their functionality:

- **nbconvert**
- **nbdime**
- **nbval**

[**nbconvert**](https://nbconvert.readthedocs.io/en/latest/) allows the user to convert a Jupyter Notebook into different formats, such as PDF, LaTeX and many more. [**nbdime**](https://nbdime.readthedocs.io/en/latest/) is a tool used to see the differences between two notebooks (diffing) or to merge two notebooks. Lastly, [**nbval**](https://github.com/computationalmodelling/nbval) is a plugin for pytest which validates the execution of the Notebook by checking that the output has not changed. 

For this workshop, Python3 will be used. No previous knowledge of Jupyter Notebooks is required, however coding skills are a plus.

## Tutorial
<hr>
### Learning Material and Exercises
All of the material created for this session is contained in Jupyter Notebooks. There is a main notebook which contains all of the learning material and exercises. This will guide you through using Jupyter Notebooks and the three packages listed above, ending with the exercises to practise what you have learnt.

### Supporting Material
A number of notebooks have been created to demonstrate the functionality of the three packages covered and will be referenced in the learning material.

### Download
You can download all of this material from [here]({filename}/JupyterNotebooks/Learning_Material.zip) and starting working through it.


## Pre-Requisites
### Installation on own machine
For working on your own machine, you will need:

- Python
- Jupyter Notebook
- nbconvert
- nbdime
- nbval (version >= 0.5.0)

#### Python

We would recommend installing Python using Anaconda. This gives you access to Python, a range of standard packages and pip (for installing further Python packages). If you do not want to install the full Anaconda distribution then you can use Miniconda which will install only a few basic packages to get you started.

#### Jupyter Notebook
- **Anaconda** - Jupyter Notebook comes as part of the Anaconda distribution
- **pip** - there is a metapackage called Jupyter which will install all of the necessary Jupyter packages
      pip install jupyter

See [here](http://jupyter.readthedocs.io/en/latest/install.html#new-to-python-and-jupyter) for further information on installing Jupyter.

#### nbconvert

- In command line run:

      pip install nbconvert

#### nbdime

- run the following lines in command line.

      pip install --upgrade nbdime

#### nbval

- **pip** - nbval can be installed through pip:
      pip install nbval


### Virtual Machine
We have also created a virtual machine which contains all of the necessary software and material for the workshop. If you prefer you can use VirtualBox and download the virtual machine labelled feeg6003_jupyternotebook from [here](http://www.soton.ac.uk/~ngcmbits/virtualmachines) to complete the workshop.

### Checking you're ready
The following steps allow you to check that you have Jupyter Notebook installed correctly and have the additional packages we are going to show you.

#### Opening Jupyter Notebook
In a terminal window:

    jupyter notebook

This should open an instance of Jupyter Notebook which usually open automatically in your browser. The Jupyter Notebook instance has the default address `http://localhost:8888/` so by typing this into your browser you should also be able to access a running Jupyter Notebook.

#### nbconvert

If you installed nbconvert using command line, run the following lines to download and run the official tests.

    pip install nbconvert[test]
    py.test --pyargs nbconvert

Most of the tests shoud pass, with some few skipped and several warnings. It can be read by the warning messages that the tests are deprecated, and will be eliminated in the next version.

#### nbdime

If you installed nbdime using command line, run the following lines to download and run the official tests.

    pip install nbdime[test]
    py.test --pyargs nbdime

Most of the tests should pass, with some failing due to some libraries not being installed properly. Ignore this for now, as they do not affect the functionality.

#### nbval

For the functionality included in this workshop we need version 0.5.0 or greater. You can check your current version using:

    pip show nbval

If you have version 0.5.0 or greater then you have what you need.
