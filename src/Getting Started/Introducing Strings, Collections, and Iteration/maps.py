# numbers = [2, 4, 6, 8, 10]
# 
# 
# # returns square of a number
# def square(number):
#     return number * number
# 
# 
# # apply square() function to each item of the numbers list
# squared_numbers_iterator = map(square, numbers)
# 
# print(squared_numbers_iterator)
# converting to list
# squared_numbers = list(squared_numbers_iterator)
# print(squared_numbers)

# Output: [4, 16, 36, 64, 100]

import collections

# def f():
#     return 3, 4


# first, second = f()
# print(first)
# (a, (b, (c, d), f)) = (1, (2, (3, 4), 5))
f = ''.join(['1', '2'])
print(f)
f = 'unforgettable'.partition('forgett')
print(f)
# ('un', 'forgett', 'able')

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day2': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps, '\n')

# print(type(f()), '\n')
print(type(res), '\n')
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))
