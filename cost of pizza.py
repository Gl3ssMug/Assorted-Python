import math
def cost(a):
    c=1.5*(pow(a/2,2))*math.pi
    return c

num1 = float(input("input diameter"))
print(cost(num1))
