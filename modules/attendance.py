import database.database


def view_attendance():

    records = database.database.get_all_attendance()

    if not records:
        print("\n❌ No Attendance Records Found!")
        return

    print("\n" + "=" * 70)
    print(f"{'Student ID':<15}{'Name':<25}{'Date':<15}{'Status'}")
    print("=" * 70)

    for _, student_id, name, date, status in records:

        status_text = "Present" if status == "P" else "Absent"

        print(f"{student_id:<15}{name:<25}{date:<15}{status_text}")

    print("=" * 70)


from datetime import date

from modules import student

# attendance management functions
from datetime import date
import database.database


def mark_attendance():

    search = input("\nEnter Student ID or Name : ").strip()

    student = database.database.search_student(search)

    if not student:
        print("\n❌ Student Not Found!")
        return

    student_id = student[0]
    name = student[1]

    print(f"\nStudent : {name}")

    status = input("Attendance (P/A): ").strip().upper()

    if status not in ("P", "A"):
        print("\n❌ Invalid Status!")
        return

    today = str(date.today())

    # Check if attendance already exists
    if database.database.attendance_exists(student_id, today):
        print("\n❌ Attendance already marked for today!")
        return

    database.database.mark_attendance(student_id, today, status)

    print("\n✅ Attendance Marked Successfully!")
    
    today = str(date.today())

    database.database.mark_attendance(student_id, today, status)

    print("\n✅ Attendance Marked Successfully!")

def view_attendance():

    records = database.database.get_all_attendance()

    if not records:
        print("\n❌ No Attendance Record Found!")
        return

    print("\n" + "=" * 75)
    print("                      ATTENDANCE RECORD")
    print("=" * 75)
    print(f"{'ID':<10}{'Name':<20}{'Date':<15}{'Status'}")
    print("-" * 75)

    for _, student_id, name, attendance_date, status in records:
        print(f"{student_id:<10}{name:<20}{attendance_date:<15}{status}")

    print("=" * 75)

def attendance_menu():

    while True:

        print("\n" + "=" * 45)
        print("        ATTENDANCE MANAGEMENT")
        print("=" * 45)
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Search Attendance")
        print("4. Update Attendance")
        print("5. Delete Attendance")
        print("6. Attendance Report")
        print("0. Back")
        print("=" * 45)

        choice = input("Enter Choice : ").strip()

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            print("\n🚧 Search Attendance - Coming Soon")

        elif choice == "4":
            print("\n🚧 Update Attendance - Coming Soon")

        elif choice == "5":
            print("\n🚧 Delete Attendance - Coming Soon")

        elif choice == "6":
            print("\n🚧 Attendance Report - Coming Soon")

        elif choice == "0":
            break

        else:
            print("\n❌ Invalid Choice!")

## attendance menu
def attendance_menu():
    while True:
        print("\n===== ATTENDANCE MANAGEMENT =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("0. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "0":
            break

        else:
            print("Invalid Choice!")