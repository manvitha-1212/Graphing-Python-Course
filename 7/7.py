import matplotlib.pyplot as plt
import numpy as np
import math

r=6378000
l=np.arange(0,90,5)
t=24*60*60
g=9.81

o=(2*3.14)/t
w=[]
radian=[]
for i in l:
    a=math.radians(i)
    radian.append(a)


for j in radian:
    gl=g-r*(o*o)*(math.pow(math.cos(j),2))
    
    w.append(gl)

plt.plot(l,w)
plt.show()