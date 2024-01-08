#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import keyword
import keyword


# In[3]:


print(keyword.kwlist)


# In[4]:


intvar = 10 # Integer variable
floatvar = 2.57 # Float Variable
strvar = "Python Language" # String variable
print(intvar)
print(floatvar)
print(strvar)


# In[5]:


intvar , floatvar , strvar = 10,2.57,"Python Language" 
# Using commas to separate variables
print(intvar)
print(floatvar)
print(strvar)


# In[7]:


p1 = p2 = p3 = p4 = 47 
# All variables pointing to same value
print(p1,p2,p3,p4)


# In[8]:


import sys


# In[10]:


val2 = 92.78 # Float data type
print(val2)
print(type(val2)) # type of object
print(sys.getsizeof(val2)) # size of float object in bytes
print(val2, " is float?", isinstance(val2, float)) # Val2 is an instance of float


# In[11]:


val3 = 25 + 10j # Complex data type
print(val3)
print(type(val3)) # type of object
print(sys.getsizeof(val3)) # size of float object in bytes
print(val3, " is complex?", isinstance(val3, complex)) # val3 is an instance of complex


# In[ ]:




