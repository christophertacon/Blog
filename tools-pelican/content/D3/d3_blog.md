title: D3 Data-driven Document
authors: Bruno Soriano, Markus Zauner
date: 21 April 2016
tags: D3, javascript, plot
slug: D3-blog


D3.js is a JavaScript library for manipulating documents based on data. It helps you bring data to life using HTML, SVG, and CSS. D3's emphasis on web standards gives you the full capabilities of modern browsers without tying yourself to a proprietary framework, combining powerful visualization components and a data-driven approach to Document Object Model (DOM) manipulation. 

<img src="http://www.optisolbusiness.com/wp-content/themes/optisol/images/innerpages/data%20driven%20document.png" alt="d3_logo"  style="width:256px;height:256px;align:" align="right">  

D3 allows you to bind arbitrary data to a DOM, and then apply data-driven transformations to the document. For example, you can use D3 to generate an HTML table from an array of numbers. Or, use the same data to create an interactive SVG bar chart with smooth transitions and interaction. 


D3 is not a monolithic framework that seeks to provide every conceivable feature. Instead, it solves the crux of the problem: efficient manipulation of documents based on data. This avoids proprietary representation and affords extraordinary flexibility, exposing the full capabilities of web standards such as HTML, SVG, and CSS. With minimal overhead, D3 is extremely fast, supporting large datasets and dynamic behaviours for interaction and animation.
    
For example, if we were to set the heights of some hypothetical bars in an HTML document with vanilla JavaScript, it'd look something like this: 

    var nums = [80, 53, 125, 200, 28, 97]; 
        
    var bars = document.getElementsByTagName("rect"); 
        for (var i = 0; i < bars.length; i++) { 
            var bar = bars.item(i); 
            bar.setAttribute("height", nums[i]); 
        }

With D3, it's 
  
    d3.selectAll('rect') 
     .attr('height', function(d, i) {return nums[i];}); 


D3 embraces declarative programming, and we can see that here: we're able to set the height of all elements in the collection using .attr, rather than having to set them individually using a for loop. Declarative code abstracts away implementation details, making complicated transformations easier to reason about. The library can be downloaded from <a href="https://github.com/mbostock/d3/releases/download/v3.5.16/d3.zip"> here</a> or can be linked directly to the latest version. HTML projects can be linked to the library by writing the following command

    <script src="http://d3.v3.min.js" charset="utf-8"></script>

The D3 library does not work only with webpage development, it can be used, for example, with Python. In this context, several D3 packages are available, such as, <a href="http://mpld3.github.io/"> MPLD3</a>, <a href="http://bokeh.pydata.org/en/latest/"> Bokeh</a>  and <a href="https://plot.ly/"> Plotly</a>. 
The <b>MPLD3</b> package is extremely easy to use: you can simply take any script generating a Matplotlib plot, run it through one of MPLD3's convenience routines, and embed the result in a web page. For those who are already using the Matplolib the additional code necessary to save a simple and interactive html plot is the following:

    mpld3.save_html(fig_name,"filename")

<b>Bokeh</b> is a Python interactive visualization library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of novel graphics in the style of D3.js, and to extend this capability with high-performance interactivity over very large or streaming datasets. This library will be used in the tutorial section.


<h1>Tutorial</h1>
In this tutorial, we will generate a exemplary scatter-plot for introducing the d3.js-package Bokeh in Python. You can download the tutorial instructions <a href="https://bitbucket.org/Bruno_Soriano/computationalmodelling.bitbucket.org/raw/401bc9b95d32558f0841edb649e82d69ad811a0e/tools-pelican/content/D3/handout.pdf"> here</a>.

For doing the tutorial, you need to download and import the appliance for a virtual machine (ubuntu). After starting, you can login with:

    username: acm2
    password: acm2

To launch the Jupyter Notebook (Python) containing the trainings-material (available <a href="https://bitbucket.org/Bruno_Soriano/computationalmodelling.bitbucket.org/raw/401bc9b95d32558f0841edb649e82d69ad811a0e/tools-pelican/content/D3/Tutorial.ipynb"> here</a>), you just have to open a terminal and type in following command:
    
    jupyter notebook
    
A tab in the browser will open automatically. If you navigate to the 'D3_Tutorial' folder in the home directory, you will find a Tutorial.ipynb file to start with.  A click on it will open a new tab in the browser.

The tutorial is devided in subsections. Each section can be run separately.  The first cell contains all used packages that are used.  The next cell contains some arbitrary generated data for generating later a scatter-plot followed by a cell where we need to define the tools, we want to provide in our plot.  Now we generate a simple scatter-plot without using any tools.
