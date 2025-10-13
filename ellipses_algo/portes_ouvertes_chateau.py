# les 64 fenetres d'un chateau comportent deux battants (un gauche et un droite).
# il y a 64 visiteurs avec des brassards numérotés de 1 à 64.
# le visiteur 1 doit ouvrir tous les battants gauches des fenetres
# le 2 doit ouvrir tous les battants droits des fenetres dont le numéro est pair.
# le 3 doit ouvrir tous les battants droits fermés dont le numéro est un multiple de 3, 
# et fermer tous les battants gauches ouverts dont le numéro est un multiple de 3
# etc
# il existe donc 4 positions possible pour chaque fenetre
# F : la fenetre est fermée
# G : le battant gauche est ouvert
# D : le battant droit est ouvert
# O : la fenetre est completement ouverte
# à la fin du passage, les visiteurs dont le numéro est egal au numéro de la fenetre completement ouverte
# entre deux fenetres fermées reçoit un cheque cadeau correspondant au numero de son brassard
#au départ toutes les fenetres sont fermées


# Niveau 1 : ecrire un programme qui permet d'afficher l'état des fenetres (F,G,D,O) apres le passage des 64 personnes.

# fenetres = ['F']*64

# def battans_fenetres(visiteurs,numero_fenetre):
#     if visiteurs%2 == 0 :
#         if fenetres[numero_fenetre-1]=='F':
#             fenetres[numero_fenetre-1] =='D'
#             return
#         elif fenetres[numero_fenetre-1]=='G':
#             fenetres[numero_fenetre-1]=='O'
#             return
#         elif fenetres[numero_fenetre-1]=='D':
#             fenetres[numero_fenetre-1]='F'
#             return
#         else : #cas 'O'
#             fenetres[numero_fenetre-1]='G'
#     else :
#         if fenetres[numero_fenetre-1]=='F':
#             fenetres[numero_fenetre-1]='G'
#             return
#         elif fenetres[numero_fenetre-1]=='G':
#             fenetres[numero_fenetre-1]='F'
#             return
#         elif fenetres[numero_fenetre-1]=='D':
#             fenetres[numero_fenetre-1]='O'
#             return
#         else :
#             fenetres[numero_fenetre-1]='D'

# for i in range(1,65):
#     for j in range(1,65):
#         if j%i ==0:
#             battans_fenetres(i,j)

# print(f"les états des 64 fenetres sont {fenetres}")


# Les 64 fenêtres sont initialement fermées
fenetres = ['F'] * 64

def battants_fenetres(visiteur, numero_fenetre):
    i = numero_fenetre - 1  # index dans la liste
    etat = fenetres[i]

    if visiteur % 2 == 0:  # visiteur pair : agit sur le battant droit
        if etat == 'F':
            fenetres[i] = 'D'
        elif etat == 'G':
            fenetres[i] = 'O'
        elif etat == 'D':
            fenetres[i] = 'F'
        elif etat == 'O':
            fenetres[i] = 'G'

    else:  # visiteur impair : agit sur le battant gauche
        if etat == 'F':
            fenetres[i] = 'G'
        elif etat == 'G':
            fenetres[i] = 'F'
        elif etat == 'D':
            fenetres[i] = 'O'
        elif etat == 'O':
            fenetres[i] = 'D'


# Chaque visiteur agit sur les fenêtres multiples de son numéro
for visiteur in range(1, 65):
    for num_fenetre in range(1, 65):
        if num_fenetre % visiteur == 0:
            battants_fenetres(visiteur, num_fenetre)

# Affichage final
# print("Les états des 64 fenêtres sont :")
# for i, etat in enumerate(fenetres, start=1):
#     print(f"Fenêtre {i:2d} : {etat}")

print(fenetres)


#Une version plus concise avec des dictionnaires
fenetres = ['F'] * 64

# Dictionnaires de transitions
transition_pair = {'F': 'D', 'G': 'O', 'D': 'F', 'O': 'G'}
transition_impair = {'F': 'G', 'G': 'F', 'D': 'O', 'O': 'D'}

def battants_fenetres(visiteur, numero_fenetre):
    i = numero_fenetre - 1
    etat = fenetres[i]
    fenetres[i] = transition_pair[etat] if visiteur % 2 == 0 else transition_impair[etat]

for visiteur in range(1, 65):
    for num_fenetre in range(1, 65):
        if num_fenetre % visiteur == 0:
            battants_fenetres(visiteur, num_fenetre)

print(fenetres)


#avec une struture conditionnelle ternaire

fenetres = ['F'] * 64

def battants_fenetres(visiteur, numero_fenetre):
    i = numero_fenetre - 1
    etat = fenetres[i]

    if visiteur % 2 == 0:  # visiteur pair → agit sur le battant droit
        fenetres[i] = (
            'D' if etat == 'F' else
            'O' if etat == 'G' else
            'F' if etat == 'D' else
            'G'
        )
    else:  # visiteur impair → agit sur le battant gauche
        fenetres[i] = (
            'G' if etat == 'F' else
            'F' if etat == 'G' else
            'O' if etat == 'D' else
            'D'
        )

# Parcours des 64 visiteurs
for visiteur in range(1, 65):
    for num_fenetre in range(1, 65):
        if num_fenetre % visiteur == 0:
            battants_fenetres(visiteur, num_fenetre)

# Affichage du vecteur final
print(fenetres)
