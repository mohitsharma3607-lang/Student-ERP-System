from utils.validation import (
    validate_name,
    validate_age,
    validate_course,
)

import database.database


# ==========================================
# Add Student
# ==========================================

def generate_student_id():
    """Return a unique student ID based on the existing student records."""

    existing_ids = {
        str(student[0])
        for student in database.database.get_all_students()
        if student and student[0] is not None
    }

    number = 1
    while f"STU{number:03d}" in existing_ids:
        number += 1

    return f"STU{number:03d}"


def insert_student(student_id, name, age, course):
    """Insert a student record and return whether the operation succeeded."""

    return database.database.insert_student(student_id, name, age, course)

def add_student():

    print("\n========== ADD STUDENT ==========")

    student_id = generate_student_id()

    print(f"Student ID : {student_id}")

    name = validate_name()
    age = validate_age()
    course = validate_course()

    if insert_student(student_id, name, age, course):
        print("\n✅ Student Added Successfully!")
    else:
        print("\n❌ Student ID already exists.")


# ==========================================
# View Students
# ==========================================

def view_students():

    students = database.database.get_all_students()

    if not students:
        print("\n❌ No Student Found!")
        return

    print("\n" + "=" * 65)
    print("                 STUDENT LIST")
    print("=" * 65)

    for i, (student_id, name, age, course) in enumerate(students, start=1):

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

    search = input("Enter Student ID or Name : ").strip()

    student = database.database.search_student(search)

    if student:

        student_id, name, age, course = student

        print("\n========== Student Found ==========")
        print(f"Student ID : {student_id}")
        print(f"Name       : {name}")
        print(f"Age        : {age}")
        print(f"Course     : {course}")
        print("===================================")

    else:

        print("\n❌ Student Not Found!")


# ==========================================
# Update Student
# ==========================================

def update_student():

    search = input("Enter Student ID or Name : ").strip()

    student = database.database.search_student(search)

    if not student:
        print("\n❌ Student Not Found!")
        return

    student_id, old_name, old_age, old_course = student

    print("\nCurrent Details")
    print("-" * 30)
    print(f"Student ID : {student_id}")
    print(f"Name       : {old_name}")
    print(f"Age        : {old_age}")
    print(f"Course     : {old_course}")

    print("\nEnter New Details")

    name = validate_name()
    age = validate_age()
    course = validate_course()

    if database.database.update_student(student_id, name, age, course):
        print("\n✅ Student Updated Successfully!")
    else:
        print("\n❌ Update Failed!")


# ==========================================
# Delete Student
# ==========================================

def delete_student():

    search = input("Enter Student ID or Name : ").strip()

    student = database.database.search_student(search)

    if not student:
        print("\n❌ Student Not Found!")
        return

    student_id, name, age, course = student

    print("\nStudent Details")
    print("-" * 30)
    print(f"Student ID : {student_id}")
    print(f"Name       : {name}")
    print(f"Age        : {age}")
    print(f"Course     : {course}")

    confirm = input("\nDelete this student? (y/n): ").strip().lower()

    if confirm == "y":
        if database.database.delete_student(student_id):
            print("\n✅ Student Deleted Successfully!")
        else:
            print("\n❌ Delete Failed!")
    else:
        print("\n❌ Delete Cancelled.")