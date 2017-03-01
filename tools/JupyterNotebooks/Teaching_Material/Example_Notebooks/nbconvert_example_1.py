
# coding: utf-8

# In[1]:

print("hello world")


# In[2]:

2+3


# In[3]:

import numpy


# In[5]:

f1 = lambda x: x+4

def f2(x, y):
    return x * y


# In[6]:

f1(2)


# In[7]:

f2(5, 3)


# In[8]:

x = 38
f1(x)


# In[9]:

x = numpy.linspace(0, 4, 11)
y = f1(x)
y


# In[10]:

z = f2(x, y)
z

