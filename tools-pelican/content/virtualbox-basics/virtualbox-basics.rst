Introduction to Virtualbox
==========================

:date: 2015-02-05
:tags: Research, Infrastructure, Productivity, Reproducibility, Testing
:slug:
   virtualbox-basics
:authors: Ian Hawke

What follows is the zero motivation and explanation instructions for getting the FEEG6003 base VirtualBox image (an LUbuntu 14.10 OS) up and running.

.. figure:: {filename}/virtualbox-basics/virtualbox-images/virtualbox-logo.png
   :figwidth: 30%
   :width: 100%
   :alt: Virtualbox logo
   :align: left

First `download and install VirtualBox for your operating system <https://www.virtualbox.org/wiki/Downloads>`__.

.. figure:: {filename}/virtualbox-basics/virtualbox-images/VBoxDownload.png
   :figwidth: 60%
   :width: 100%
   :alt: Virtualbox download
   :align: left

Second `download the feeg6003lubuntu image <http://gamma.kk.soton.ac.uk/feeg6003/virtualbox-images/feeg6003lubuntu.ova>`__.

.. figure:: {filename}/virtualbox-basics/virtualbox-images/ImportAppliance1.png
   :figwidth: 60%
   :width: 100%
   :alt: Importing the virtual machine
   :align: left

Then import the virtual machine into VirtualBox.

.. figure:: {filename}/virtualbox-basics/virtualbox-images/ImportAppliance2.png
   :figwidth: 60%
   :width: 100%
   :alt: Importing the virtual machine
   :align: left

To start the machine just press **Start**.

.. figure:: {filename}/virtualbox-basics/virtualbox-images/StartVM.png
   :figwidth: 60%
   :width: 100%
   :alt: Starting the virtual machine
   :align: left

The machine name, username and password are all the same: ``feeg6003``. Enter the password once the login screen appears.

.. figure:: {filename}/virtualbox-basics/virtualbox-images/LUbuntu1.png
   :figwidth: 60%
   :width: 100%
   :alt: Login screen
   :align: left

At this point you have a working virtual machine, but it will be awkward to work with. So we need to make it work better with your hardware by installing the Guest Additions. First we need to install a C compiler (it's a *really* basic VM!). Open a terminal (either from the menu, Accessories, or by pressing ``Ctrl+Alt+T``).

.. figure:: {filename}/virtualbox-basics/virtualbox-images/terminal.png
   :figwidth: 60%
   :width: 100%
   :alt: Open a terminal
   :align: left

Install gcc by typing::

    sudo apt-get install gcc

.. figure:: {filename}/virtualbox-basics/virtualbox-images/gcc.png
   :figwidth: 60%
   :width: 100%
   :alt: Installing gcc
   :align: left

Next, go to the *external* menu (that is, the menu on your "real" machine), and choose Devices, then Insert Guest Additions, ...

.. figure:: {filename}/virtualbox-basics/virtualbox-images/GuestAdditions1.png
   :figwidth: 60%
   :width: 100%
   :alt: Getting Guest Additions going
   :align: left

Now we need to actually install the software. Back in the terminal, change directory to the "CD" by typing something like::

    cd /media/feeg6003/VirtualBox...

You can use the tab key to complete each entry: there should be no ambiguity here. Then install the software by typing::

    sudo sh ./VBoxLinuxAdditions.sh

This should rapidly say it's installed the software.

.. figure:: {filename}/virtualbox-basics/virtualbox-images/GuestAdditions2.png
   :figwidth: 60%
   :width: 100%
   :alt: Installing Guest Additions
   :align: left

Finally, close the terminal, "eject the CD", and reboot the virtual machine. To do this, select logout from the menu, then select reboot. Once the VM restarts, you should have much better screen resolution.

From this base image you can install whatever software you want or need onto the VM. Using the package manager is the simplest way to install software. We did this using ``apt-get`` above, but other tools include the software centre

.. figure:: {filename}/virtualbox-basics/virtualbox-images/software-centre.png
   :figwidth: 60%
   :width: 100%
   :alt: Software centre
   :align: left

or ``synaptic``.

.. figure:: {filename}/virtualbox-basics/virtualbox-images/synaptic.png
   :figwidth: 60%
   :width: 100%
   :alt: synaptic
   :align: left

This base image can now have all the necessary software installed on, for re-distribution ready to demonstrate the tool or area you're focusing on.
