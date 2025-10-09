#dans le cadre d'une sortie scolaire, 28 enfants visitent la tour de contrôle.
#ils portent des brassard numérotés de 1 à 28.
# un tableau de commande permet l'allumage de 196 feux de signalisation pour les différentes pistes d'atterissage.
#afin de passer le temps, les enfants appuient à tour de rôle sur les interrupteurs qui acctionnent les feux
#l'enfant 1 appuie sur les interrupteurs multiple de 1
#l'enfant 2 appuie sur les interrupteurs multiples de 2
#l'enfant 3 sur les interrupteurs multiples de 3
# etc (tous les feux étant initialement éteints)

#Niveau 1 : faire un programme qui permet d'afficher l'état des feux après le passage des 28 enfants.
# cad affiché un vecteur qui indique l'état des feux : 0 pour éteint et 1 pour allumé
# afficher aussi le nb de feux allumés

# import numpy as np

# go=input("Appuyez sur une touche pour continuer")
# feux = np.zeros(196)
# for enfants in range(1,29):
#     for interrupteur in range(1,197):
#         if interrupteur%enfants==0:
#             if feux[interrupteur-1]==0:
#                 feux[interrupteur-1]=1
#             else:
#                 feux[interrupteur-1]=0
# somme=sum(feux)

# print(f"l'état des feux après le passage des enfants est {feux}")
# print(f"le nb de feux allumés est {somme}")

#version avec liste et modification des feux plus rapide
# feux = [0] * 196

# for enfant in range(1, 29):
#     for interrupteur in range(1, 197):
#         if interrupteur % enfant == 0:
#             feux[interrupteur - 1] = 1 - feux[interrupteur - 1]

# somme = sum(feux)

# print(f"État final des feux : {feux}")
# print(f"Nombre de feux allumés : {somme}")


#une fonction possible pour pouvoir changer rapidement le nb de feux et le nb d'enfants
# def allumage_feux(nb_feux=196, nb_enfants=28):
#     feux = [0] * nb_feux
#     for enfant in range(1, nb_enfants + 1):
#         for interrupteur in range(enfant, nb_feux + 1, enfant):
#             feux[interrupteur - 1] = 1 - feux[interrupteur - 1]
#     return feux, sum(feux)

# resultat = allumage_feux(196,28)
# print(resultat)

#Niveau 2 : Modifier le programme afin qu'il soit possible de choisir le nb d'enfants et le nb de feux de signalisation
#On veut aussi la liste des numéros des feux allumés

# go=input("Appuyez sur une touche pour continuer")

# def allumage_feux(nb_feux=196, nb_enfants=28):
#     feux = [0] * nb_feux
#     for enfant in range(1, nb_enfants + 1):
#         for interrupteur in range(enfant, nb_feux + 1, enfant):
#             feux[interrupteur - 1] = 1 - feux[interrupteur - 1]

#     nb_allumes = sum(feux)
#     feux_allumes = [i + 1 for i, etat in enumerate(feux) if etat == 1]

#     return feux, nb_allumes, feux_allumes

# etat, total, allumes = allumage_feux(196,196)

# print(f"Nombre total de feux allumés : {total}")
# print(f"Numéros des feux allumés : {allumes}")

#Niveau 3 : lorsque le nb de feux est 196, représenter le nuage de points du nb de feux allumés après 
# le passage des enfants (nb_enfants). Afin de limiter les temps de calcul, on prendra des multiples de 28
# pour le nb d'enfants

# import matplotlib.pyplot as plt

# def allumage_feux(nb_feux=196, nb_enfants=28):
#     """
#     Simule le passage des enfants appuyant sur les interrupteurs.
#     Retourne le nombre total de feux allumés à la fin.
#     """
#     feux = [0] * nb_feux
#     for enfant in range(1, nb_enfants + 1):
#         for interrupteur in range(enfant, nb_feux + 1, enfant):
#             feux[interrupteur - 1] = 1 - feux[interrupteur - 1]
#     return sum(feux)  # on retourne uniquement le total


# # --- Programme principal ---
# nb_feux = 196
# valeurs_nb_enfants = list(range(28, nb_feux + 1, 28))  # 28, 56, 84, ..., 196
# resultats = []  # pour stocker le nb de feux allumés

# for nb_enfants in valeurs_nb_enfants:
#     nb_allumes = allumage_feux(nb_feux, nb_enfants)
#     resultats.append(nb_allumes)
#     print(f"{nb_enfants} enfants → {nb_allumes} feux allumés")

# # --- Tracé du graphique ---
# plt.figure(figsize=(8,5))
# plt.scatter(valeurs_nb_enfants, resultats, color='blue', s=60)
# plt.plot(valeurs_nb_enfants, resultats, linestyle='--', alpha=0.6)
# plt.title("Nombre de feux allumés selon le nombre d'enfants")
# plt.xlabel("Nombre d'enfants")
# plt.ylabel("Nombre de feux allumés")
# plt.grid(True)
# plt.ylim(bottom=0)
# plt.show()


import matplotlib.pyplot as plt

def allumage_feux(nb_feux=196, nb_enfants=28):
    """
    Simule le passage des enfants appuyant sur les interrupteurs.
    Retourne le nombre total de feux allumés à la fin.
    """
    feux = [0] * nb_feux
    for enfant in range(1, nb_enfants + 1):
        for interrupteur in range(enfant, nb_feux + 1, enfant):
            feux[interrupteur - 1] = 1 - feux[interrupteur - 1]
    return sum(feux)  # on retourne uniquement le total


# --- Programme principal ---
nb_feux = 196
valeurs_nb_enfants = range(1, nb_feux + 1)  # 1 à 196
resultats = []

for nb_enfants in valeurs_nb_enfants:
    nb_allumes = allumage_feux(nb_feux, nb_enfants)
    resultats.append(nb_allumes)

# --- Tracé du graphique ---
plt.figure(figsize=(10,6))
plt.scatter(valeurs_nb_enfants, resultats, color='blue', s=5)
plt.plot(valeurs_nb_enfants, resultats, linestyle='--', alpha=0.1)
plt.title("Nombre de feux allumés selon le nombre d'enfants")
plt.xlabel("Nombre d'enfants")
plt.ylabel("Nombre de feux allumés")
plt.grid(True)
plt.ylim(bottom=0)  # axe Y commence à 0
plt.show()


