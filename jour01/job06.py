class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficher_age(self):
        print(f"L'age de l'animal {self.age} ans")

    def vieillir(self):
        self.age += 1
    
    def nommer(self, prenom):
        self.prenom = prenom
    
    def afficher_prenom(self):
        print(f"L'animal se nomme {self.prenom}")

mon_animal = Animal()
mon_animal.afficher_age()

mon_animal.vieillir()
mon_animal.afficher_age()

mon_animal.nommer("Atilla")
mon_animal.afficher_prenom()

