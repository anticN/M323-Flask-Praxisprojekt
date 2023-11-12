class Absence:
    def __init__(self, date, reason, student_id, is_excused=False):
        self.date = date
        self.reason = reason
        self.student_id = student_id
        self.is_excused = is_excused

    def __str__(self):
        return f"Absence: date: {self.date} reason: {self.reason} student_id: {self.student_id} is_excused: {self.is_excused}"
