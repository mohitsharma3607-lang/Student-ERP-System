from datetime import datetime
# student generation statement
def generate_student_id():

    try:
        with open("students.txt", "r") as file:

            students = file.readlines()

            if len(students) == 0:
                return 1001

            last_student = students[-1]

            last_id = int(last_student.split(",")[0])

            return last_id + 1

    except FileNotFoundError:
        return 1001

# view statement
def view_students():

    try:
        with open("students.txt", "r") as file:

            students = file.readlines()

            if len(students) == 0:
                print("\n❌ No Student Found!")
                return

            print("\n" + "=" * 50)
            print("           STUDENT LIST")
            print("=" * 50)

            for i, student in enumerate(students, start=1):

                student_id, name, age, course = student.strip().split(",")

                print(f"\nStudent No. : {i}")
                print(f"Student ID  : {student_id}")
                print(f"Name        : {name}")
                print(f"Age         : {age}")
                print(f"Course      : {course}")
                print("-" * 50)

    except FileNotFoundError:
        print("\n❌ students.txt file not found!")

# add statement
def add_student():

    student_id = generate_student_id()

    name = input("Enter Student Name : ").strip()
    age = input("Enter Student Age : ").strip()
    course = input("Enter Student Course : ").strip()

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{age},{course}\n")

    print("\n==============================")
    print("✅ Student Added Successfully!")
    print(f"Student ID : {student_id}")
    print("==============================")

def view_students():

    try:
        with open("students.txt", "r") as file:

            students = file.readlines()

            if len(students) == 0:
                print("\n❌ No Student Found!")
                return

            print("\n" + "=" * 50)
            print("           STUDENT LIST")
            print("=" * 50)

            for i, student in enumerate(students, start=1):

                student_id, name, age, course = student.strip().split(",")

                print(f"\nStudent No. : {i}")
                print(f"Student ID  : {student_id}")
                print(f"Name        : {name}")
                print(f"Age         : {age}")
                print(f"Course      : {course}")
                print("-" * 50)

    except FileNotFoundError:
        print("\n❌ students.txt file not found!")

# search statement
def search_student():

    search = input("Enter Student ID or Name : ").strip()

    try:
        with open("students.txt", "r") as file:

            students = file.readlines()

            found = False

            for student in students:

                student_id, name, age, course = student.strip().split(",")

                if student_id == search or name.lower() == search.lower():

                    print("\n" + "=" * 40)
                    print("      STUDENT FOUND ✅")
                    print("=" * 40)
                    print(f"Student ID : {student_id}")
                    print(f"Name       : {name}")
                    print(f"Age        : {age}")
                    print(f"Course     : {course}")
                    print("=" * 40)

                    found = True
                    break

            if not found:
                print("\n❌ Student Not Found!")

    except FileNotFoundError:
        print("\n❌ students.txt file not found!")

#delte statement
def delete_student():

    search = input("Enter Student ID or Name to Delete : ").strip()

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        found = False

        with open("students.txt", "w") as file:

            for student in students:

                student_id, name, age, course = student.strip().split(",")

                if student_id == search or name.lower() == search.lower():

                    found = True
                    continue

                file.write(f"{student_id},{name},{age},{course}\n")

        if found:
            print("\n✅ Student Deleted Successfully!")

        else:
            print("\n❌ Student Not Found!")

    except FileNotFoundError:
        print("\n❌ students.txt file not found!")

# total students statement
def total_students():

    try:
        with open("students.txt", "r") as file:

            students = file.readlines()

            print("\n" + "=" * 35)
            print(f"📚 Total Students : {len(students)}")
            print("=" * 35)

    except FileNotFoundError:
        print("\n❌ students.txt file not found!")

#update statement
def update_student():

    search = input("Enter Student ID or Name to Update : ").strip()

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        updated_students = []
        found = False

        for student in students:

            student_id, name, age, course = student.strip().split(",")

            if student_id == search or name.lower() == search.lower():

                print("\n✅ Student Found!")
                print(f"Student ID : {student_id}")
                print(f"Current Name : {name}")
                print(f"Current Age : {age}")
                print(f"Current Course : {course}")

                print("\nEnter New Details")

                new_name = input("Enter New Name : ").strip()
                new_age = input("Enter New Age : ").strip()
                new_course = input("Enter New Course : ").strip()

                updated_students.append(
                    f"{student_id},{new_name},{new_age},{new_course}\n"
                )

                found = True

            else:
                updated_students.append(student)

        with open("students.txt", "w") as file:
            file.writelines(updated_students)

        if found:
            print("\n✅ Student Updated Successfully!")

        else:
            print("\n❌ Student Not Found!")

    except FileNotFoundError:
        print("\n❌ students.txt file not found!")

# desine statement
def dashboard():

    try:
        with open("students.txt", "r") as file:

            students = file.readlines()

            total = 0
            adults = 0
            minors = 0

            for student in students:

                student = student.strip()

                # Blank line skip
                if not student:
                    continue

                data = student.split(",")

                # Invalid record skip
                if len(data) != 4:
                    print(f"⚠ Invalid record skipped: {student}")
                    continue

                student_id, name, age, course = data

                total += 1

                if age.isdigit():
                    if int(age) >= 18:
                        adults += 1
                    else:
                        minors += 1
                else:
                    print(f"⚠ Invalid age for {student_id}: {age}")

            print("\n" + "=" * 50)
            print("      🎓 STUDENT MANAGEMENT SYSTEM 🎓")
            print("=" * 50)
            print(f"📚 Total Students : {total}")
            print(f"👨 Adults (18+)   : {adults}")
            print(f"🧒 Minors (<18)   : {minors}")
            print("=" * 50)

    except FileNotFoundError:
        print("students.txt file not found!")
        
# date time statement
def show_datetime():

    now = datetime.now()

    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%I:%M:%S %p")

    print(f"📅 Date : {current_date}")
    print(f"🕒 Time : {current_time}")

# analytics statement
def analytics():

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if len(students) == 0:
            print("\n❌ No Student Found!")
            return

        total = len(students)
        adults = 0
        minors = 0
        total_age = 0

        oldest_name = ""
        oldest_age = 0

        youngest_name = ""
        youngest_age = 999

        course_count = {}

        for student in students:

            student_id, name, age, course = student.strip().split(",")

            age = int(age)

            total_age += age

            # Adult / Minor
            if age >= 18:
                adults += 1
            else:
                minors += 1

            # Oldest Student
            if age > oldest_age:
                oldest_age = age
                oldest_name = name

            # Youngest Student
            if age < youngest_age:
                youngest_age = age
                youngest_name = name

            # Course Count
            if course in course_count:
                course_count[course] += 1
            else:
                course_count[course] = 1

        average_age = total_age / total

        # Most Popular Course
        popular_course = max(course_count, key=course_count.get)

        print("\n" + "=" * 55)
        print("                📊 ANALYTICS")
        print("=" * 55)

        print(f"📚 Total Students : {total}")
        print(f"👨 Adults          : {adults}")
        print(f"🧒 Minors          : {minors}")
        print(f"📈 Average Age     : {average_age:.2f}")

        print(f"\n🏆 Oldest Student  : {oldest_name} ({oldest_age})")
        print(f"🎈 Youngest Student: {youngest_name} ({youngest_age})")

        print("\n🎓 Course Statistics")
        print("-" * 55)

        for course, count in course_count.items():
            print(f"{course:<20} {'█' * count} ({count})")

        print("-" * 55)

        print("\n💡 INSIGHTS")
        print(f"⭐ Most Popular Course : {popular_course}")
        print(f"📈 Average Age        : {average_age:.2f} Years")

        print("=" * 55)

    except FileNotFoundError:
        print("\n❌ students.txt file not found!")