# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
# =============================================================================


def calculate_average(scores):
    """Calculates and returns the average score."""
    total = 0

    for score in scores:
        total += score

    return round(total / len(scores), 2)


def add_student(students):
    """Adds a new student record."""
    name = input("Student name: ")
    student_id = input("Student ID: ")

    num_scores = int(input("How many scores? "))

    scores = []
    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)

    print(f'Student "{name}" added successfully.')


def display_students(students):
    """Displays all student records."""
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n---------------------------------------------------------------")
    print(f"{'Name':20}{'ID':15}{'Scores':20}{'Average'}")
    print("---------------------------------------------------------------")

    for student in students:
        scores_text = ", ".join(str(score) for score in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:20}{student['id']:15}{scores_text:20}{average:.2f}")

    print("---------------------------------------------------------------")


def find_average(students):
    """Finds and displays the average score of a specific student."""
    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            average = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average:.2f}")
            return

    print("Error: Student ID not found.")


def display_menu():
    """Displays the main menu."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            find_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")


# Run the program
main()