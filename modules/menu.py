# ==========================================
# Student ERP - Main Menu
# ==========================================

from modules.student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
)

from modules.user import (
    add_user,
    view_users,
)

from modules.dashboard import dashboard
from modules.analytics import analytics
from modules.reports import reports_menu
from modules.backup import backup_menu
from modules.export_csv import export_to_csv
from modules.attendance import attendance_menu
# ==========================================
# Student Management Menu
# ==========================================

def student_management_menu():

    while True:

        print("\n" + "=" * 45)
        print("        STUDENT MANAGEMENT")
        print("=" * 45)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        choice = input("\nEnter Choice : ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            break

        else:
            print("\n❌ Invalid Choice!")


# ==========================================
# User Management Menu
# ==========================================

def user_management_menu():

    while True:

        print("\n" + "=" * 45)
        print("         USER MANAGEMENT")
        print("=" * 45)

        print("1. Add User")
        print("2. View Users")
        print("3. Back")

        choice = input("\nEnter Choice : ").strip()

        if choice == "1":
            add_user()

        elif choice == "2":
            view_users()

        elif choice == "3":
            break

        else:
            print("\n❌ Invalid Choice!")


# ==========================================
# Main Menu
# ==========================================

def main_menu():

    while True:

        print("\n" + "=" * 45)
        print("            STUDENT ERP")
        print("=" * 45)

        print("1. Student Management")
        print("2. User Management")
        print("3. Dashboard")
        print("4. Analytics")
        print("5. Reports")
        print("6. Backup")
        print("7. Export CSV")
        print("8. Attendance Menu")
        print("9. Fees Management (Coming Soon)")
        print("10. Examination (Coming Soon)")
        print("11. Logout")

        choice = input("\nEnter Choice : ").strip()

        if choice == "1":
            student_management_menu()

        elif choice == "2":
            user_management_menu()

        elif choice == "3":
            dashboard()

        elif choice == "4":
            analytics()

        elif choice == "5":
            reports_menu()

        elif choice == "6":
            backup_menu()

        elif choice == "7":
            export_to_csv()

        elif choice == "8":
            attendance_menu()

        elif choice == "9":
            print("\n🚧 Fees Management Module Coming Soon...")

        elif choice == "10":
            print("\n🚧 Examination Module Coming Soon...")

        elif choice == "11":
            print("\n👋 Thank You for using Student ERP.")
            break

        else:
            print("\n❌ Invalid Choice!")