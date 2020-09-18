from sympy import *
from sympy.plotting import plot
x = symbols('x')


    
y=diff(-x,x,x)
p1 = plot(y, (x,-10000,10000),show=False,line_color='red',points=1000)

p1.append(p1[0])


p1.show()