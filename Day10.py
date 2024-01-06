#!/usr/bin/env python
# coding: utf-8

# In[1]:
#10

## Function with argument and return value
def squareofnum(a):
    '''Square Function :- This function will return the square of a number'''
    return a**2
squareofnum(10)


# In[3]:


def areaofcircle():
    r=float(input('Enter radius:'))
    return 3.14*r*r
areaofcircle()


# In[4]:


product  =  lambda  a,  b  :  a  *  b
#This  lambda  function  takes  two  arguments  (a,b)
#and do the multiplication
print(product(5,  6))


# In[5]:


# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


# In[6]:


# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# In[ ]:




