title: Installing Pelican on lubuntu
date: 2015-02-12
authors: Denis Kramer
tags: Infrastructure, Productivity, Outreach
slug: install-pelican

## Obtain virtual machine

Install VirtualBox on your system (if you have not done so before), download the [lubuntu image](http://gamma.kk.soton.ac.uk/feeg6003/virtualbox-images/feeg6003lubuntu.ova), and add to VirtualBox. Refer to [the VirtualBox post]({filename}/virtualbox-basics/virtualbox-basics.rst) for further guidance on how to setup VirtualBox.

### Install make gcc

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

## Installing Pelican

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

## Installing Mercurial

We use [Mercurial](http://mercurial.selenic.com) as version control software for the blocks post repository.

Use the linux package manager to install mercurial

	 sudo apt-get install mercurial meld

