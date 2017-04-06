'''def midpoint(f, a, b, n):
    h = (b-a)/float(n)
    for i in range(1,n,1):
        s = f(a + i*h)
    return h*s'''

import numpy as np

def midpoint1(f, a, b, n):
    h = (b-a)/float(n)
    s=0
    for i in range(1,n,1):
        s += f*(a - (0.5*h) + i*h)
    return h*s

def midpoint2(f, a, b, n):
    h = (b-a)/float(n)
    s=[]
    for i in range(1,n,1):
        s.append(f*(a - (0.5*h) + i*h))
    sum2=sum(s)
    return h*sum2

def midpoint3(f, a, b, n):
   h = (b-a)/float(n)
   s=[]
   for i in range(1,n,1):
       s.append(f*(a - (0.5*h) + i*h))
   sum2=np.sum(s)
   return h*sum2

f=10
a=2
b=4
n=20

ans1=midpoint1(f,a,b,n)
print(ans1)

ans2=midpoint2(f,a,b,n)
print(ans2)

ans3=midpoint3(f,a,b,n)
print(ans3)