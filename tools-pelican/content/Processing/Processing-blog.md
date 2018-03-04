title: Processing Language Basics
authors: James Brooks; Chris Tacon
date: 2018-03-06
tags: processing, visualisation, visualization, art, coding, language, IDE
slug: Processing-Blog

#Introduction to Processing
**Processing** is a spinoff of Java designed to simplify the task of creating complex visualisations, computational artworks, GUIs and games! Since its origins lie in Java, it is object orientated and shares a common syntax. Processing is also open source and can be run and coded on Windows, Mac or Linux.

Processing was developed back in 2001 by Casey Reas and Ben Fry at the MIT Media Lab and was further developed by the Processing Foundation along with Daniel Shiffman.

#How to Open Processing
If you are using the Virtual Machine supplied for the workshop:  
***Step 1***: Boot up the virtual machine  
***Step 2***: Open a terminal (e.g. LXTerminal)  
***Step 3***: Type the following into the terminal:
```vim
cd processing-3.3.6
./processing
```

Processing files are contained within folders (or directories) of the same name. They have the extension: ***.pde***  
Easiest to open Processing files from within the Processing IDE.


#Handy Links
[Downloads](https://www.processing.org/download)
[Online Tutorials](https://www.processing.org/tutorials/)
[Example Code](https://www.processing.org/examples/)

#How to Code in Processing
As Processing is built on the Java language the syntax is similar and the coding is object orientated. There are two key functions when writing a Processing program: the **setup()** and **draw()** functions.

The setup() function is run once while the draw() function is run on a loop at each frame. The setup() function should therefore contain the code needed at the beginning of the program such as declaring the size of the canvas and initializing any objects and variables.

```java
void setup() {
	size(100, 200);
}
```

This code would setup the canvas with dimensions 100x200. This simultaneously sets the values of the variables **width** and **height** to be 100 and 200 respectively. The coordinates of a point on the canvas are given by (x, y) where x,y travel along the width and height respectively. The origin (0,0) of the canvas is at the top left corner and so y increases as you both down the canvas.

##Hello World
In Processing it is possible to print output to the command line visible in the IDE using the command **println()**. Printing to the command line can be useful to determine information about your program but is not what Processing is made for. For example to write the phrase "Hello World" on the canvas we could use the code:
```java
void setup() {
	size(400, 400);
	background(0);
}

void draw() {
	stroke(255);
	textAlign(CENTER);
	textSize(40);
	text("Hello World", 200, 200);
}
```

Lets break down exactly what this code is doing: The setup function is called when the program is run and sets up a canvas of size 400x400 with a Black background (We will cover colours in more detail later). The draw function is then run repeatedly, in this case the program is actually writing the phrase to the screen repeatedly at each frame and visually we would see the same result by placing all the code within the setup() function. Inside the draw() function we set the stroke to 255 which means the text will be white and the text size to be at 40pts. We then display the text "Hello World" at coordinates (200,200) which which is at the center of the text due to the align setting. 

##Shapes
below is a list of the code to draw several common types of shapes:

| Command | Shape |
| :-- | :-- |
| `point(x, y);` | `Point` |
| `line(x1,y1,x2,y2);` | `Line` |
| `rect(x,y,width,height);` | `Rectangle` |
| `triangle(x1,y1,x2,y2,x3,y3);` | `Triangle` |
| `ellipse(x,y,width,height);` | `Ellipse` |
| `arc(x,y,width,height,start,stop)` | `Arc` |
| `box(width,height,depth);` | `Box` |
| `sphere(radius);` | `Sphere` |

Some important alligning functions when placing these shapes on the canvas are:

| Shape | Function | Mode |
| :-- | :-- | :-- |
| `Rectangle` | `rectMode(mode)` | `CORNER or CENTER` |
| `Ellipse` | `ellipseMode(mode)` | `RADIUS or CENTER` |
| `Text` | `textAlign(horizontal, vertical)` | `horizontal: LEFT,RIGHT,CENTER vertical: TOP,BOTTOM,CENTER` |

##Colours

In this section we will talk about how to add colour to your program. Colours in Processing are described by numbers ranging from 0-255, where 0 represents a 'weak' amount colour and '255' a strong amount colour. For example if we consider the familiar function:

```java
background(0);
```

When we have a single input the number represents the amount of white, therefore for here where we have 0 the background will be black. Similary if we put 255 the background would be white and for numbers in between varying shades of grey.

Colours can also be defined by a tuple **(R,G,B)** representing Red, Green and Blue respectively. The strength of each colour is given by a number ranging between 0-255 as before.

The following functions can be used to insert a colour:

| Function | Effect |
| :-- | :-- |
| background(R, G, B); | Background Colour |
| fill(R,G,B); | Fill Colour |
| noFill(); | Remove Fill (Fully Transparent) |
| stroke(R,G,B); | Border/Line Colour |
| noStroke(); | Remove Borders |

We should say here that the order of which these statements appear matters, everything after a fill() statement will be filled with that colour and so care must be taken when applying colour.

There is also another variable **alpha** which can be added as an argument i.e **(R, G, B, alpha)**, this sets the transparancy and also ranges from 0-255 with 0 being completely transparent and 255 opaque.

##IO

Below we will list the code for various methods to load input data and write output:

**Loading in Text File**

```java
String lines[] = loadStrings("data.text");		//Load lines of text
for(int i=0; i<lines.length; i++) {			//Cycle through each line
	String pieces[] = split(lines[i], '\t');	//Split each line into words
}
```

**Loading in Image File**
```java
Pimage img;				//Declare variable of Pimage type
img = loadimage("myImage.jpg");		//Load the image into the program
image(img,x,y,width,height);		//Place image
```

**Writing to Text File**
```java
PrintWriter output = createWriter("DataOut.txt");		//Create output file
output.println(DataToWrite);					//Write to file
output.close();							//Close write file
```

**Print to Console**
```java
println("String");	//test
```

##Interactivity
In Processing you are able to interact with the canvas using the mouse and keyboard this opens up opportunities to be create by adding in buttons, maneuverability and other possiblities.

###Keyboard

```java
if(keyPressed) {
	if (key == 'alphanumeric') {
		/*functionality*/
	} 
}
```

This code begins by checking if the key pressed is alphanumeric, that is a letter a-z or number 0-9. Having checked that you can add some functionality to respond to the key being pressed. The **keyPressed** variable is a bollean and takes the value true if a key is pressed and false if not.

**Special keys**
```java
if (keyPressed) {
	if (key == CODED) {
		if (keyCode == see below) {
			/*functionality*/
		}
	}
}
```

This code checks to see if a key is pressed, it then checks to see if the key is 'coded'. The keyCodes for these special coded keys include: ALT, CONTROL, SHIFT, UP, DOWN, LEFT, RIGHT.

###Mouse
```java
mouseX;			//Takes the value of the x coordinate in pixels of the cursor on the canvas
mouseY;			//Takes the value of the y coordinate in pixels of the cursor on the canvas
```

```java
pmouseX;		//x position of cursor at previous frame
pmouseY;		//y position of cursor at previous frame
```

```java
if (mousePressed == True) {
	/*functionality*/
}
```

As with the keyboard the mousePressed variable is a boolean returning true if a mouse button is pressed and false otherwise.


##Object Orientated Programming

In this section we we will give a brief introduction into object orientated programming and classes. Object orientated programming works by defining a class of objects which share the same attributes: For example you might have a class Ball with attributes of colour and radius.

An object is then defined as an instance of this class with given values for these attributes: For example the object red ball is an instance of the class Ball.

You declare an object as you would a variable:

```java
Classname object;			//E.g Ball red_ball
```

You can then initialise this object:

```java
object1 = new Classname(Temp Values);
```

This creates a new object of the type Classname with specific attributes given by Temp Values. For example **red_ball = new Ball([255, 0, 0]);**.

**Class Structure**

```java
Class Classname {
	//Class Variables
	Var_type Var_name;
	//Constructor
	Classname(Temp Values) {
		/*Assign value to variable
		From temporary variable*/
		Var_name = Temp_Var;
	}
	//Class Functions
	Return_type function(/*External Inputs*/) {
	}
}
```
The values entered when initializing the object are passed to the constructor within the class which generates the new instance of the class, the object. You can also define functions within the class, these functions are then called on the object using the syntax:

```java
object.function(values);
```

Where the values correspond to the external inputs defined in the class. For example you may have a display() function for the ball which draws the red ball.

#Resources

PDF Slides: [Presentation Slides]({filename}/Processing/Slides.pdf)

Powerpoint Slides: [Powerpoint Slides]({filename}/Processing/Slides.pdf)

Crib Sheet Docx: [Crib Sheet Docx]({filename}/Processing/Crib.docx)

Crib Sheet PDF: [Crib Sheet PDF]({filename}/Processing/Crib.pdf)








