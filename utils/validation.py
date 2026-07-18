# ==========================================
# validation.py
# Student ERP System
# ==========================================

def validate_name():
    """
    Validate student name.
    Only alphabets and spaces are allowed.
    """

    while True:
        name = input("Enter Student Name : ").strip()

        if not name:
            print("❌ Name cannot be empty.")
            continue

        if not all(ch.isalpha() or ch.isspace() for ch in name):
            print("❌ Name should contain only letters.")
            continue

        return name


def validate_age():
    """
    Validate student age.
    Age must be between 16 and 60.
    """

    while True:
        age = input("Enter Student Age : ").strip()

        if not age.isdigit():
            print("❌ Age must contain only numbers.")
            continue

        age = int(age)

        if age < 16 or age > 60:
            print("❌ Age must be between 16 and 60.")
            continue

        return age


def validate_course():
    """
    Validate course name.
    """

    while True:
        course = input("Enter Student Course : ").strip()

        if not course:
            print("❌ Course cannot be empty.")
            continue

        return course