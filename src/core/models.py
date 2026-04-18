class person:
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_naissance

class student(person):
    def __init__(self, nom, prenom, date_naissance, code_massar, absences):
        super().__init__(nom, prenom, date_naissance)
        self.date_de_naissance = date_naissance
        self.code_massar = code_massar
        self.absences = absences

class professeur(person):
    def __init__(self, nom, prenom, matiere):
        super().__init__(nom, prenom)
        self.matiere = matiere


