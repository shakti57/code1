#!/usr/bin/env python
# coding: utf-8

# In[1]:

#
price=float(input("Enter Price"))
if(price>100000):
    print(" tax is 15% ")
elif(price>50000 and price<=100000):
    print("tax is 10% ")
else:
    print("tax is 5%")


# In[2]:


#explain the pgm
year=int(input("enter the year"))
 
if (year%4)==0:
    if(year%100==0):
        if(year%4==0):
            print(year,"year is leap year")
        else:
            print(year,"Not a leap year")
    else:
        print(year,"leap year")
else:
    print(year," not a leap year")


# In[3]:


num=int(input("enter anumber between 1 to 7------ "))
if(num==1):
    print("sunday")
elif(num==2):
    print("monday")
elif(num==3):
    print("tuesday")
elif(num==4):
    ptint("wednesday")
elif(num==5):
    print("thursday")
elif(num==6):
    print("friday")
elif num==7:
    print("saturday")
else:
    print("wrong entry")


# In[4]:


num1=input("enter any number")
l=len(num1)
if(l!=3):
    print("enter digit is 3 number digit")
else:
    print("middle digitis",(int(num1)%100//10))


# In[ ]:




