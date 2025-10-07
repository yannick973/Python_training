#dans un club de vacances, 12 personnes sont assises autour d'une table circulaire où les places sont numérotées
# la personne à la place 12 a 11 coquillages.
# a chaque étape de ce jeu, on choisit au hasard une personne qui dispose d'au moins 2 coquillages
# celle-ci doit alors donner un coquillage à ses deux voisins
# on répète n fois cette étape

# Niveau 1 : écire le programme
# import random

# coquillages = [0]*12 # crée une liste remplie de zeros
# coquillages[11] = 11  # la 12e personne a 11 coquillages

# n = int(input("Combien d'étapes souhaitez-vous ? :"))

# for etape in range(1, n+1):
#     # on cherche toutes les personnes ayant au moins 2 coquillages
#     candidats = [i for i in range(12) if coquillages[i] >= 2]

#     if not candidats:
#         print("Plus personne n’a au moins 2 coquillages. Fin du jeu.")
#         break

#     # choix au hasard d’une personne parmi les candidats
#     i = random.choice(candidats)

#     # indices circulaires des voisins gauche et droit
#     gauche = (i - 1) % 12
#     droite = (i + 1) % 12

#     # transfert de coquillages
#     coquillages[i] -= 2
#     coquillages[gauche] += 1
#     coquillages[droite] += 1
#     # affichage intermédiaire (facultatif)
#     print(f"les candidats sont {candidats}")
#     print(f"Étape {etape:3d} → personne {i+1} donne à {gauche+1} et {droite+1}")
#     print(f"Coquillages : {coquillages}")

# # résultat final
# print("\nRépartition finale :")
# for i, c in enumerate(coquillages, start=1):
#     print(f"Personne {i} : {c} coquillages")

# Niveau 2 : modifie le programme pour qu'il détermine le nb d'étapes nécessaires pour que tous les participants, 
# sauf un seul, aient exactement un coquillage

# import random

# # 12 personnes autour de la table
# coquillages = [0] * 12
# coquillages[11] = 11  # la 12e personne a 11 coquillages

# etape = 0

# while True:
#     # condition d'arrêt : tous sauf un ont exactement 1 coquillage
#     nb_un = sum(1 for c in coquillages if c == 1)
#     nb_autres = len(coquillages) - nb_un
#     if nb_autres == 1:
#         break  # on a atteint l'objectif

#     # on cherche toutes les personnes ayant au moins 2 coquillages
#     candidats = [i for i in range(12) if coquillages[i] >= 2]

#     if not candidats:
#         print("Plus personne n’a au moins 2 coquillages. Fin du jeu.")
#         break

#     # choix au hasard d’une personne parmi les candidats
#     i = random.choice(candidats)

#     # voisins circulaires
#     gauche = (i - 1) % 12
#     droite = (i + 1) % 12

#     # transfert
#     coquillages[i] -= 2
#     coquillages[gauche] += 1
#     coquillages[droite] += 1

#     etape += 1

# print(f"\nNombre d'étapes nécessaires : {etape}")
# print("Répartition finale :")
# for idx, c in enumerate(coquillages, start=1):
#     print(f"Personne {idx} : {c} coquillages")

# Niveau 3 : modifier le programme pour afficher le graphique du nb de personnes sans coquillage 
# en fonction du nombre d'étapes.

import random
import matplotlib.pyplot as plt

# 12 personnes autour de la table
coquillages = [0] * 12
coquillages[11] = 11  # la 12e personne a 11 coquillages

etape = 0

# listes pour stocker l'évolution
etapes_list = []
sans_coquillage = []

while True:
    # compter le nombre de personnes sans coquillage
    nb_sans = sum(1 for c in coquillages if c == 0)
    
    # sauvegarder pour le graphique
    etapes_list.append(etape)
    sans_coquillage.append(nb_sans)
    
    # condition d'arrêt : tous sauf un ont exactement 1 coquillage
    nb_un = sum(1 for c in coquillages if c == 1)
    nb_autres = len(coquillages) - nb_un
    if nb_autres == 1:
        break

    # on cherche toutes les personnes ayant au moins 2 coquillages
    candidats = [i for i in range(12) if coquillages[i] >= 2]

    if not candidats:
        print("Plus personne n’a au moins 2 coquillages. Fin du jeu.")
        break

    # choix aléatoire d’une personne parmi les candidats
    i = random.choice(candidats)

    # voisins circulaires
    gauche = (i - 1) % 12
    droite = (i + 1) % 12

    # transfert de coquillages
    coquillages[i] -= 2
    coquillages[gauche] += 1
    coquillages[droite] += 1

    etape += 1

# affichage du graphique
plt.figure(figsize=(8,5))
plt.plot(etapes_list, sans_coquillage, marker='+')
plt.xlabel("Nombre d'étapes")
plt.ylabel("Nombre de personnes sans coquillage")
plt.title("Évolution des personnes sans coquillage")
plt.grid(True)
plt.show()
