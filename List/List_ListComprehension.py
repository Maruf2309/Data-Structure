# Example 7: List Comprehension
# List comprehension is a concise way to create lists using an expression and iteration.
# It can be used to generate new lists from existing ones.

# Creating a list of squares of numbers from 0 to 4
squared_list = [x**2 for x in range(5)]

# printing the list
# print('Squared List :', squared_list)


# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print('Even Number :',even_numbers)


# Converting strings to uppercase
words = ['hello', 'world', 'python', 'rocks']
uppercase_words = [word.upper() for word in words]
print(uppercase_words)
