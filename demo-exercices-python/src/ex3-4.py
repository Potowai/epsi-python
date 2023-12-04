print("Calcul de l'aire et du perimetre d'un quadrilatere")
longueur = (int(input("Quelle est la longueur?\n")))
largeur = (int(input("Quelle est la largeur\n")))


def calc_aire():
    print("L'aire :", largeur * longueur)


def calc_perimetre():
    print("Le perimetre :", (largeur * 2) + (longueur * 2))


def draw():
    print("Carré de ", longueur, "x", largeur, " :")
    for i in range(0, largeur + 1):
        print("-" * longueur)


if (largeur != 0 and longueur != 0):
    calc_aire()
    calc_perimetre()
    draw()
else:
    print("ERROR : Longueur ou largeur = 0 !")