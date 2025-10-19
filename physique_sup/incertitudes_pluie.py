import numpy as np
import matplotlib.pyplot as plt

m1 = 72
delta_m1 = 5
N = 1000000
m1_MC = m1 + delta_m1*np.random.uniform(-1,1,N)
plt.hist(m1_MC,bins=100)
plt.show()