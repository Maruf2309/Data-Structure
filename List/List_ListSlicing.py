# Example 5: Removing Elements from a List
# You can remove elements from a list using remove() and pop().
# remove() deletes the first occurrence of a value, while pop() removes an element by index.

# Example list
my_list = ['a', 'b', 'c', 'd']

# Removing elements
my_list.remove('b')
popped_item = my_list.pop(2)

# Printing the list after removal
print('List after Removal:', my_list)
print('Popped Item:', popped_item)

# Define a list
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Basic slicing [start:stop]
print(my_list[1:5])  

# Slicing with step [start:stop:step]
print(my_list[0:7:2])  

# Omitting start index (starts from 0 by default)
print(my_list[:4]) 

# Omitting stop index (goes to the end of the list)
print(my_list[3:])  

# Negative indices (start counting from the end)
print(my_list[-3:])  

# Full list copy
print(my_list[:])  
