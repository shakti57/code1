#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Range function
for i in range(1,10):
# range is a generator function which
#yields numbers from specified start to end point
    print(i)


# In[2]:


# Nested loops
list1=['Maths','Science','Geo','Eco','Social']
list2=[78,90,70,56,90]
for i in list1: # Outer loop
    for k in list2: # inner loop
        print(i,k)


# In[3]:


a=['red','blue','green']
b=['Apple','Banana','Orange']
for i in a: ## outer loop
    for h in b: ## inner loop
        print(i,h)


# In[4]:


l = [34,66,43,23,27,88,74,16]
for c in l:
    if(c%2==0):
        print(c,'is even')
    else:
        print(c,'is odd')


# In[5]:


city = ['bangalore', 'Mumbai',  'Pune']
for index in range(len(city)):
    print('Current city :', city[index])

print("Good bye!")


# In[ ]:




