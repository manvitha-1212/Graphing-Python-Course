#without air resistance
import numpy as np
import matplotlib.pylab as plt
import math as m


u=10
T=np.arange(0,30,.001)
a=u*(m.sin(m.radians(45)))
b=u*(m.cos(m.radians(45)))
x=[]
y=[]
y1=0

for t in T:
    
    
    y1=a*t-((9.81/2)*(t**2))
    if y1<0:
		    break
    x.append(b*t)
    y.append(y1)

plt.plot(x,y)
plt.show()     

        

