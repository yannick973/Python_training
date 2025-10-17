#simuler à l'aide de python un processus aleatoire de variation de luminosité d'une étoile quand 
# une exoplanete passe devant

import matplotlib.pyplot as plt
import numpy as np
import random
import os

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

def xyz(t):
    xP=a/R*np.sin(2*np.pi /T*(t-t0))
    yP=0.8
    zP=a/R*np.cos(2*np.pi /T*(t-t0))
    return xP,yP,zP

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

alpha=0.4
n=1000



tmin=494.5*24*3600
tmax=497*24*3600
dt=360 #toutes les 6 min

t=[]
lum_num=[]
u_lum_num=[]
temps=tmin
while temps < tmax:
    x,y,z=xyz(temps)
    if z>0: #transit de la planète devant l'étoile
        lum,u_lum=mesure_Kepler(x,y,alpha,n)
    else:
        lum,u_lum=mesure_Kepler(2,2,alpha,n)
    t.append(temps)
    lum_num.append(lum)
    u_lum_num.append(u_lum)
    temps= temps+dt
    print(round((temps-tmin)/(tmax-tmin)*100,1),'%')
t=np.array(t)
lum_num=np.array(lum_num)
u_lum_num=np.array(u_lum_num)

# --- Création du chemin de sortie ---
base_dir = os.path.dirname(__file__)  # dossier où se trouve ce script
output_dir = os.path.join(base_dir, "output", "exoplanete_transit_output")

# Création du dossier s’il n’existe pas déjà
os.makedirs(output_dir, exist_ok=True)

# --- Nom du fichier image ---
output_path = os.path.join(output_dir, "courbe_transit.png")

plt.figure()
plt.title("Courbe de transit exoplanétaire")
plt.xlabel('durée (en jours)')
plt.ylabel('luminosité apparente normalisée')
plt.errorbar(t/(24*3600),lum_num,yerr=u_lum_num,fmt='bo')
# --- Sauvegarde ---
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.show()




