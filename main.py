import flask
from student import Student, Absence

students = [Student(1, "Lambo", 18, "IM21A", {"IT": 5.5, "Mathe": 4.5, "Deutsch": 3.5}),
            Student(2, "Maroc", 17, "IM21A", {"IT": 4, "Mathe": 5, "Deutsch": 5.5}),
            Student(3, "Miro", 19, "IM21B", {"IT": 3.5, "Mathe": 4, "Deutsch": 4.5}),
            Student(4, "Mero", 18, "IM21B", {"IT": 5, "Mathe": 5.5, "Deutsch": 6})]


app = flask.Flask(__name__)


@app.route('/')
def index():
    return f"Hallo! Das ist Nikola's Praxisarbeit zum Modul 323"


@app.route('/a1g/<int:student_id>')
def pure_function(student_id):
    """Das ist eine pure Function welche die gesamte Anzahl Absenzen eines Schülers zurückgibt
    :param student_id: die ID des Schülers"""
    total = len(students[student_id-1].excused_absences) + len(students[student_id-1].unexcused_absences)
    return str(total) if total > 0 else f"Keine Absenzen beim Schüler {students[student_id-1].name}"


if __name__ == '__main__':
    students[0].add_excused_absence("Krank")
    students[0].add_unexcused_absence("Zu spät")
    students[1].add_excused_absence("Militär")
    app.run(debug=True)
