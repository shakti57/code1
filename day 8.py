#!/usr/bin/env python
# coding: utf-8
#  day8
# In[1]:


# Timedelta function demonstration
 
from datetime import date, timedelta

current_date = date.today()

# Calculating future dates
# for 730 days
future_date_after_2yrs = current_date + timedelta(days=730)
future_date_after_2yrs


# In[2]:


# Simple while loop
i=1
while i<6:
    print('While condition is true',i)
    i+=1


# In[3]:


# While loop with break.
#It is used to stop loop even if while condition is true
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1


# In[4]:


# While loop with continue statement.
i=0
while i<6:
    i+=1
    if i==3:
        continue

    print(i)


# In[5]:


# While loop with else statement.
i=7
while i <6:
    print(i)
    i+=1
else:
    print('While loop condition is false')


# In[ ]:




