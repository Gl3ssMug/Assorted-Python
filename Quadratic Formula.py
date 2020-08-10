import math

def ans(a,b,c):
	x=((-b)+(math.sqrt(pow(b,2)-(4*a*c))))/(2*a)
	y=((-b)-(math.sqrt(pow(b,2)-(4*a*c))))/(2*a)
	return x,y
	
a = float(input("enter ax^2"))
b = float(input("enter bx"))
c = float(input("enter c"))
print(ans(a,b,c))


