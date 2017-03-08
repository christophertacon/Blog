title: Introduction to Emacs
authors: Jamie Caldwell, Nicholas McCaw, Daniel Powell
date: 2017-05-06
tags: Emacs, NGCM, VirtualBox
slug: Emacs

<p align="center"><img src="{filename}/Emacs/emacs_logo.png" align="right" style="margin: 2em 5em 2em 2em"/></p>

#Emacs

Emacs is a customisable, self-documenting and fully extensible text editor. Emacs is freely available under the GNU license and is generally distributed with Linux operating systems. It has a Graphical and Terminal mode of operation and therefore makes it particularly appealing for HPC where remote editing of files is common.

#The Workshop
-
The aim of the workshop is to introduce the fundamental concepts and basic navigation for using Emacs. With Emacs being such a flexible and powerful editor the learning curve can be initially steep. As such, the workshop will contain live-demonstrations and exercises (text-editing and programming in c) to familiarise the user with using Emacs. After the workshop the user should have an understanding of the concepts behind Emacs and comfortable exploring more complex and powerful concepts within Emacs.

The workshop will consist of a presentation, live-demonstrations and exercises.


##Prerequisites

This workshop will require no previous knowledge of using Emacs. One exercise assumes knowledge of programming and compiling in C.

We will use a virtual machine for this tutorial. Install VirtualBox on your system (if you have not done so before). Refer to [the VirtualBox post]({filename}/virtualbox-basics/virtualbox-basics.rst) for further guidance on how to setup VirtualBox. A virtual machine is available which contains Emacs and gcc installed along with the documents to complete the tasks. This can be downloaded from: this [link](http://www.southampton.ac.uk/~ngcmbits/virtualmachines/Emacs_Intro.ova)
www.soton.ac.uk/~ngcmbits/virtualmachines.

The login username and password are feeg6003 and the task documents are stored in /home/feeg6003/Intro_to_Emacs.

Alternatively, you can download Emacs and a c compiler and simply download the tutorial documents from [here]({filename}/Emacs/Emacs_Tasks.tar)

##Presentation Slides

The presentation slides that were used for the workshop can be downloaded from [here]({filename}/Emacs/Introduction_to_EMACS.ppt)and provide an overview of the fundamental concepts involved with Emacs.

##Task: Basic Navigation and Use
For the first task, we introduce you to the basic navigation and use of Emacs by manipulating some example files.

### Basic Navigation

Begin by opening emacs. Do this by opening a terminal on the virtual machine by pressing ctrl-alt-t, then type 'emacs &' and press enter.

Once in emacs open the file named 'emacs_tutorial.txt'. The emacs mini-buffer acts like a terminal therefore you need to enter the file path and file name. You can also use tab complete.

The emacs_tutorial.txt file contains a list of commands for basic navigation of the buffers. It also contains instructions to create new buffers, move between buffers and delete buffers.

### Theme Changing

The theme of emacs can be changed to suit the users preferences. This is done by using alt-x load-theme. The options can be viewed by pressing tab. Select favoured theme then press enter.

### Calendar

A useful function of emacs is the built in calendar. To access the calendar type alt-x calendar. This will display the calendar in a new buffer. The calendar is read only however events can be added. To do this, move to the date you wish to create an event. Press i d to add event to that day, i w creates a weekly event and i y creates a yearly event. Ensure the buffer is saved. The event is saved to the buffer named 'diary', which is stored within the emacs directories.

Once the event has been created the user can then view the events of the day by typing 'alt-x diary' whilst working on another buffer.

### Tasks
A series of short tasks has been created to get the user to use emacs and learn the initial commands

1. Create new file
2. Import the âsample.txtâ file
3. Navigate through it
4. Add something at the end
5. Save
6. Add event to todays date
7. Go back to the file
8. Check what events are on today
9. Close the event buffer

#### Solutions

1. C-x C-f then type the name of the file you want to create
2. C-x i then find the file named 'sample.txt'
3. Get used to the C-f C-b etc commands from the tutorial
4. Make an addition to the buffer
5. C-x C-s
6. M-x calendar, go to todays date, i d to insert an event to that date. Ensure the buffer is saved before exiting
7. C-x C-f find the file.
8. M-x diary whilst in the created file buffer.
9. C-o to go to the event buffer, C-x 0 to close the buffer.

##Task: Using Emacs for practical

Emacs can be used to program in a variety of programming languages including C. In this section we will apply what we have learnt in the previous Emacs task to a some basic C programming and use of the terminal (All taught in Advanced Computational Methods I).

### Task 1

This task gives the user a taste of opening, editing and saving a C file and then using the terminal to compile it.

Open the C file "file01.c" (using C-x C-f)

The contents of the file should be displayed on the screen. Notice the syntax highlighting from Emacs switching to the C major mode (no music puns here). The file is riddled with errors and should be corrected and then saved (C-x C-s).

Once this is done, open the terminal in Ubuntu (Ctrl + Alt + t) and navigate to the working directory where "file01.c" resides. Compile the file using GCC to the same standards that we applied in ACM1 and name the file "file01"

gcc -ansi -Wall -pedantic -o file01 file01.c

Once this successfully compiles without errors, run the compiled code from the terminal

./file01

Then ensure the output is exactly

Number 0.
Number 1.
Number 2.
Number 3.
Number 4.
Number 5.
Number 6.
Number 7.
Number 8.
Number 9.

### Task 2a

Save the corrected file "file01.c" as "file02.c" (C-x C-w, NOT C-x C-s)

Edit file in Emacs so the final printed value is "Number 99."

Compile "file02.c" in the same way as "file01.c" and call the output file "file02".

Check the output looks correct and then pipe the output of the file into a text file called "text02.txt".

./file02 > text02.txt

Open the text file "text02.txt" in Emacs in a second window.

### Task 2b

Revert the for loop in "file02.c" to its previous value.

Save the file, recompile and pipe the output back to "text02.txt".

You should notice that although you have now changed the contents of the file, Emacs is still displaying the old contents...

Open the file "text02.txt" again in another frame to confirm that the file has indeed changed.
