class Person:
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_naissance

class Student(Person):
    def __init__(self, nom, prenom, date_naissance, code_massar):
        super(Student, self).__init__(nom, prenom, date_naissance)
        self.code_massar = code_massar

    def to_dict(self):
        """تحويل بيانات الطالب إلى قاموس لحفظها في JSON"""
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_de_naissance,
            "code_massar": self.code_massar
        }

class Matiere:
    def __init__(self, nom_matiere, code_matiere):
        self.nom_matiere = nom_matiere
        self.code_matiere = code_matiere

    def to_dict(self):
        return {
            "nom_matiere": self.nom_matiere,
            "code_matiere": self.code_matiere
        }

class Absence:
    def __init__(self, date, student_code, code_matiere, justification="Non justifiée"):
        self.date = date
        self.student_code = student_code  # نستخدم الكود لربطه بملف الطلاب
        self.code_matiere = code_matiere # نستخدم كود المادة
        self.justification = justification

    def to_dict(self):
        return {
            "date": self.date,
            "student_code": self.student_code,
            "code_matiere": self.code_matiere,
            "justification": self.justification
        }