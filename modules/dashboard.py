from datetime import datetime
from utils.file_handler import read_students


def dashboard():
    """
    Display Student ERP Dashboard
    """

    students = read_students()

    total_students = 0
    adults = 0
    minors = 0
    courses = set()

    for student in students:

        student = student.strip()

        if not student:
            continue

        data = student.split(",")

        if len(data) != 4:
            continue

        student_id, name, age, course = data

        total_students += 1

        age = int(age)

        if age >= 18:
            adults += 1
        else:
            minors += 1

        courses.add(course)

    now = datetime.now()

    print("\n" + "=" * 55)
    print("          🎓 STUDENT ERP DASHBOARD")
    print("=" * 55)

    print(f"📅 Date            : {now.strftime('%d-%m-%Y')}")
    print(f"🕒 Time            : {now.strftime('%I:%M:%S %p')}")

    print("-" * 55)

    print(f"👨 Total Students  : {total_students}")
    print(f"🧑 Adults          : {adults}")
    print(f"🧒 Minors          : {minors}")
    print(f"🎓 Total Courses   : {len(courses)}")

    print("=" * 55)