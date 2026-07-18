from utils.validation import (
    validate_name,
    validate_age,
    validate_course,
)

from utils.file_handler import (
    read_students,
    write_students,
    append_student,
)


FILE_NAME = "data/students.txt"


# ==========================================
# Generate Student ID
# ==========================================

def generate_student_id():

    students = read_students()

    if not students:
        return 1001

    last_record = students[-1].strip()

    if not last_record:
        return 1001

    data = last_record.split(",")

    return int(data[0]) + 1


# ==========================================
# Add Student
# ==========================================

def add_student():

    student_id = generate_student_id()

    name = validate_name()
    age = validate_age()
    course = validate_course()

    record = f"{student_id},{name},{age},{course}\n"

    append_student(record)

    print("\n===================================")
    print("✅ Student Added Successfully")
    print(f"Student ID : {student_id}")
    print("===================================")


# ==========================================
# View Students
# ==========================================

def view_students():

    students = read_students()

    if not students:
        print("\n❌ No Student Found!")
        return

    print("\n" + "=" * 65)
    print("                 STUDENT LIST")
    print("=" * 65)

    for i, student in enumerate(students, start=1):

        student = student.strip()

        if not student:
            continue

        data = student.split(",")

        if len(data) != 4:
            continue

        student_id, name, age, course = data

        print(f"\nStudent No. : {i}")
        print(f"Student ID  : {student_id}")
        print(f"Name        : {name}")
        print(f"Age         : {age}")
        print(f"Course      : {course}")
        print("-" * 65)


# ==========================================
# Search Student
# ==========================================

def search_student():

    search = input("Enter Student ID or Name : ").strip().lower()

    students = read_students()

    found = False

    for student in students:

        student = student.strip()

        if not student:
            continue

        data = student.split(",")

        if len(data) != 4:
            continue

        student_id, name, age, course = data

        if student_id == search or name.lower() == search:

            print("\n========== Student Found ==========")
            print(f"Student ID : {student_id}")
            print(f"Name       : {name}")
            print(f"Age        : {age}")
            print(f"Course     : {course}")
            print("===================================")

            found = True
            break

    if not found:
        print("\n❌ Student Not Found!")


# ==========================================
# Update Student
# ==========================================

def update_student():

    search = input("Enter Student ID or Name : ").strip().lower()

    students = read_students()

    updated_students = []

    found = False

    for student in students:

        student = student.strip()

        if not student:
            continue

        data = student.split(",")

        if len(data) != 4:
            continue

        student_id, name, age, course = data

        if student_id == search or name.lower() == search:

            print("\nUpdating Student...\n")

            new_name = validate_name()
            new_age = validate_age()
            new_course = validate_course()

            updated_students.append(
                f"{student_id},{new_name},{new_age},{new_course}\n"
            )

            found = True

        else:

            updated_students.append(student + "\n")

    write_students(updated_students)

    if found:
        print("\n✅ Student Updated Successfully!")

    else:
        print("\n❌ Student Not Found!")


# ==========================================
# Delete Student
# ==========================================

def delete_student():

    search = input("Enter Student ID or Name : ").strip().lower()

    students = read_students()

    updated_students = []

    found = False

    for student in students:

        student = student.strip()

        if not student:
            continue

        data = student.split(",")

        if len(data) != 4:
            continue

        student_id, name, age, course = data

        if student_id == search or name.lower() == search:

            found = True
            continue

        updated_students.append(student + "\n")

    write_students(updated_students)

    if found:
        print("\n✅ Student Deleted Successfully!")

    else:
        print("\n❌ Student Not Found!")