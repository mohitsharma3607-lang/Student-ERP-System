from utils.file_handler import read_students


def total_students_report():
    """
    Display total student report.
    """

    students = read_students()

    if not students:
        print("\n❌ No Student Found!")
        return

    total_students = 0
    total_age = 0
    adults = 0
    minors = 0

    for student in students:

        student = student.strip()

        if not student:
            continue

        data = student.split(",")

        if len(data) != 4:
            continue

        student_id, name, age, course = data

        age = int(age)

        total_students += 1
        total_age += age

        if age >= 18:
            adults += 1
        else:
            minors += 1

    average_age = total_age / total_students

    print("\n" + "=" * 50)
    print("        📄 TOTAL STUDENT REPORT")
    print("=" * 50)
    print(f"👨 Total Students : {total_students}")
    print(f"📈 Average Age    : {average_age:.2f}")
    print(f"🧑 Adults         : {adults}")
    print(f"🧒 Minors         : {minors}")
    print("=" * 50)


def course_report():
    """
    Display course-wise report.
    """

    students = read_students()

    if not students:
        print("\n❌ No Student Found!")
        return

    course_count = {}

    for student in students:

        student = student.strip()

        if not student:
            continue

        data = student.split(",")

        if len(data) != 4:
            continue

        student_id, name, age, course = data

        course_count[course] = course_count.get(course, 0) + 1

    print("\n" + "=" * 50)
    print("        🎓 COURSE REPORT")
    print("=" * 50)

    for course, count in course_count.items():
        print(f"{course:<20} : {count}")

    print("=" * 50)


def age_report():
    """
    Display age report.
    """

    students = read_students()

    if not students:
        print("\n❌ No Student Found!")
        return

    total_students = 0
    total_age = 0

    oldest_name = ""
    oldest_age = 0

    youngest_name = ""
    youngest_age = 999

    for student in students:

        student = student.strip()

        if not student:
            continue

        data = student.split(",")

        if len(data) != 4:
            continue

        student_id, name, age, course = data

        age = int(age)

        total_students += 1
        total_age += age

        if age > oldest_age:
            oldest_age = age
            oldest_name = name

        if age < youngest_age:
            youngest_age = age
            youngest_name = name

    average_age = total_age / total_students

    print("\n" + "=" * 50)
    print("          👶 AGE REPORT")
    print("=" * 50)
    print(f"👶 Youngest Student : {youngest_name} ({youngest_age})")
    print(f"👴 Oldest Student   : {oldest_name} ({oldest_age})")
    print(f"📈 Average Age      : {average_age:.2f}")
    print("=" * 50)


def reports_menu():
    """
    Reports menu.
    """

    while True:

        print("\n" + "=" * 50)
        print("          📄 REPORTS MENU")
        print("=" * 50)
        print("1. Total Students Report")
        print("2. Course-wise Report")
        print("3. Age Report")
        print("4. Back")
        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            total_students_report()

        elif choice == "2":
            course_report()

        elif choice == "3":
            age_report()

        elif choice == "4":
            break

        else:
            print("\n❌ Invalid Choice!")