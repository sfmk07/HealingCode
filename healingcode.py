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

class Docteur:
    def __init__(self):
        self.nom = "Débogueur"
        self.argent = 0
        self.cabinet = ["chat"]
        self.table_de_diagnostic = {
            "mal indenté": "ctrl+maj+f",
            "unsave": "saveOnFocusChange",
            "404": "CheckLinkRelation",
            "azmatique": "Ventoline",
            "syntaxError": "f12+doc"
        }

    def diagnostiquer(self, patient):
        print(f"Diagnostic pour {patient.nom}: {self.table_de_diagnostic[patient.maladie]}")
        return self.table_de_diagnostic[patient.maladie]

    def recevoir_paiement(self, montant):
        self.argent += montant