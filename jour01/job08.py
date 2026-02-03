import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def diametre(self):
        return self.rayon * 2

    def aire(self):
        return math.pi * (self.rayon**2)

    def circonference(self):
        return self.diamètre() * math.pi

    def afficherInfo(self):
        print(f"rayon : {self.rayon}")
        print(f"diamètre : {self.diametre()}")
        print(f"aire : {self.aire()}")
        print(f"aire : {self.circonference()}")

cercle1 = Cercle(4)
cercle2 = Cercle(7)

#on affiche les infos des cercles avec les infos de base
cercle1.afficherInfo()
cercle2.afficherInfo()

#on change le rayon et apres on affiche à nouveau

cercle1.changerRayon(9)
cercle2.changerRayon(23)

cercle1.afficherInfo()
cercle2.afficherInfo()


