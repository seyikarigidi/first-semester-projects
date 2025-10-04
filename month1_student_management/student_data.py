students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    pass

def view_students():
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    """
    TODO: Loop through the students list and print each student's info.
    """
    pass

def get_average_grade():
    if not students:
        return 0.0
    total = sum(student["grade"] for student in students)
    return total / len(students)
    """
    TODO: Return the average grade of all students.
    """
    pass

