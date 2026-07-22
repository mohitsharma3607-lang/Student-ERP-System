from datetime import datetime

# ==============================
# Student Module
# ==============================
from modules.student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
)

# ==============================
# Other Modules
# ==============================
from modules.dashboard import dashboard
from modules.analytics import analytics
from modules.reports import reports_menu
from modules.backup import backup_menu
from modules.export_csv import export_to_csv
from modules.login import login
from modules.menu import main_menu
from modules.user import add_user, view_users
from modules.user import add_user, view_users

# ==============================
# Database
# ==============================
from database.database import (
    initialize_database,
)
# ==============================
# Initialize Database
# ==============================
initialize_database()


# Uncomment only for testing
# show_all_students()


def show_datetime():
    """Display current date and time."""
    now = datetime.now()

    print("\n===================================")
    print("Current Date :", now.strftime("%d-%m-%Y"))
    print("Current Time :", now.strftime("%I:%M:%S %p"))
    print("===================================")


def main():
    while True:

        show_datetime()

        print("\n========== STUDENT ERP ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Dashboard")
        print("7. Analytics")
        print("8. Reports")
        print("9. Backup")
        print("10. Export CSV")
        print("11. User Management")
        print("12. View Users")
        print("13. Exit")
        print("=================================")

        choice = input("Enter your choice : ").strip()

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
            dashboard()

        elif choice == "7":
            analytics()

        elif choice == "8":
            reports_menu()

        elif choice == "9":
            backup_menu()

        elif choice == "10":
            export_to_csv()

        elif choice == "11":
            add_user()

        elif choice == "12":
            view_users()

        elif choice == "13":
            print("\n👋 Thank You for using Student ERP.")
            break

        else:
            print("\n❌ Invalid Choice! Please try again.")


if __name__ == "__main__":

    if not login():
        exit()

    dashboard()

    input("\nPress Enter to Continue...")

    main_menu()
