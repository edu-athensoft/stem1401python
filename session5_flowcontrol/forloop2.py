# using for loop to calculate the sum of a list

list = [1,2,3,4,5,6,7,8,9,10]

sum = 0

for x in list:
    sum = x + sum

print("sum = {}".format(sum))

sum = 0
for x in range(1,10001):
    sum = x + sum

print("sum = {}".format(sum))