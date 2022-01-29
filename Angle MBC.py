# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

a=int(input())
b=int(input())

c=math.hypot(a,b)
n=c/210

w=math.asin(1*a/c)
d=math.sqrt((b**2+n**2)-(2*b*n*math.cos(w)))
o=math.asin(math.sin(w)*n/d)

print(int(round(math.degrees(o),0)),'\u00B0',sep='')