#!/usr/bin/env python
# coding: utf-8

# In[1]:


x  = 20
y  = 30

print('Is  x  greater  than  y  :-  ',x>y) 
print('Is  x  less  than    y  :-  ',x<y) 
print('Is  x  equal  to    y  :-  ',x==y)
print('Is  x  not  equal  to  y  :-  ',x!=y)
print('Is  x  greater  than  or  equal  to  y  :-  ',x>=y)
print('Is  x  less  than  or  equal  to  y  :-  ',x<=y)


# In[2]:


x = True
y = False

print('Logical  AND  operation  :-  ',x  and  y)  #  True  if  both  values  are  true
print('Logical  OR  operation  :-  ',x  or  y)  #  True  if  either  of  the  values  is  true
print('NOT  operation  :-  ',not  y  )  #  True  if  operand  is  false


# In[3]:


x=11
if(x>10):
    print('i am in if block')
elif(x==6):   
# elif will help in checking more than 1 if condition
    print('i am in elif block')
elif(x==0):
    print('Zero number')
else:
    print('i am in else block')  


# In[4]:


## Nesting
x=5
if(x>=3):
    print('i am in 1st if')
    if(x>2):
        print('i am in 2nd if')
        if(x==4):
            print('i am in 3rd if ')


# In[5]:


i=4
if(i>0):
    print('first loop')
    if(i<=5):
        print('second loop')
        print('number is in primary range')
        if(i>5): #False
            print('mid range')
        else:
            print('end of the loop')
else:
    print('number is negative')

print('out of the nested loop')  


# In[ ]:




