title: Virtualization with Docker
date: 2016-03-10
authors: Ignacio Vidal
tags: Virtual Machines, Linux

<p align="center"><img src="{filename}/revealJS/reveal.png" align="right" style="margin: 2em 5em 2em 2em"/></p> 

## Introduction

[Virtual Machines](https://en.wikipedia.org/wiki/Virtual_machine) have been extensively used 

## Docker vs. Virtual Machines

## Images, containers and registry

#### Software (Own Machine)

## Let's begin!

It's time to grab a terminal and start playing with docker. Install the software on debian based linux distributions should be as easy as typing `apt-get install docker.io`

### Docker commands

Interfacing the docker engine is done via commands, issued as `docker <command>`, where `<command>` can be:

- `run`: runs a container from an image.
- `images`: list available images within the host system.
- `ps`: list containers.
- `exec`: runs a command in a running container .
- `kill`,`stop`,`start`,`restart`: kills, stops, starts or restarts a container.
- ...

Executing `docker` without arguments will print a detailed list of available commands. `docker <command> --help` will print help.

### Hello World

We will now print a *dockerized* hello world. The command to execute is:

    docker run ubuntu /bin/echo "hello world"
    
wich means: *Hey, docker! Grab the ubuntu image from the registry if it doesn't exits yet, create a ubuntu environment, run a container executing `/bin/echo "hello world"` and exit!*

That was a lot of work to simply print a string on the screen.

### Interactive bash session

The same way we ran `/bin/echo`, we can run `/bin/bash`, so...

    docker run ubuntu /bin/bash
    
Oh... it didn't worked. Why? Because we have to tell docker to allocate a pseudo TTY (option `-t`) and to attach the standard input to the container (option `-i`). Now

    docker run ubuntu -t -i /bin/bash
    
greets us with a root terminal in a dockerized ubuntu. But remember! We are only running `bash`! Not the whole Ubuntu! That's precisely the whole point of docker: being able to run applications in a isolated and controlled environment without running the whole environment itself!  
  
In this bash session we can run whatever command we like (including `apt-get`, of course) and access the network. You may install new software, but changes won't be permanent.

If we open another terminal window on the host machine and execute `docker ps`, we will see our `bash` container running with an associated container ID (some hexadecimal number like `f0ef61c5fc04` and a human-friendly random name (`reverent_lumiere`, by example).

We can stop the container (`docker stop reverent_lumiere`, which will kick you out of the terminal), start it again were it was left (`docker start reverent_lumiere`) and reattach to the terminal with `docker attach reverent_lumiere`.

### Daemonizing containers

Most of the useful applications in linux are not interactive. Web servers, databases and services alike run in background (daemons). If we want a container to be daemonized we simply add the `-d` switch to the docker client: `docker run -d ubuntu command`.

### Creating Docker images

You may want to create a custom docker image. Maybe you are working in a team and you are using a specific version of `python` and a custom tuned `numpy` library. A great way to ensure that everyone uses the same environment is building and shipping a docker image.

There are two ways of creating an image:

#### Incremental changes

Changes to an image done with a bash interactive session will not be persistent *unless* you commit them.

#### Using a DOCKERFILE

Running a bash session and commiting the changes may be inconvinient to manage images and deploy to a large team. Luckily we can automate the process and specify creation commands in a bash-style script: the DOCKERFILE.



#### Virtual Machine

If you want to reproduce the steps in this short tutorial, you can download a bare minimum Debian Jessie virtual machine [here](https://dummy.ac.uk). You will only be presented with a bash console (no X) and a limited set of commands. Docker.io is pre-installed, so you can inmediatly start playing around. User: Password: 

#### Useful links

- [Docker Engine user guide](https://docs.docker.com/engine/userguide/intro/)
- [Docker Hub](https://docs.docker.com/linux/)
- [An introduction to Docker for reproducible research. By Carl Boettige](http://www.carlboettiger.info/assets/files/pubs/10.1145/2723872.2723882.pdf)
- [Contain This, Unleashing Docker for HPC. By Douglas M. Jacobsen and Richard Shane Canon](https://www.nersc.gov/assets/Uploads/cug2015udi.pdf)
- 

#### Files

Summary of files contained within:

- README.md: github README file to display markdown on page
- feeg6003_reveal_HTML.html: HTML version of the presentation
- feeg6003_reveal_MD.html: Markdown version of the presentation
- feeg6003_template_adv.html: A template with full reveal options
- feeg6003_template_basic.html: A template with cre reveal options
- img/: folder for images
- plotfile.js: File containing the JavaScript for the embedded plot
- reveal.js/: Folder containg the reveal.js files
- tutorial.pdf: Guide for the workshop lab
- tutorial_material/: Material for the lab
- uos-logo.css: CSS file to include the university logo in the corner of the presentation

<p/>
## Using Reveal.js Presentations

You can view a Reveal.js presentation in any JavaScript enabled browser.

#### Using generic software

Open the presentation/HTML file in your preferred text editor. Open the presentation/HTML file with your browser. When you make edits to the file, you then must refresh the presentation page in the broswer 

#### Using Brackets

Open the presentation/HTML file you wish to edit in Brackets. Click the lightning bolt icon in the upper right corner, this should open a browser window and the lighning bolt should turn from grey to yellow. As you save your presentation, the changes will be reflected in the browser dynamically.

#### Controlling the presentation

If you wish to make the presentation full screen, then press the **F** key, or leave the window reduced if you want to just test the presentation. With the browser in focus, the presentation can be controlled using the arrow keys or spacebar.

## Tutorial

For the tutorial page click [here]({filename}/revealJS/tutorial.html), if you would like it in PDF format click [here]({filename}/revealJS/tutorial.pdf). For the tutorial files click [here]({filename}/revealJS/feeg6003_revealjs.zip)

### Internal notes

"sudo docker run --dns=152.78.3.34 -ti ubuntu:14.04 /bin/bash" <- This is the command line that we have to run! We have to specify the DNS directly because the UoS internal network.
