
a = float(input("please input side a= "))
b = float(input("please input side b= "))
c = float(input("please input side c= "))

# print(type(a),type(b),type(c))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("area is {}, a={}, b={}, c={}".format(area,a, b, c ))