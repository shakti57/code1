#!/usr/bin/env python
# coding: utf-8
#
# In[1]:


# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the list
print("Original List:", numbers)

# Add an element to the list
numbers.append(6)

# Print the updated list
print("Updated List:", numbers)

# Calculate the sum of the list
total = sum(numbers)
print("Sum of the List:", total)


# In[2]:


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# In[3]:


import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)

print("Area of the circle:", area)


# In[4]:


input_string = input("Enter a string: ")
reversed_string = input_string[::-1]

print("Original String:", input_string)
print("Reversed String:", reversed_string)


# In[7]:


def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
result = fibonacci(num_terms)
print("Fibonacci Series:", result)


# In[ ]:





# In[ ]:




