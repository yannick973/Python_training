#on cherche à prédire l'évolution d'une file de voitures
# notamment la formation de bouchons en accordéons
# et aussi le démarrage de voitures à l'arrêt, au passage d'un feu au vert

import matplotlib.pyplot as plt

a = 1.4 # accélération constante de la premiere voiture
Vmax = 14
tf = Vmax/a
taud = 2
tauR = 0.9 # temps de réaction moyen
L0= 5 #distance entre deux voitures consécutives à l'arrêt
k = 30
pas = tauR/100 
N = 200 # Nb de voitures dans la file
nbre = int((tf+N*taud+10*tauR)/pas) #nb d'itérations dans la méthode d'Euler