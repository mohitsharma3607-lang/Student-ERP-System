# ==========================================
# file_handler.py
# Student ERP System
# ==========================================

FILE_NAME = "data/students.txt"


def read_students():
    """
    Read all student records.
    """

    try:
        with open(FILE_NAME, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        return []


def write_students(students):
    """
    Overwrite student records.
    """

    with open(FILE_NAME, "w") as file:
        file.writelines(students)


def append_student(student):
    """
    Add one student record.
    """

    with open(FILE_NAME, "a") as file:
        file.write(student)