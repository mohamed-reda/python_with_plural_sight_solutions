import time


# print(time.ctime())
# print(time.ctime())
# print(time.ctime())
# print(time.ctime())
# print(time.ctime())
# print(time.ctime())


def Mo(menu=None):
    if menu is None:
        menu = []
    menu.append('Mo')
    print(menu)


Mo()
Mo()
Mo(['Hello'])
Mo()

"""
['Mo']
['Mo']
['Hello', 'Mo']
['Mo']
"""
"""
['Mo']
['Mo', 'Mo']
['Hello', 'Mo']
['Mo', 'Mo', 'Mo']
"""
