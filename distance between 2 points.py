import math
def distance(a,b,c,d):
    x=math.sqrt((pow(d-b,2))+(pow(c-a,2)))
    return x

num1 = float(input("input x1"))
num2 = float(input("input y1"))
num3 = float(input("input x2"))
num4 = float(input("input y2"))
print(distance(num1,num2,num3,num4))
