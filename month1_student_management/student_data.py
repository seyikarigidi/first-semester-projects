import json
import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "students.json")
students = []

def load_students():
    global students
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            students = json.load(f)
    else:
        students = []

def save_students():
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    save_students()

def view_students():
    if not students:
        print("No students available.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']:.2f}")

def get_average_grade():
    if not students:
        return 0.0
    total = sum(student["grade"] for student in students)
    return total / len(students)
    pass

