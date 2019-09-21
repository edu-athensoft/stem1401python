# mistake values
odd = [2, 4, 6, 8]
print(odd)

# change the 1st item
odd[0] = 1
odd[3] = 9

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]
print(odd)


#======================

odd = [1, 3, 5]
odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)


# to concatenate two lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1 + list2)

#Output: ["re", "re", "re"]
print([1,2,3,4] * 3)


odd2 = [1, 9]
odd2.insert(1,3)
print(odd2)

odd2[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]
print(odd2)