a = ['p','r','o','b','l','e','m']
print(a)

# remove an item
del a[0]
print(a)

a.remove('r')
print(a)

# Output: 'm'
print(a.pop())
print(a)

#clear a list, remove all items
a.clear()

# Output: []
print(a)


