# suite de Syracuse
# a partir d'un nombre entier, plus grand que zero, 
# s'il est pair on le divise par 2
# s'il est impair, on le multiplie par 3 et on ajoute 1
# on arrête dès que la suite vaut 1 car cela enchainera sur un cycle trivial 1,4,2,1,4,2,1 ...

# Niveau 1 : ecrire un programme qui affiche la suite de Syracuse à partir d'un nombre entier n donné

def syracuse(n):
    """Retourne la suite de Syracuse à partir de n."""
    suite = [n]  # on inclut le nombre de départ
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # division entière
        else:
            n = 3 * n + 1
        suite.append(n)
    return suite

# Lecture de l'utilisateur
nombre = int(input("Entrez un nombre entier positif n : "))
if nombre <= 0:
    print("Le nombre doit être supérieur à zéro.")
else:
    L = syracuse(nombre)
    print(f"La suite de Syracuse du nombre {nombre} est : {L}")

