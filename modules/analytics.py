import database.database


def analytics():
    """
    Student ERP Analytics
    """

    students = database.database.get_all_students()

    if not students:
        print("\n❌ No Student Found!")
        return

    total_students = len(students)
    total_age = 0

    oldest_name = ""
    oldest_age = 0

    youngest_name = ""
    youngest_age = float("inf")

    course_count = {}

    adults = 0
    minors = 0

    for student_id, name, age, course in students:

        age = int(age)
        total_age += age

        if age >= 18:
            adults += 1
        else:
            minors += 1

        if age > oldest_age:
            oldest_age = age
            oldest_name = name

        if age < youngest_age:
            youngest_age = age
            youngest_name = name

        course_count[course] = course_count.get(course, 0) + 1

    average_age = total_age / total_students
    popular_course = max(course_count, key=course_count.get)

    print("\n" + "=" * 60)
    print("              📊 STUDENT ANALYTICS")
    print("=" * 60)

    print(f"👨 Total Students     : {total_students}")
    print(f"📈 Average Age        : {average_age:.2f}")

    print(f"\n👴 Oldest Student     : {oldest_name} ({oldest_age})")
    print(f"👶 Youngest Student   : {youngest_name} ({youngest_age})")

    print(f"\n🧑 Adults             : {adults}")
    print(f"🧒 Minors             : {minors}")

    print("\n🎓 Students Per Course")
    print("-" * 60)

    for course, count in course_count.items():
        print(f"{course:<20} : {count}")

    print("-" * 60)
    print(f"⭐ Most Popular Course : {popular_course}")

    print("=" * 60)