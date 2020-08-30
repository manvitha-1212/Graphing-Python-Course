import numpy as np
import matplotlib.pylab as plt
import math as m
angle=np.arange(0,90,5)
def ran(angle):

    g=9.81
    u=15
    T=np.arange(0,30,.001)
    b=u*(m.sin(m.radians(angle)))
    a=u*(m.cos(m.radians(angle)))
    x=[]
    y=[]
    y1=0
    y1d=y1
    x1=0
    x1d=x1
    ad=a
    bd=b


    for t in T:
        x1=x1d+a*0.0001
        a=ad+(-a)*0.0001
        ad=a
        x1d=x1
        y1=y1d+b*(0.0001)
        b=bd+(-g-b)*0.0001
        bd=b
        y1d=y1
        if(y1<0):
            return x1
r=[]
for ang in angle:
	r.append(ran(ang))
plt.plot(angle,r,color="green")
plt.show()