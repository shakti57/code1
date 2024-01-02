#!/usr/bin/env python
# coding: utf-8

# In[1]:


def digit_names(number):
    # Define a mapping between digits and their names
    digit_mapping = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    # Convert the number to a string to iterate over its digits
    number_str = str(number)

    # Display the names of the digits
    digit_names_list = [digit_mapping[digit] for digit in number_str]

    # Print the result
    result = ' '.join(digit_names_list)
    print(result)

# Get input from the user
user_number = int(input("Enter a number: "))

# Display the digit names
digit_names(user_number)


# In[2]:


def calculate_percentage(total_marks, obtained_marks):
    try:
        # Calculate percentage
        percentage = (obtained_marks / total_marks) * 100

        # Display the result
        print(f"Total Marks: {total_marks}")
        print(f"Obtained Marks: {obtained_marks}")
        print(f"Percentage: {percentage:.2f}%")

    except ZeroDivisionError:
        print("Error: Total marks cannot be zero.")

# Get input from the user
total_marks = float(input("Enter total marks: "))
obtained_marks = float(input("Enter obtained marks: "))

# Call the function to calculate and display the percentage
calculate_percentage(total_marks, obtained_marks)


# In[3]:


i=0
while i < 20:
    print(i)
    i += 1


# In[4]:


name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")
print(tup)


# In[5]:


dict1 = {'age': 35, 'name': 'abc', 'salary': 45000}

val = dict1['age']

if val in dict1:
    print('This is a member of the dictionary')
else:
    print('This is not a member of the dictionary')


# In[6]:


def convert(t):
    return t*9/5 + 32

print(convert(20))


# In[ ]:




