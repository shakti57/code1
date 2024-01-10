#!/usr/bin/env python
# coding: utf-8

# In[1]:

#14d
import numpy as np

# Create a 1D array
array1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array
array2d = np.array([[1, 2, 3], [4, 5, 6]])

# Perform basic operations
sum_array1d = np.sum(array1d)
mean_array2d = np.mean(array2d)

print("1D Array:", array1d)
print("2D Array:")
print(array2d)
print("Sum of 1D Array:", sum_array1d)
print("Mean of 2D Array:", mean_array2d)


# In[2]:


import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Perform element-wise addition, subtraction, multiplication, and division
addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# In[3]:


import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Access elements using indexing
element_at_index_2 = arr[2]

# Slice the array
subset = arr[1:4]

print("Original Array:", arr)
print("Element at index 2:", element_at_index_2)
print("Subset (index 1 to 3):", subset)


# In[4]:


import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
matrix_product = np.dot(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Matrix Product:")
print(matrix_product)


# In[5]:


import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array to a 2x3 matrix
reshaped_arr = arr.reshape(2, 3)

# Create two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Stack the arrays vertically and horizontally
vertical_stack = np.vstack((array1, array2))
horizontal_stack = np.hstack((array1, array2))

print("Original 1D Array:", arr)
print("Reshaped 2x3 Array:")
print(reshaped_arr)
print("Vertical Stack:")
print(vertical_stack)
print("Horizontal Stack:", horizontal_stack)


# In[ ]:




