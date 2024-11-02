# Example 8: List Comprehension with Conditional Nesting
# Using list comprehension with nested loops and conditions to filter elements.

# Example matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flattening and filtering even numbers from the matrix (2D matrix)
even_flattened = [num for row in matrix for num in row if num % 2 ==0]

print('Flattened Even Numbers:', even_flattened)

## Flattening the Matrix: It iterates through each row in the matrix, and then each number in those rows, effectively flattening the 2D list into a 1D list.
