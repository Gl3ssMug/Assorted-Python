def ans(a,b,d,e,c):
    u=b/a
    x=u/2
    y=-(pow(x,2))
    v=y*a
    z=c+v
    
    f=e/d
    i=f/2
    g=-(pow(i,2))
    l=g*d
    k=z+l
    return x,i,k

num1 = float(input("enter x^2"))
num2 = float(input("enter x"))
num3 = float(input("enter y^2"))
num4 = float(input("enter y"))
num5 = float(input("enter c"))
print(ans(num1,num2,num3,num4,num5))


