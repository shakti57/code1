#!/usr/bin/env python
# coding: utf-8

# In[1]:

#11
# Using a for loop to print numbers from 1 to N
N = 5
for i in range(1, N + 1):
    print(i)


# In[2]:


# Using a for loop to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")


# In[3]:


# Using a for loop to find the sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
sum_result = 0
for num in numbers:
    sum_result += num

print(f"The sum of numbers is: {sum_result}")


# In[4]:


# Using a while loop to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

num_to_check = 11
if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number")
else:
    print(f"{num_to_check} is not a prime number")


# In[6]:


# Using a while loop to reverse a string
def reverse_string(input_str):
    reversed_str = ""
    index = len(input_str) - 1
    while index >= 0:
        reversed_str += input_str[index]
        index -= 1
    return reversed_str

original_str = "desrever"
print(f"The reversed string is: {reverse_string(original_str)}")


# In[ ]:




