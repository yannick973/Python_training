#simuler à l'aide de python un processus aleatoire de variation de luminosité d'une étoile quand 
# une exoplanete passe devant

import numpy as np
import random

def mesure_luminosite(x,y,alpha,n):
    compteur=0
    for k in range (n):
        x0 = np.random.uniform(-1,1)
        y0 = np.random.uniform(-1,1)
        if (x0**2+y0**2) <= 1 and ((x0-x)**2 + (y0-y)**2 > alpha**2):
            compteur +=1
    return 4 * compteur / n / np.pi

def mesure_Kepler(x,y,alpha,n):
    mesures=[]
    for i in range(10):
        mesures.append(mesure_luminosite(x,y,alpha,n))
    return np.mean(mesures), np.std(mesures,ddof = 1)

#print(mesure_Kepler(2,2,0.1,1000))
#période orbitale T(s)
T = 4.9*24*3600
#décalage temporel t0 (s)
t0=495.8*24*3600

MSol=1.99e30
RSol=6.96e8
M=1.36*MSol
R= 2.02*RSol
G=6.67e-11
ua=1.50e11
a = 0.063*ua

def xyz(t):
    xP=a/R*np.sin(2*np.pi /T*(t-t0))
    yP=0
    zP=a/R*np.cos(2*np.pi /T*(t-t0))
    return xP,yP,zP


