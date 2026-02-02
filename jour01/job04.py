class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom 
    def se_presenter(self):
        return f"Je suis {self.prenom} {self.nom}"
personne1 = Personne("Abdallah", "Antuat")
personne2 = Personne("Ahamada", "Assmine")
personne3 = Personne("Feraud", "Noemie")

print(personne1.se_presenter())
print(personne2.se_presenter())
print(personne3.se_presenter())
