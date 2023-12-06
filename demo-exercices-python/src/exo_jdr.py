class Personnage():
    def __init__(self, nom, pv, attaque, defense, catchphrase):
        self.nom = nom
        self.pv = pv
        self.pvmax = pv
        self.attaque = attaque
        self.defense = defense
        self.catchphrase = catchphrase

    def attaquer(self, cible):
        cible.pv = (cible.pv + cible.defense) - self.attaque
        print(self.nom + " attaque " + cible.nom + " et lui inflige " + str(self.attaque) + " points de dégâts!")

    def sePresenter(self):
        print("Je m'appelle " + self.nom + ", " + self.catchphrase + "!")


class Guerrier(Personnage):
    def __init__(self, nom, pv, attaque, defense, catchphrase):
        super().__init__(nom, pv, attaque, defense, catchphrase)

    def criDeGuerre(self):
        print(self.catchphrase + " !")


class Mage(Personnage):
    def __init__(self, nom, pv, attaque, defense, catchphrase):
        super().__init__(nom, pv, attaque, defense, catchphrase)
        self.mana = 10

    def lancerSort(self, cible):
        if self.mana >= 1:
            cible.pv -= self.attaque
            self.mana -= 1
            print(self.nom + " lance un sort sur " + cible.nom + " et lui inflige " + str(self.attaque) + " points de dégâts!")
        else:
            print("Pas assez de mana pour lancer le sort!")


class Archer(Guerrier):
    def __init__(self, nom, pv, attaque, defense, catchphrase):
        super().__init__(nom, pv, attaque, defense, catchphrase)

    def tirer(self, cible):
        cible.pv -= self.attaque
        print(self.nom + " tire sur " + cible.nom + " et lui inflige " + str(self.attaque) + " points de dégâts!")


class Clerc(Personnage):
    def __init__(self, nom, pv, attaque, defense, catchphrase):
        super().__init__(nom, pv, attaque, defense, catchphrase)
        self.heal = 2

    def soigner(self, cible):
        cible.pv += self.heal
        print(self.nom + " soigne " + cible.nom + " et lui rend 2 points de vie!")


class Paladin(Guerrier, Clerc):
    def __init__(self, nom, pv, attaque, defense, catchphrase):
        super().__init__(nom, pv, attaque, defense, catchphrase)

# Path: exo_jdr.py
# Création des personnages
guerrier = Guerrier("Guerrier", 10, 3, 1, "Grrrrrr")
mage = Mage("Mage", 5, 5, 1, "Abracadabra")
archer = Archer("Archer", 7, 2, 1, "Pew pew")
paladin = Paladin("Paladin", 8, 2, 1, "Pour la gloire")
clerc = Clerc("Clerc", 6, 1, 1, "Pour le seigneur")

# Créer un combat avec les personnages et afficher le résultat dans la console
guerrier.sePresenter()
mage.sePresenter()
print("Le combat commence !")

while guerrier.pv > 0 and mage.pv > 0:
    guerrier.attaquer(mage)
    mage.lancerSort(guerrier)

    print("PV Guerrier:", guerrier.pv)
    print("PV Mage:", mage.pv)

    if guerrier.pv <= 0:
        print("Le guerrier est mort !")
    elif mage.pv <= 0:
        print("Le mage est mort !")

