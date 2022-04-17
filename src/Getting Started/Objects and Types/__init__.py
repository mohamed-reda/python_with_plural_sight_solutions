i = [13]
x = i
print('case 1-----------------------------')
print(f'id(i) = {id(i)}')
print(f'id(x) = {id(x)}')
print(f'id(i[0]) = {id(i[0])}')

print(f'id(x[0]) = {id(x[0])}')

print('\ncase 2-----------------------------')

i[0] = 12

print(f'id(i) = {id(i)}')
print(f'id(x) = {id(x)}')

print(f'id(i[0]) = {id(i[0])}')

print(f'id(x[0]) = {id(x[0])}')

print('-----------------------------')

"""
So here, the id of the first index who just changed, not tje id of the list

""" 
