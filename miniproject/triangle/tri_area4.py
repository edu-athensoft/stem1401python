a = float(input("please input side a= "))
b = float(input("please input side b= "))
c = float(input("please input side c= "))

# a = 3.5
# b = 6
# c = 1

# print(min(a,b,c))
# print(max(a,b,c))

side = [a,b,c]
side.sort()

# print(side)
# print(side[-1])

# if a,b,and c can compose a valid triangle, then calculate the area, otherwise show an alert "not a valid triangle"

# a + b > c  and   a + c > b  and c + b > a
if(side[0]+side[1] > side[-1]):
# if(a + b > c and  a + c > b and c + b > a ):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("area is {}, a={}, b={}, c={}".format(area, a, b, c ))
else:
    print("Not a valid triangle, please try again!")



