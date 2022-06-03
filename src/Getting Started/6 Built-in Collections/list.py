# t = list(range(1, 16, 2))

# print(t)
#########################
# print(type(enumerate(t)))
# print(t[-2])
#########################
# print(t[1:3])
# print(t[1:])
# print(t[:3])
# s = t[:]
# print(s is t)  # False, this is a copy
#########################
# s = t[1:]
# print(t[1:] is t[1:])  # False, this is a copy
# print(t[1:] == t[1:] == s)  # True, this is a copy

###
# only references are copied not the whole reference of the list
###


#########################
# s = t[:]
# s[0] = 2
# print(t is s)  # False, this is a copy
#########################
# s = t.copy()
# s[0] = 2
# print(t is s)  # False, this is a copy
#########################
# s = list(t)
#########################
# print(t is s)  # False, this is a copy

#############################################

# a = [[1.2], [3, 4]]
# b = a[:]
# # print(a is b)  # False, this is a copy
# # print(a[0] is b[0])  # True, this is a copy of the same reference
# 
# b[0] = [10, 20]
# print(a[0] is b[0])  # False, we changed the reference of just b[0] not a[0]
# print(a[0])
# print(b[0])
#############################################

c = [1, 2]
print(c * 4)
c = [[1, 2]] * 4
print(c)
c[2].append(7)
# this will add 7 for every list at the big list,
# because the big list has duplicated lists from the same reference.
print(c)
