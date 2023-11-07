class Absence:
    def __init__(self, date, reason, student_id, is_excused=False):
        self.date = date
        self.reason = reason
        self.student_id = student_id
        self.is_excused = is_excused
