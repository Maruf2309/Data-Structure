# Example 7: Dictionary with Nested Structures
# Accessing and modifying elements in a dictionary with nested structures.

# Example dictionary with nested structures
nested_dict = {
    'person':{
        'name':'John',
        'details':{
            'age':30,
            'city':'New York',
            'skills':['Python', 'Data Science']
        }
    }
}

# Accessing nested elements
city = nested_dict['person']['details']['city']
# print(city)
# Modifying a nested element
nested_dict['person']['details']['skills'].append('Machine Learning')

# Print Result 
print('City :', city)
print('Updated Dictionary :', nested_dict)