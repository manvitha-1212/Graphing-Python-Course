import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10000,10000,20)
dx = x[1]-x[0]
_dx=x[2]-x[1]
y = -x
dydx=np.gradient(y,dx)
_dydx=np.gradient(y,_dx)
plt.plot(x,_dydx)
plt.show()
