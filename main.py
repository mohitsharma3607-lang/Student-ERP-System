from function import *

while True:

    dashboard()

    print("\n" + "=" * 45)
    show_datetime()
    print("-" * 50)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Analytics")
    print("7. Exit")
    print("=" * 45)

    choice = input("Enter Your Choice : ")

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
        analytics()

    elif choice == "7":
        print("Thank You ❤️")
        break

    else:
        print("\nInvalid Choice!")