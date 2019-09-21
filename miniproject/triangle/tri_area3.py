a = float(input("please input side a= "))
b = float(input("please input side b= "))
c = float(input("please input side c= "))

# print(type(a),type(b),type(c))


# if a,b,and c can compose a valid triangle, then calculate the area, otherwise show an alert "not a valid triangle"

# a + b > c  and   a + c > b  and c + b > a

if(a + b > c and  a + c > b and c + b > a ):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("area is {}, a={}, b={}, c={}".format(area, a, b, c ))
else:
    print("Not a valid triangle, please try again!")

