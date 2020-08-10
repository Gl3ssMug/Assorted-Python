def grad(a,b,c,d):
    g=(d-b)/(c-a)
    return g

num1 = float(input("input x1"))
num2 = float(input("input y1"))
num3 = float(input("input x2"))
num4 = float(input("input y2"))
print(grad(num1,num2,num3,num4))

