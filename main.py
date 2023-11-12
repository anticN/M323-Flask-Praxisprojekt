from flask import Flask, jsonify, request
from student import Student, Absence

students = [Student(1, "Lambo", 18, "IM21A", {"IT": 5.5, "Mathe": 4.5, "Deutsch": 5}),
            Student(2, "Maroc", 17, "IM21A", {"IT": 3.5, "Mathe": 4, "Deutsch": 3.5}),
            Student(3, "Miro", 19, "IM21B", {"IT": 3.5, "Mathe": 4, "Deutsch": 4.5}),
            Student(4, "Mero", 18, "IM21B", {"IT": 5, "Mathe": 5.5, "Deutsch": 6}),
            Student(5, "Moro", 17, "IM21B", {"IT": 4.5, "Mathe": 4.5, "Deutsch": 4}),]


app = Flask(__name__)


@app.route('/')
def index():
    return f"Hallo! Das ist Nikola's Praxisarbeit zum Modul 323"


@app.route('/a1g/<int:student_id>')
def pure_function(student_id):
    """Das ist eine pure Function welche die gesamte Anzahl Absenzen eines Schülers zurückgibt
    :param student_id: die ID des Schülers"""
    total = len(students[student_id-1].excused_absences) + len(students[student_id-1].unexcused_absences)
    return str(total) if total > 0 else f"Keine Absenzen beim Schüler {students[student_id-1].name}"


@app.route('/a1f/<int:student_id>')
def immutable_value(student_id):
    """Das ist eine Funktion die einen unveränderlichen Wert zurückgibt. Der Wert ist ein Tupel mit Absenzen eines
    Schülers."""
    absence_tuple = (students[student_id-1].excused_absences, students[student_id-1].unexcused_absences)
    print(absence_tuple)
    return str(absence_tuple)


@app.route('/a1e/<int:student_id>')
def different_problems():
    pass


@app.route('/b1gfe/<int:student_id>')
def avg_grades(student_id):
    """
    :param student_id:
    :return: Den Durchschnitt der Noten eines Schülers
    """
    avg = sum(students[student_id-1].grades.values()) / len(students[student_id-1].grades.values())
    return f"Der Durchschnitt der Noten von {students[student_id-1].name} ist {avg}"


def filter_by_grades(students, grade):
    new_list = []
    for student in students:
        if avg_grades(student.student_id) >= grade:
            new_list.append(student)
    return new_list


def filter_by_class(students, class_name):
    """
    :param students: Liste der Studenten
    :param class_name: Klasse nach der gefiltert werden soll
    :return: Neue gefilterte Liste
    """
    new_list = []
    for student in students:
        if student.student_class == class_name:
            new_list.append(student)
    return new_list


@app.route('/b2g/<filter_func>/<filter_value>')
def filter_students(filter_func, filter_value):
    """
    :param students: Die Liste der Studenten
    :param filter_func: Die Funktion mit der gefiltert werden soll
    :param filter_value: Der Wert nach dem gefiltert werden soll
    :return: Die gefilterte Liste
    """
    if filter_func == "filter_by_grades":
        filter_func = filter_by_grades(students, filter_value)
        print(filter_func)
        return str(filter_func)
    elif filter_func == "filter_by_class":
        filter_func = filter_by_class(students, filter_value)
        return str(filter_func)
    else:
        return "Falsche Funktion"


# Funktion zur Anzeige von Schülern
def display_students(action_function):
    result = []
    for student in students:
        result.append(action_function(student))
    return result


# Eine Aktion, um den Namen eines Schülers anzuzeigen
def display_name(student):
    return f"Name: {student.name}"


# Eine Aktion, um das Alter eines Schülers anzuzeigen
def display_age(student):
    return f"Alter: {student.age}"

# Route zur Anzeige von Schülern nach Namen
@app.route('/b2gf/display_names')
def display_names():
    student_names = display_students(display_name)
    return student_names

# Route zur Anzeige von Schülern nach Alter
@app.route('/b2gf/display_ages')
def display_ages():
    student_ages = display_students(display_age)
    return student_ages



if __name__ == '__main__':
    students[0].add_excused_absence("Krank")
    students[0].add_unexcused_absence("Zu spät")
    students[0].add_unexcused_absence("Verschlafen")
    students[1].add_excused_absence("Militär")
    print("Everything done to start flask")
    app.run(debug=True)
