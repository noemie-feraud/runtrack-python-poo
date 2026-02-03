class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def valeur_TVA(self):
        return self.prixHT * self.TVA

    def CalculerPrixTTC(self):
        return self.prixHT - self.valeur_TVA()
    
    def afficher_produit(self):
        print(f"Le produit {self.nom} son prix HT est de {self.prixHT}€")
        print(f"La TVA sur ce produit est de {self.valeur_TVA()}€")
        print(f"Le prix TTC de ce produit est de {self.CalculerPrixTTC()}€")
        
    def changer_nom(self, nouveau_nom):
        self.nom = nouveau_nom
        return self.nom

    def changer_prix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
        return self.prixHT
    
notre_produit = Produit("chaise", 56, 0.2)
notre_produit.CalculerPrixTTC()
notre_produit.afficher_produit()

