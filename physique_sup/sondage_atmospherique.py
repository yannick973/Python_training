import matplotlib.pyplot as plt
import numpy as np


# Altitude en km
zexp = np.array([
    0.0, 5.0, 10.0, 12.0, 20.0, 25.0, 30.0, 35.0, 40.0,
    45.0, 48.0, 52.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0,
    84.0, 92.0, 95.0, 100.0
])
#Température en °Celsius
Texp = np.array([
    15.0, -18.0, -49.0, -56.0, -56.0, -51.0, -46.0, -37.0,
    -22.0, -8.0, -2.0, -2.0, -7.0, -17.0, -33.0, -54.0,
    -65.0, -79.0, -86.0, -86.0, -81.0, -72.0
])

def T(z, unite):
    z_km = z / 1000      # Conversion en km pour comparaison dans la liste
    alpha = 1            # Valeur par défaut pour la conversion en K
    if unite == 'C':
        alpha = 0        # Pas de décalage pour la température en °C

    i = 0
    while z_km > zexp[i + 1]:  # Recherche de l’indice i
        i = i + 1

    # Interpolation linéaire entre zexp[i] et zexp[i+1]
    temperature = alpha * 273 + Texp[i] + (z_km - zexp[i]) / (zexp[i + 1] - zexp[i]) * (Texp[i + 1] - Texp[i])

    return temperature

N= 1000
zmax=100.0e3
dz=zmax / (N-1)
zatm = np.array([k*dz for k in range(N)])
Tatm = np.array([T(zatm[k],'C') for k in range(N)])

# Tracer le graphique
plt.figure(figsize=(6,8))  # Un format vertical
plt.plot(Tatm, zatm/1000, label='Température interpolée')  # T sur x, z sur y
plt.scatter(Texp, zexp, color='red', label='Données expérimentales')
plt.xlabel("Température (°C)")
plt.ylabel("Altitude (km)")
plt.title("Profil de température de l'atmosphère")
plt.grid(True)
plt.legend()
plt.show()