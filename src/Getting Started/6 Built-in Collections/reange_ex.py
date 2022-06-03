# range(stop)
# range(start, stop)
# range(start, stop, steps)
print(list(range(1, 16, 2)))

### 
# enumerate:
#   get the index and then the value as a tuple for every element of the list.
###
t = list(range(1, 16, 2))

for p in enumerate(t):
    print(p)
