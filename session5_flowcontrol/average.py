
# average of 1 to 1000

sum = 0

for x in range(1, 1001):
    sum += x

print("sum = {}".format(sum))

length = len(range(1,1001))

avg = sum/length

print(avg)

