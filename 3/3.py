import matplotlib.pyplot as plt
import numpy as np
import math as m

l=1
g=9.81
T=(2*3.14)*(m.sqrt(l/g))
t=[]
a=np.arange(0,90,5)

for i in a:
    t.append(T)

plt.plot(a,t)
plt.xlabel('theta')
plt.ylabel('time')

plt.show()
