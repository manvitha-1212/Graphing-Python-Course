from sympy import *
import matplotlib.pyplot as plt
x=Symbol('x')

    
y=diff(-x,x,x)



plt.plot(x,y)
plt.show()
