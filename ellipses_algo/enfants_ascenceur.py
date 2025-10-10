# dans le cadre d'une sortie scolaire, 14 enfants visitent une tour qui se trouve proche de leur ecole.
# ils ont des brassards de 1 à 14
# cette tour à 49 étages et est équipé d'ascenceurs pouvant contenir 50 personnes.
# chaque ascenceur a un panneau de commande avec 49 boutons poussoirs qui permettent d'accéder aux étages
# si on appuie une fois sur un bouton, celui-ci s'allume et l'étage est selectionné
# si on rappuie sur le même bouton, cela n'a aucun effet
# si on appuie cela éteint le bouton
# chaque enfant appuie sur les boutons multiples de son brassard

# Niveau 1 : ecrire un programme qui affiche l'état des boutons après le passage des 14 enfants +
# le nb de boutons allumés

# #Initialisation : 49 boutons (étages)
# etages = [0] * 49
# presses = [0] * 49  # compteur d'appuis pour chaque bouton

# # Les 14 enfants appuient chacun sur les multiples de leur brassard
# for enfant in range(1, 15):
#     for bouton in range(1, 50):
#         if bouton % enfant == 0:
#             presses[bouton - 1] += 1  # on compte chaque appui

# # Détermination de l'état final des boutons
# for i in range(49):
#     n = presses[i]
#     if n % 3 == 1 or n % 3 == 2:
#         etages[i] = 1
#     else:
#         etages[i] = 0

# # Comptage des étages allumés
# somme = sum(etages)

# # Affichage des résultats
# print(f"État final des étages : {etages}")
# print(f"Nombre d'étages sélectionnés : {somme}")

# # (optionnel) affichage des numéros d’étages allumés
# etages_allumes = [i + 1 for i, etat in enumerate(etages) if etat == 1]
# print(f"Étages sélectionnés : {etages_allumes}")


# voici la version du livre

# import numpy as np

# # Initialisation du panneau de boutons
# global bp
# bp = np.zeros(49)

# # Fonction pour appuyer sur un bouton
# def boutonpanneau(p):
#     global bp #le mot-clé global sert à dire à la fonction : “Je veux utiliser la variable bp qui est définie à l’extérieur de la fonction, au lieu de créer une nouvelle variable locale.”
#     if bp[p-1] == 2:
#         bp[p-1] = 0
#     else:
#         bp[p-1] = bp[p-1] + 1

# # Fonction pour compter le nombre d'étages sélectionnés
# def nb_etages():
#     y = 0
#     for j in range(0,49):
#         if bp[j] != 0:
#             y += 1
#     return y

# # Boucle pour chaque enfant
# for e in range(1,15):
#     for k in range(1,50):
#         if k % e == 0:
#             boutonpanneau(k)

# # Résultats
# nume = nb_etages() #toutes les valeurs différentes de 0 compte pour 1 sur le nb d'étages sélectionnés
# print("État final des boutons :", bp)
# print("Nombre d'étages sélectionnés :", nume)

# # Optionnel : afficher les numéros d'étages allumés
# etages_allumes = [i+1 for i, etat in enumerate(bp) if etat != 0]
# print("Étages sélectionnés :", etages_allumes)


# Niveau 2 : modifier le programme afin qu'il soit possible de choisir le nb d'enfants et le nb de boutons
# on doit aussi avoir la liste des étages non sélectionnés
# tester le programme pour enfants = 49 et boutons =49, quelle remarque peut-on faire à propos 
# des étages non sélectionnés

# def simulation_etages(nb_enfants=14, nb_boutons=49):
#     # Initialisation
#     etages = [0] * nb_boutons
#     presses = [0] * nb_boutons  # compteur d'appuis pour chaque bouton

#     # Les enfants appuient sur les multiples de leur brassard
#     for enfant in range(1, nb_enfants + 1):
#         for bouton in range(1, nb_boutons + 1):
#             if bouton % enfant == 0:
#                 presses[bouton - 1] += 1

#     # Détermination de l'état final des boutons
#     for i in range(nb_boutons):
#         n = presses[i]
#         if n % 3 == 1 or n % 3 == 2:
#             etages[i] = 1
#         else:
#             etages[i] = 0

#     # Comptage des étages allumés
#     somme = sum(etages)

#     # Listes des étages allumés et non sélectionnés
#     etages_allumes = [i + 1 for i, etat in enumerate(etages) if etat == 1]
#     etages_non_selectionnes = [i + 1 for i, etat in enumerate(etages) if etat == 0]

#     # Retour des résultats
#     return etages, somme, etages_allumes, etages_non_selectionnes

# # Exemple d'utilisation
# etages, somme, allumes, non_selectionnes = simulation_etages(nb_enfants=49, nb_boutons=49)
# print(f"Nombre d'étages sélectionnés : {somme}")
# print(f"Étages sélectionnés : {allumes}")
# print(f"Étages non sélectionnés : {non_selectionnes}")


#Niveau 3 : représenter le nuage de points du nb d'étages sélectionnés après le passage des enfants
# ceci en fonction du nb d'enfants

import matplotlib.pyplot as plt

# Paramètres
nb_boutons = 49
max_enfants = 49

# Listes pour stocker les résultats
nb_enfants_list = []
nb_etages_selectionnes = []

# Boucle sur le nombre d'enfants
for nb_enfants in range(1, max_enfants + 1):
    # Initialisation
    etages = [0] * nb_boutons
    presses = [0] * nb_boutons
    
    # Simulation
    for enfant in range(1, nb_enfants + 1):
        for bouton in range(1, nb_boutons + 1):
            if bouton % enfant == 0:
                presses[bouton - 1] += 1
                
    # Calcul des états finaux
    for i in range(nb_boutons):
        n = presses[i]
        if n % 3 == 1 or n % 3 == 2:
            etages[i] = 1
        else:
            etages[i] = 0
    
    # Stockage des résultats
    nb_enfants_list.append(nb_enfants)
    nb_etages_selectionnes.append(sum(etages))

# Tracé du nuage de points
plt.figure(figsize=(10, 5))
plt.scatter(nb_enfants_list, nb_etages_selectionnes, color='blue')
plt.xlabel("Nombre d'enfants")
plt.ylabel("Nombre d'étages sélectionnés")
plt.title("Nombre d'étages sélectionnés en fonction du nombre d'enfants")
plt.grid(True)
plt.ylim(bottom=0)
plt.show()
