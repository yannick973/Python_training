#des loups, des moutons et serpents vivent sur une ile.
# chaque jour il y a le même enchainement
# chaque loup tue un Mouton 
# chaque mouton tue un serpent
# chaque serpent tue un Loup 
# le 1er jour il y a 322 loups, 567 moutons, 427 serpents

#Niveau 1 : combien d'animaux restent-ils sur l'ile le 5eme jour ?
#l=322
#m=567
#s=427
# nb_animaux=input(" Donnez le nb de loups, moutons, serpents ([l,m,s]) :")
# nb_animaux=eval(nb_animaux)
# l =nb_animaux[0]
# m=nb_animaux[1]
# s=nb_animaux[2]
# nb_jours = int(input("Entrez le nb de jours :"))

# for i in range(nb_jours):
#     m = m - l 
#     s = s - m 
#     l = l - s 
#     print(f"Jour {i+1} : loups={l}, moutons={m}, serpents={s}")

# Niveau 2 : il y a l = 15 681 566, m=27519230,s=20773652
#déterminer le nb de jours k tel qu'à l'aube du k+1 jour il reste moins de 200 moutons sur l'ile

# l=15681566
# m=27519230
# s=20773652
# k=0

# while m>200 and l>0 and s>0 :
#     m = m - l 
#     s = s - m 
#     l = l - s 
#     k +=1
#     print(f"Jour {k} : loups={l}, moutons={m}, serpents={s}")

# niveau 3 : à l'aube du 7eme jour, il ne reste plus qu'1 loup, 2 moutons et 3 serpents. 
# Combien y avait il d'animaux au départ ?


l=1
m=2
s=3
k=0
for i in range(6):
    l = l +s 
    s = s + m 
    m = m + l
    k -= 1
    print(f"Jour {k} : loups={l}, moutons={m}, serpents={s}")