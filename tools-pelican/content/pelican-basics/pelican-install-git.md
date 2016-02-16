title: Installing Pelican and Git on lubuntu
date: 2016-02-16
authors: Denis Kramer
tags: Infrastructure, Productivity, Outreach
slug: install-pelican-git

This post provides a step-by-step guide to manually install Pelican on [the bare VirtualBox lubuntu image](http://gamma.kk.soton.ac.uk/feeg6003/virtualbox-images/feeg6003lubuntu-2016.ova). You probably want to install it on your own machine as well for any serious work. In most cases, this should be easier than for lubuntu. The key is to make sure you have Python 2.x and the python package manager **pip** available. Then it should be as simple as running

	pip install pelican markdown
	
as root or super-user. 

We also use Git as version control software. Please refer to the [Git webpage](https://git-scm.com) for downloads and installation instructions for your machine. On most Linux systems, it is usually best to trust the package manager and use something like

	sudo apt-get install git
	

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

On lubuntu 15.10, pip can be installed via apt-get
	
	:::bash
	sudo apt-get install python-pip

If this fails, you probably have an older operating system. You can find instructions to install pip manually on the blog explaining ![installation of pelican with mercurial]({filename}/pelican-basics/pelican-install.md).

Finally, once pip is available, pelican (with markdown extension) can be installed

	sudo pip install pelican markdown
	
![Install pip]({filename}/pelican-basics/images/install_pelican.png "Installing the python package manager")

# Installing Git

We use [Git](https://git-scm.com) as version control software for the blocks post repository.

Use the linux package manager to install git and meld

	 sudo apt-get install git meld

![Meld](http://meldmerge.org) is a visual diff and merge tool that is useful.
