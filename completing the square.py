def answer(a,b,c):
    u=b/a
    x=u/2
    y=-(pow(x,2))
    v=y*a
    z=c+v
    return x,z

num1 = int(input("input x^2"))
num2 = int(input("input x"))
num3 = int(input("input c"))
print(answer(num1,num2,num3))



               

