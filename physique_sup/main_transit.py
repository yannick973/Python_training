#simuler à l'aide de python un processus aleatoire de variation de luminosité d'une étoile quand 
# une exoplanete passe devant
from fonctions import *

moyenne, ecart_type = mesure_Kepler(2, 2, 0.1, 1000)
print(f"Luminosité moyenne : {moyenne:.8f}, écart-type : {ecart_type:.8f}")
