import numpy as np
import matplotlib.pyplot as plt

def mesure_luminosite(x,y,alpha,n):
    compteur=0
    for k in range(n):
        x0=np.random.uniform(-1,1)
        y0=np.random.uniform(-1,1)
        if (x0**2+y0**2)<=1 and ((x0-x)**2+(y0-y)**2 > alpha**2):
                                 compteur+=1
    return 4 * compteur / n / np.pi


alpha=0.1

n= 10000

L = mesure_luminosite(x=0.3, y=0.4, alpha=alpha, n=n)

print(L)
