# Program: gov.py
# Purpose:...

# Date Started: 26 March 2018

import numpy as np
import random
import matplotlib.pyplot as plt

# Parameter values
s = 0.2
delta = 0.1
alpha = 0.35
A = 10.0
phi_ss = 0.2

random.seed(402)

# Steady-state values
Kstar = A*(s*(1-phi_ss)/delta)**(1/(1-alpha))
Ystar = (A**(1-alpha))*Kstar**(alpha)
Cstar = (1-s)*Ystar
Istar = s*Ystar

horizon = 125
Ksim = Kstar*np.ones((horizon, 1))
Ysim = Ystar*np.ones((horizon, 1))
Isim = Istar*np.ones((horizon, 1))
Csim = Cstar*np.ones((horizon, 1))
rsim = 0.0*np.ones((horizon, 1))

phi_sim = 0.17 + 0.06*np.random.rand(horizon,1)

for ii in range(25, horizon):
    Ksim[ii] = (1-delta)*Ksim[ii-1] + Isim[ii-1]
    Ysim[ii] = A**(1-alpha)*(Ksim[ii])**alpha
    Isim[ii] = s*(1-phi_sim[ii])*Ysim[ii]
    Csim[ii] = (1-s)*Ysim[ii]
    rsim[ii] = Cstar/Csim[ii] - 1

    
plt.plot(Ksim)
plt.title("K")
plt.show()

plt.plot(rsim)
plt.title("r")
plt.show()


