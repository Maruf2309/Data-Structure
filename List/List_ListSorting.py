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


my_list = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(my_list)
print(sorted_list) 

sorted_list_desc = sorted(my_list, reverse=True)  # Descending Sorting
print(sorted_list_desc)  

my_list = [5, 2, 9, 1, 5, 6]
my_list.sort()
print(my_list)  

