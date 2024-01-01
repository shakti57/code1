#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to calculate factorial: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")


# In[2]:


# Check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# In[3]:


# Adding two numbers using a function
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("Sum:", result)


# In[4]:


# Calculating the square of a number using a function
def square(x):
    return x ** 2

result = square(10)
print("Square:", result)


# In[5]:


# Concatenating strings
first_name = "Ram"
last_name = "Krishna"
full_name = first_name + " " + last_name
print("Full Name:", full_name)


# In[ ]:




