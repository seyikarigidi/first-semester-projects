# Entry point for the student management system
from student_data import students, add_student, view_students, get_average_grade, load_students, save_students

print("📚 Welcome to the Student Record System")

while True:
    print("\n1. Add student\n2. View students\n3. Get average grade\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print(f"📊 Average Grade: {get_average_grade():.2f}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")