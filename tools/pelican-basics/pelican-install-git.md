title: Installing Pelican and Git on lubuntu
date: 2016-02-16
authors: Denis Kramer
tags: Infrastructure, Productivity, Outreach
slug: install-pelican-git

This post provides a step-by-step guide to manually install Pelican on [the bare VirtualBox lubuntu image](http://gamma.kk.soton.ac.uk/feeg6003/virtualbox-images/feeg6003lubuntu.ova). You probably want to install it on your own machine as well for any serious work. In most cases, this should be easier than for lubuntu. The key is to make sure you have Python 2.x and the python package manager **pip** available. Then it should be as simple as running

	pip install pelican markdown
	
as root or super-user. 

We also use Mercurial as version control software. Please refer to the [Mercurial webpage](http://mercurial.selenic.com) for downloads and installation instructions for your machine. On most Linux systems, it is usually best to trust the package manager and use something like

	sudo apt-get install mercurial
	

# Obtain virtual machine

Install VirtualBox on your system (if you have not done so before), download the [lubuntu image](http://gamma.kk.soton.ac.uk/feeg6003/virtualbox-images/feeg6003lubuntu.ova), and add to VirtualBox. Refer to [the VirtualBox post]({filename}/virtualbox-basics/virtualbox-basics.rst) for further guidance on how to setup VirtualBox.

## Install make gcc

Make is needed for the guest installations. We also use make with pelican for convenience (more on that later)

	:::bash
	sudo apt-get install make gcc
	
![Installing gcc]({filename}/pelican-basics/images/install_gcc.png "Installing gcc and make")

Install Guest additions by injecting the *Host Additions CD* and run the following command in the cd subdirectory

	:::bash
	cd /media/feeg6003/<NAME OF VBOXADDITIONS CD>
	sudo ./VBoxLinuxAdditions.run
	
![Installing guest additions]({filename}/pelican-basics/images/install_vbox.png "Installing guest additions")

This should take a minute or two. Reboot the virtual machine after installation of the guest additions.

# Installing Pelican

**Hint:** Make sure that you are **not** using python 3.

![Python version]({filename}/pelican-basics/images/python_version.png "Checking the python version")

We need to manually install the python package manager on lubuntu as this is not bundled with python prior to version 2.7.9. First obtain the installer script using wget

	wget https://bootstrap.pypa.io/get-pip.py

and then install the package manager (pip) as super-user

	sudo python get-pip.py

![Install pip]({filename}/pelican-basics/images/install_pip.png "Installing the python package manager")

Finally, once pip is available, pelican (with markdown extension) can be installed

	sudo pip install pelican markdown
	
![Install pip]({filename}/pelican-basics/images/install_pelican.png "Installing the python package manager")

# Installing Mercurial

We use [Mercurial](http://mercurial.selenic.com) as version control software for the blocks post repository.

Use the linux package manager to install mercurial

	 sudo apt-get install mercurial meld

