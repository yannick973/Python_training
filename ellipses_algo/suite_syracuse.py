# suite de Syracuse
# a partir d'un nombre entier, plus grand que zero, 
# s'il est pair on le divise par 2
# s'il est impair, on le multiplie par 3 et on ajoute 1
# on arrête dès que la suite vaut 1 car cela enchainera sur un cycle trivial 1,4,2,1,4,2,1 ...

# Niveau 1 : ecrire un programme qui affiche la suite de Syracuse à partir d'un nombre entier n donné

# def syracuse(n):
#     """Retourne la suite de Syracuse à partir de n."""
#     suite = [n]  # on inclut le nombre de départ
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2  # division entière
#         else:
#             n = 3 * n + 1
#         suite.append(n)
#     return suite

# # Lecture de l'utilisateur
# nombre = int(input("Entrez un nombre entier positif n : "))
# if nombre <= 0:
#     print("Le nombre doit être supérieur à zéro.")
# else:
#     L = syracuse(nombre)
#     print(f"La suite de Syracuse du nombre {nombre} est : {L}")

# Niveau 2 : ajouter au programme la durée de vol cad le nb d'entier de la suite qui précède la premiere apparition du nb 1
# et l'altitude maximale, cad la valeur maximale atteinte par l'entier 

# def syracuse(n):
#     """Retourne la suite de Syracuse à partir de n, sa durée de vol et son altitude maximale."""
#     suite = [n]  # on inclut le nombre de départ
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         suite.append(n)
    
#     duree_vol = len(suite) - 1      # nombre d'entiers avant d'atteindre 1
#     altitude_max = max(suite)       # valeur maximale atteinte
#     return suite, duree_vol, altitude_max

# # Lecture de l'utilisateur
# nombre = int(input("Entrez un nombre entier positif n : "))
# if nombre <= 0:
#     print("Le nombre doit être supérieur à zéro.")
# else:
#     suite, duree_vol, altitude_max = syracuse(nombre)
#     print(f"La suite de Syracuse du nombre {nombre} est : {suite}")
#     print(f"Durée de vol : {duree_vol}")
#     print(f"Altitude maximale : {altitude_max}")

# Niveau 3 : déterminer l'entier n compris entre 77 000 et 78 000 qui atteint l'altitude maximale. 
# déterminer aussi la durée de vol de ce nombre

# def syracuse(n):
#     """Retourne la suite de Syracuse à partir de n, sa durée de vol et son altitude maximale."""
#     suite = [n]
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         suite.append(n)
#     duree_vol = len(suite) - 1
#     altitude_max = max(suite)
#     return suite, duree_vol, altitude_max

# # Recherche de l'entier atteignant l'altitude maximale
# altitude_max_globale = 0
# nombre_max = 0
# duree_vol_max = 0

# for n in range(77000, 78001):
#     _, duree_vol, altitude_max = syracuse(n)
#     if altitude_max > altitude_max_globale:
#         altitude_max_globale = altitude_max
#         nombre_max = n
#         duree_vol_max = duree_vol

# print(f"L'entier entre 77 000 et 78 000 atteignant l'altitude maximale est : {nombre_max}")
# print(f"Altitude maximale : {altitude_max_globale}")
# print(f"Durée de vol de ce nombre : {duree_vol_max}")


# #Une version optimisée pour utiliser moins de mémoire
# def syracuse_info(n):
#     """
#     Retourne la durée de vol et l'altitude maximale de la suite de Syracuse à partir de n.
#     Version optimisée : ne stocke pas la suite entière.
#     """
#     duree_vol = 0
#     altitude_max = n
#     x = n
#     while x != 1:
#         if x % 2 == 0:
#             x = x // 2
#         else:
#             x = 3 * x + 1
#         duree_vol += 1
#         if x > altitude_max:
#             altitude_max = x
#     return duree_vol, altitude_max

# # Recherche de l'entier atteignant l'altitude maximale
# altitude_max_globale = 0
# nombre_max = 0
# duree_vol_max = 0

# for n in range(77000, 78001):
#     duree_vol, altitude_max = syracuse_info(n)
#     if altitude_max > altitude_max_globale:
#         altitude_max_globale = altitude_max
#         nombre_max = n
#         duree_vol_max = duree_vol

# print(f"L'entier entre 77 000 et 78 000 atteignant l'altitude maximale est : {nombre_max}")
# print(f"Altitude maximale : {altitude_max_globale}")
# print(f"Durée de vol de ce nombre : {duree_vol_max}")


#ajout d'élément pour estimer le temps de calcul et la mémoire utilisée
# import time
# import tracemalloc

# def syracuse_info(n):
#     duree_vol = 0
#     altitude_max = n
#     x = n
#     while x != 1:
#         if x % 2 == 0:
#             x = x // 2
#         else:
#             x = 3 * x + 1
#         duree_vol += 1
#         if x > altitude_max:
#             altitude_max = x
#     return duree_vol, altitude_max

# # Démarrage du suivi du temps et de la mémoire
# start_time = time.time()
# tracemalloc.start()

# # Recherche de l'entier atteignant l'altitude maximale
# altitude_max_globale = 0
# nombre_max = 0
# duree_vol_max = 0

# for n in range(77000, 78001):
#     duree_vol, altitude_max = syracuse_info(n)
#     if altitude_max > altitude_max_globale:
#         altitude_max_globale = altitude_max
#         nombre_max = n
#         duree_vol_max = duree_vol

# # Fin du suivi du temps et de la mémoire
# current, peak = tracemalloc.get_traced_memory()
# end_time = time.time()
# tracemalloc.stop()

# print(f"L'entier entre 77 000 et 78 000 atteignant l'altitude maximale est : {nombre_max}")
# print(f"Altitude maximale : {altitude_max_globale}")
# print(f"Durée de vol de ce nombre : {duree_vol_max}")

# print(f"\nTemps de calcul : {end_time - start_time:.4f} secondes")
# print(f"Usage mémoire : {current / 1024:.2f} Ko (courant), {peak / 1024:.2f} Ko (pic)")


#code pour visualiser les valeurs prises par la suite de Syracuse

import matplotlib.pyplot as plt

def syracuse_suite(n):
    """Retourne la suite complète de Syracuse à partir de n."""
    suite = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        suite.append(n)
    return suite

# Exemple : visualiser la suite pour n = 77000
n = 77000
suite = syracuse_suite(n)

plt.figure(figsize=(10, 6))
plt.plot(range(len(suite)), suite, marker='o', linestyle='-')
plt.title(f"Suite de Syracuse pour n = {n}")
plt.xlabel("Étape (indice dans la suite)")
plt.ylabel("Valeur de la suite")
plt.grid(True)
plt.show()
