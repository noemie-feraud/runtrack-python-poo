class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacement_gauche(self):
        self.x -= 1
    def deplacement_droite(self):
        self.x +=1
    def deplacement_bas(self):
        self.y += 1
    def deplacement_haut(self):
        self.y -= 1
    def position(self):
        return (self.x, self.y)
    def afficher_personnage(self):
        print(f"Le personnage de jeu se situe en position {self.position()}")

joueur = Personnage(0, 0)
joueur.afficher_personnage()

#On déplace notre joueur
joueur.deplacement_droite()
joueur.deplacement_bas()
joueur.deplacement_bas()

#on affiche sa nouvelle position
joueur.afficher_personnage()

#on test les deux autres méthodes
joueur.deplacement_gauche()
joueur.deplacement_gauche()
joueur.deplacement_haut()

#on affiche encore
joueur.afficher_personnage()



