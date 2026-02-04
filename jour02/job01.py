class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def afficher_longueur(self):
        return self.__longueur

    def afficher_largeur(self):
        return self.__largeur

    def changer_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def changer_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

forme = Rectangle(10, 5)
print(forme.afficher_longueur())
print(forme.afficher_largeur())

forme.changer_longueur(20)
forme.changer_largeur(10)

print(forme.afficher_longueur())
print(forme.afficher_largeur())