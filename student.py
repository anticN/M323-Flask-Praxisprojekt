import datetime

from absence import Absence


class Student:
    def __init__(self, student_id, name, age, student_class, grades):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.student_class = student_class
        self.grades = grades
        self.excused_absences = []
        self.unexcused_absences = []

    def __str__(self):
        return f"Student: student_id: {self.student_id}, name: {self.name}, age: {self.age}, student_class: {self.student_class}, grades: {self.grades}"

    def __repr__(self):
        return f"Student: student_id: {self.student_id}, name: {self.name}, age: {self.age}, student_class: {self.student_class}, grades: {self.grades}"

    def add_excused_absence(self, reason):
        self.excused_absences.append(Absence(datetime.datetime.now(), reason, self.student_id, True))

    def add_unexcused_absence(self, reason):
        self.unexcused_absences.append(Absence(datetime.datetime.now(), reason, self.student_id))

