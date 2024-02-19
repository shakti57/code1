#!/usr/bin/env python
# coding: utf-8

# In[1]:
#day 02

# conditional statement pgm
# if
a=20
b=30
if(a<=b):
    print("a is smaller than b")
print("block end")


# In[2]:


a=20
b=20
if(a<b):
    print("a is smaller than b")
if(a==b):
    print("a is equals to b")
print("block end")


# In[3]:


a=100
b=20
if(a<b):
    print("a is smaller than b")
if(a==b):
    print("a is equals to b")
if(a>b):
    print("a is greater than b")
print("block end")


# In[4]:


a=int(input("enter A- "))
b=int(input("enter B- "))
if(a<b):
    print("A is smaller than B")
if(a==b):
    print("A is equals to B")
if(a>b):
    print("A is greater than B")
print(" if block end")


# In[5]:


marks=float(input(" Enter Your Percentage(%)--"))
if(marks>90):
    print("Your Grade is A")
elif(marks<=90 and marks>80):
    print("Your Grade is B")
elif(marks>=60 and marks<=80):
    print("Your Grade is C")
else:
    print("Your Grade is D")


# In[ ]:




