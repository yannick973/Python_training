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

