##################################################
# Dockerfile to build the feeg6003/scicomp image #
# Based on Ubuntu 14:04                          #
##################################################

# Set the base image to Ubuntu
FROM ubuntu:14.04
# File Author
MAINTAINER Ignacio Vidal

# Update the repository
RUN apt-get update

# Install build-essential
RUN apt-get install -y build-essential

# Install parallel computing libraries
RUN apt-get install -y libopenmpi-dev openmpi-bin libgomp1

# Install python
RUN apt-get install -y python2.7

# Install numpy, scipy, matplotlib and GSL
RUN apt-get install -y libgsl0-dev python2.7-numpy python-matplotlib

#Install miscellaneous tools
RUN apt-get install -y gnuplot git nano

ENTRYPOINT /bin/bash
