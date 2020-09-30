from matplotlib import pyplot as plt
import math
import numpy as np

from sympy import symbols, Eq, solve


co=[0]*10

print("Root locus is drawn with help of OLTF, so give value of OLTF")
print("For ax^3+bx^2+cx^1+d, consider this is denomenator and give value of a,b,c,d" )

a1=int(input())
b1=int(input())
c1=int(input())
d1=int(input())
   

print("For ax^3+bx^2+cx^1+d, consider this is numerator and give value of a,b,c,d" )
a2=int(input())
b2=int(input())
c2=int(input())
d2=int(input())


X=list()
Y=list()
for k in range(0,10000,1):
    k1=k/100
    print(k1)
    x = symbols('x')
    
    sol = solve(a1*(x**3)+b1*(x**2)+c1*(x**1)+d1+k1*(a2*(x**3)+b2*(x**2)+c2*(x**1)+d2))
    for i in range(0,len(sol)):
        
        co[i]=complex(sol[i])
        
        X.append(co[i].real)
        Y.append(co[i].imag)
        
plt.plot(X,Y,'ro')
plt.show()   

    



    



