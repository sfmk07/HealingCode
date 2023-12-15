import time

class Patient:
    def __init__(self, nom, maladie, argent):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent
        self.poche = "vide"
        self.etat_de_sante = "malade"

    def se_rendre_a(self, endroit):
        print(f"{self.nom} se rend à {endroit}.")

    def prendre_medicament(self, medicament):
        self.poche = medicament
        self.etat_de_sante = "guéri"

    def payer(self, montant):
        self.argent -= montant
        print(f"{self.nom} a payé {montant}€.")