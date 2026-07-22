from datetime import datetime
import database.database


def dashboard():
    """
    Display Student ERP Dashboard
    """

    students = database.database.get_all_students()

    total_students = len(students)
    adults = 0
    minors = 0
    courses = set()

    for student_id, name, age, course in students:

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