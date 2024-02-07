#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Day15
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)
print(df)


# In[2]:


import pandas as pd

# Reading a CSV file into a DataFrame
df = pd.read_csv('example.csv')
print(df)


# In[3]:


import pandas as pd

data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Selecting a column
print(df['Name'])

# Filtering based on a condition
print(df[df['Age'] > 30])


# In[4]:


import pandas as pd

data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Calculating mean, median, and standard deviation
print("Mean Age:", df['Age'].mean())
print("Median Age:", df['Age'].median())
print("Standard Deviation of Age:", df['Age'].std())


# In[5]:


import pandas as pd

data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Adding a new column
df['Salary'] = [50000, 60000, 75000]

# Updating values based on a condition
df.loc[df['Age'] > 30, 'Salary'] += 10000

# Dropping a column
df = df.drop('City', axis=1)

print(df)


# In[ ]:




