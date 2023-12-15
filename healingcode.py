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

    def chat_miaule(self):
        print("Miaou!")

class Pharmacie:
    def __init__(self):
        self.prix_des_traitements = {
            "ctrl+maj+f": 60,
            "saveOnFocusChange": 100,
            "CheckLinkRelation": 35,
            "Ventoline": 40,
            "f12+doc": 20
        }

    def vendre_medicament(self, traitement, patient):
        if patient.argent >= self.prix_des_traitements[traitement]:
            patient.payer(self.prix_des_traitements[traitement])
            patient.prendre_medicament(traitement)
            print(f"{patient.nom} a acheté le traitement {traitement}.")
        else:
            patient.etat_de_sante = "mort"
            print(f"{patient.nom} n'a pas assez d'argent pour le traitement et est maintenant mort.")

def simuler_code_de_guerison(patients, docteur, pharmacie):
    for patient in patients:
        # Le patient va chez le médecin
        patient.se_rendre_a("cabinet du docteur")
        traitement = docteur.diagnostiquer(patient)
        docteur.recevoir_paiement(50)
        patient.payer(50)

        # Le chat du docteur miaule
        docteur.chat_miaule()
        time.sleep(2)  # Le chat miaule toutes les deux secondes

        # Le patient va à la pharmacie
        patient.se_rendre_a("pharmacie")
        pharmacie.vendre_medicament(traitement, patient)

        # Afficher l'état du patient
        print(f"Statut de {patient.nom}: Santé - {patient.etat_de_sante}, Argent - {patient.argent}€, Traitement - {patient.poche}\n")

# Création des instances et exécution de la simulation
donnees_patients = [
    Patient("Marcus", "mal indenté", 100),
    Patient("Optimus", "unsave", 200),
    Patient("Sangoku", "404", 80),
    Patient("DarthVader", "azmatique", 110),
    Patient("Semicolon", "syntaxError", 60)
]

docteur = Docteur()
pharmacie = Pharmacie()

simuler_code_de_guerison(donnees_patients, docteur, pharmacie)
