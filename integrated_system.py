students = []

# These sets are maintained from the student records.
departments = set()
all_subjects = set()
student_clubs = set()


def roll_tuple(value):
    """Store a roll number as a one-item tuple."""
    return (value.strip(),)


def registration_tuple(value):
    """Store a registration number as a one-item tuple."""
    return (value.strip(),)


def find_student(roll_number):
    """Return the student dictionary matching the roll number."""
    target = roll_tuple(roll_number)

    for student in students:
        if student["roll_number"] == target:
            return student

    return None


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def input_email():
    while True:
        email = input("Enter email ID: ").strip().lower()

        if "@" in email and "." in email.split("@")[-1]:
            return email

        print("Invalid email. Please enter a valid email ID.")


def input_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid whole number.")


def input_float(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt).strip())

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def input_date_of_birth():
    while True:
        dob = input("Enter DOB (DD-MM-YYYY): ").strip()
        parts = dob.split("-")

        if len(parts) != 3:
            print("Use DD-MM-YYYY format.")
            continue

        try:
            day, month, year = map(int, parts)

            if not 1 <= day <= 31:
                print("Invalid day.")
                continue

            if not 1 <= month <= 12:
                print("Invalid month.")
                continue

            if not 1900 <= year <= 2100:
                print("Invalid year.")
                continue

            return (day, month, year)

        except ValueError:
            print("DOB must contain numbers only.")


def input_comma_list(prompt, title_case=False):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Enter at least one value.")
            continue

        items = [item.strip() for item in value.split(",") if item.strip()]

        if title_case:
            items = [item.title() for item in items]

        if items:
            return items

        print("Enter at least one value.")


def input_clubs():
    value = input(
        "Enter student clubs separated by commas (or press Enter for none): "
    ).strip()

    if not value:
        return set()

    return {
        club.strip().title()
        for club in value.split(",")
        if club.strip()
    }


def update_collection_sets():
    """Rebuild unique department, subject and club sets."""
    departments.clear()
    all_subjects.clear()
    student_clubs.clear()

    for student in students:
        departments.add(student["department"])
        all_subjects.update(student["subjects"])
        student_clubs.update(student["clubs"])


def display_student(student):
    print("\n" + "=" * 55)
    print("STUDENT DETAILS")
    print("=" * 55)

    roll = student["roll_number"][0]
    registration = student["registration_number"][0]
    day, month, year = student["date_of_birth"]

    print("Roll Number       :", roll)
    print("Registration No.  :", registration)
    print("Date of Birth     :", f"{day:02d}-{month:02d}-{year}")
    print("Name              :", student["name"])
    print("Department        :", student["department"])
    print("Subjects          :", ", ".join(student["subjects"]))

    print("\nAcademic Details:")
    for i, subject in enumerate(student["subjects"]):
        print(
            f"  {subject:<20} "
            f"Marks: {student['marks'][i]:g}   "
            f"Attendance: {student['attendance'][i]:g}%"
        )

    print("\nContact Information:")
    print("Address           :", student["contact"]["address"])
    print("Email             :", student["contact"]["email"])

    if student["clubs"]:
        print("Clubs             :", ", ".join(sorted(student["clubs"])))
    else:
        print("Clubs             : None")

    print("=" * 55)


def add_student():
    print("\n--- ADD STUDENT ---")

    roll = input_non_empty("Enter roll number: ")

    if find_student(roll) is not None:
        print("A student with this roll number already exists.")
        return

    registration = input_non_empty("Enter registration number: ")
    name = input_non_empty("Enter student name: ").title()
    department = input_non_empty("Enter department: ").upper()
    address = input_non_empty("Enter address: ")
    email = input_email()
    dob = input_date_of_birth()

    subjects = input_comma_list(
        "Enter subjects separated by commas: ",
        title_case=True
    )

    marks = []
    attendance = []

    print("\nEnter academic details:")

    for subject in subjects:
        mark = input_float(
            f"Enter marks for {subject} (0-100): ",
            0,
            100
        )

        attendance_value = input_float(
            f"Enter attendance for {subject} (0-100): ",
            0,
            100
        )

        marks.append(mark)
        attendance.append(attendance_value)

    clubs = input_clubs()

    student = {
        "roll_number": roll_tuple(roll),
        "registration_number": registration_tuple(registration),
        "date_of_birth": dob,
        "name": name,
        "department": department,
        "subjects": subjects,
        "marks": marks,
        "attendance": attendance,
        "contact": {
            "address": address,
            "email": email
        },
        "clubs": clubs
    }

    students.append(student)
    update_collection_sets()

    print("\nStudent added successfully.")


def search_student():
    print("\n--- SEARCH STUDENT ---")

    roll = input_non_empty("Enter roll number: ")
    student = find_student(roll)

    if student is None:
        print("Student Not Found.")
        return

    display_student(student)


def update_student():
    print("\n--- UPDATE STUDENT ---")

    roll = input_non_empty("Enter roll number to update: ")
    student = find_student(roll)

    if student is None:
        print("Student Not Found.")
        return

    while True:
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Department")
        print("3. Address")
        print("4. Email")
        print("5. Subjects, Marks and Attendance")
        print("6. Clubs")
        print("0. Cancel")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            student["name"] = input_non_empty("Enter new name: ").title()
            break

        elif choice == "2":
            student["department"] = input_non_empty(
                "Enter new department: "
            ).upper()
            break

        elif choice == "3":
            student["contact"]["address"] = input_non_empty(
                "Enter new address: "
            )
            break

        elif choice == "4":
            student["contact"]["email"] = input_email()
            break

        elif choice == "5":
            subjects = input_comma_list(
                "Enter new subjects separated by commas: ",
                title_case=True
            )

            marks = []
            attendance = []

            for subject in subjects:
                marks.append(
                    input_float(
                        f"Enter marks for {subject} (0-100): ",
                        0,
                        100
                    )
                )

                attendance.append(
                    input_float(
                        f"Enter attendance for {subject} (0-100): ",
                        0,
                        100
                    )
                )

            student["subjects"] = subjects
            student["marks"] = marks
            student["attendance"] = attendance
            break

        elif choice == "6":
            student["clubs"] = input_clubs()
            break

        elif choice == "0":
            print("Update cancelled.")
            return

        else:
            print("Invalid choice.")

    update_collection_sets()
    print("Record updated successfully.")


def delete_student():
    print("\n--- DELETE STUDENT ---")

    roll = input_non_empty("Enter roll number to delete: ")

    student = find_student(roll)

    if student is None:
        print("Student Not Found.")
        return

    display_student(student)

    confirmation = input("Are you sure you want to delete this record? (y/n): ")
    if confirmation.strip().lower() != "y":
        print("Deletion cancelled.")
        return

    students.remove(student)
    update_collection_sets()

    print("Record deleted successfully.")


def display_all_students():
    print("\n--- ALL STUDENTS ---")

    if not students:
        print("No records available.")
        return

    for student in students:
        display_student(student)


def calculate_average():
    print("\n--- CALCULATE AVERAGE MARKS ---")

    roll = input_non_empty("Enter roll number: ")
    student = find_student(roll)

    if student is None:
        print("Student Not Found.")
        return

    if not student["marks"]:
        print("No marks available.")
        return

    average = sum(student["marks"]) / len(student["marks"])

    print(f"Student: {student['name']}")
    print(f"Average Marks: {average:.2f}")


def find_highest_scorer():
    print("\n--- HIGHEST SCORER ---")

    if not students:
        print("No records available.")
        return

    students_with_marks = [
        student for student in students
        if student["marks"]
    ]

    if not students_with_marks:
        print("No marks available.")
        return

    highest = students_with_marks[0]
    highest_average = (
        sum(highest["marks"]) / len(highest["marks"])
    )

    for student in students_with_marks[1:]:
        average = sum(student["marks"]) / len(student["marks"])

        if average > highest_average:
            highest = student
            highest_average = average

    print(f"Highest Scorer: {highest['name']}")
    print(f"Roll Number: {highest['roll_number'][0]}")
    print(f"Department: {highest['department']}")
    print(f"Average Marks: {highest_average:.2f}")


def list_students_by_department():
    print("\n--- STUDENTS BY DEPARTMENT ---")

    if not students:
        print("No records available.")
        return

    department = input_non_empty("Enter department: ").upper()

    matching_students = [
        student for student in students
        if student["department"] == department
    ]

    if not matching_students:
        print("No students found in this department.")
        return

    print(f"\nStudents in {department}:")

    for student in matching_students:
        print(
            f"- {student['roll_number'][0]} : "
            f"{student['name']}"
        )


def count_students():
    print("\n--- COUNT STUDENTS ---")
    print("Total Students:", len(students))


def generate_reports():
    print("\n--- ACADEMIC REPORT ---")

    if not students:
        print("No records available.")
        return

    update_collection_sets()

    print("Total Students       :", len(students))
    print("Unique Departments   :", ", ".join(sorted(departments)))
    print("Unique Subjects      :", ", ".join(sorted(all_subjects)))

    if student_clubs:
        print("Unique Student Clubs :", ", ".join(sorted(student_clubs)))
    else:
        print("Unique Student Clubs : None")

    print("\nDepartment-wise Count:")

    for department in sorted(departments):
        count = sum(
            1 for student in students
            if student["department"] == department
        )
        print(f"  {department}: {count}")

    print("\nStudent Averages:")

    for student in students:
        if student["marks"]:
            average = sum(student["marks"]) / len(student["marks"])
            print(
                f"  {student['roll_number'][0]} - "
                f"{student['name']}: {average:.2f}"
            )


def display_menu():
    print("\n" + "=" * 55)
    print(" STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add Student")
    print("2. Search Student by Roll Number")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Calculate Average Marks")
    print("7. Find Highest Scorer")
    print("8. List Students by Department")
    print("9. Count Students")
    print("10. Generate Reports")
    print("0. Exit")
    print("=" * 55)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_all_students()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            find_highest_scorer()
        elif choice == "8":
            list_students_by_department()
        elif choice == "9":
            count_students()
        elif choice == "10":
            generate_reports()
        elif choice == "0":
            print("Program ended. Thank you!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.")


if __name__ == "__main__":
    main()
