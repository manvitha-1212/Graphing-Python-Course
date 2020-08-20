import numpy as np
import matplotlib.pyplot as plt
class ODESolver(object):
    def __init__(self, omega_0 = 0, theta_0 = 10, eta=0.01, n_iter=10):
        self.omega_0 = omega_0
        self.theta_0 = theta_0
        self.eta = eta
        self.n_iter = n_iter
    def euler(self,alpha):
        
        self.time_ = np.zeros(self.n_iter)
        self.omega_ = np.zeros(self.n_iter)
        self.theta_ = np.zeros(self.n_iter)
        self.omega_[0] = self.omega_0
        self.theta_[0] = self.theta_0*np.pi/180.0
        
        for i in range(self.n_iter-1):
            self.time_[i+1] = self.time_[i] + self.eta
            self.omega_[i+1] = self.omega_[i] + self.eta*alpha(self.theta_[i])
            self.theta_[i+1] = self.theta_[i] + self.eta*self.omega_[i]
        return self
def alpha(x):
    return -np.sin(x)   

time=ODESolver(omega_0 = 0, theta_0 = 10, eta=0.1, n_iter=300).euler(alpha).time_
theta=ODESolver(omega_0 = 0, theta_0 = 10, eta=0.1, n_iter=300).euler(alpha).theta_
plt.plot(time,theta*180/np.pi,lw=3,color='red')
plt.xlabel('time(s)',size=10)
plt.ylabel('angle (deg)',size=10)
plt.title('Euler Method',size=10)
plt.show()