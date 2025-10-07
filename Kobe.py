import matplotlib.pyplot as plt
import numpy as np

# Demander les coefficients à l'utilisateur
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Vérifier que ce n'est pas une droite
if a == 0:
    print("Ce n'est pas un polynôme du second degré (a ≠ 0).")
else:
    # Définir la fonction polynomiale
    def f(x):
        return a*x**2 + b*x + c

    # Calcul du sommet de la parabole pour centrer la fenêtre autour
    x_sommet = -b / (2*a)
    x_min = x_sommet - 10
    x_max = x_sommet + 10

    # Générer les valeurs de x
    x = np.linspace(x_min, x_max, 400)
    y = f(x)

    # Tracer la courbe
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.title("Graphique du polynôme du second degré")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)  # Axe x
    plt.axvline(0, color='black', linewidth=0.5)  # Axe y
    plt.legend()
    plt.show()
