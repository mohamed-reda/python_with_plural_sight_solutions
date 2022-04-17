# rebinding_global_names


count = 0


def set_count(c):
    global count
    count = c


#     count here is a local varible


set_count(10)
print(count)
"""
0
"""
