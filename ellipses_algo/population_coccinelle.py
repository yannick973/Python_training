#Léa étudie l’évolution d’une population de coccinelles dans son département. 
# Elle constate que cette population augmente de 5 % tous les ans et que 50 coccinelles meurent chaque année. 
# Cette année, on a recensé 3 000 individus.

#Niveau 1 : ecrire un programme qui permet de déterminer la population de coccinelle au bout de n années


# def population(pop_initiale, taux_croissance, mortalite, nb_annees):
#     pop = pop_initiale
#     for i in range(nb_annees):
#         pop = pop * (1 + taux_croissance/100) - mortalite
#         print(f"Année {i} : {pop:.0f} coccinelles")
#     return pop

# # Exemple d'utilisation :
# pop_initiale = 3000
# taux_croissance = 5   # 5 %
# mortalite = 50
# nb_annees = 10

# resultat = population(pop_initiale, taux_croissance, mortalite, nb_annees)
# print(f"Au bout de {nb_annees} ans, la population sera d’environ {resultat:.0f} coccinelles.")

# Niveau 2 : modifier le programme pour savoir au bout de combien d'années la population augmente 
# d'au moins 20%


# Niveau 2 : modifier le programme pour savoir au bout de combien d'années la population augmente d'au moins 20 %

# pop_initiale = 3000
# taux_croissance = 5
# mortalite = 50

# pop = pop_initiale
# annee = 0

# while pop < 1.2 * pop_initiale:  # 20 % d'augmentation
#     pop = pop * (1 + taux_croissance / 100) - mortalite
#     annee += 1

# print(f"La population a augmenté d'au moins 20 % après {annee} années.")
# print(f"Population à ce moment-là : {pop:.0f} coccinelles")

#variante avec une fonction 
# def nb_annees_augmentation(pop_initiale, taux_croissance, mortalite, augmentation):
#     """
#     Calcule au bout de combien d'années la population a augmenté d'au moins un certain pourcentage.

#     pop_initiale : population de départ
#     taux_croissance : pourcentage d'augmentation annuelle (ex : 5 pour 5 %)
#     mortalite : nombre d'individus qui meurent chaque année
#     augmentation : pourcentage visé (ex : 20 pour +20 %)
#     """
    
#     pop = pop_initiale
#     annee = 0

#     while pop < (1 + augmentation / 100) * pop_initiale:
#         pop = pop * (1 + taux_croissance / 100) - mortalite
#         annee += 1

#     return annee, pop  # on renvoie les deux valeurs


# # === Appel "classique" de la fonction ===
# resultat = nb_annees_augmentation(3000, 5, 50, 20)

# # on récupère les deux valeurs renvoyées
# annees, pop_finale = resultat

# print(f"La population a augmenté d'au moins 20 % après {annees} années.")
# print(f"Population à ce moment-là : {pop_finale:.0f} coccinelles.")

#Niveau 3 : au bout de combien d'années, la population de coccinelles aura-t-elle doublé ?

def doublement(pop_initiale, taux_croissance, mortalite):
       
    pop = pop_initiale
    annee = 0

    while pop < 2 * pop_initiale:
        pop = pop * (1 + taux_croissance / 100) - mortalite
        annee += 1

    return annee, pop  # on renvoie les deux valeurs


# === Appel "classique" de la fonction ===
resultat = doublement(3000, 5, 50)

# on récupère les deux valeurs renvoyées
annees, pop_finale = resultat

print(f"La population aura doublé après {annees} années.")
print(f"Population à ce moment-là : {pop_finale:.0f} coccinelles.")
