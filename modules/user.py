# user ka module hai jisme user ko add karne ka function hai
from database.database import connect_db


def add_user():
    print("\n========== ADD USER ==========")

    username = input("Username : ").strip()
    password = input("Password : ").strip()
    role = input("Role (Admin/Teacher/Staff): ").strip().title()

    if role not in ["Admin", "Teacher", "Staff"]:
        print("❌ Invalid Role!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users(username, password, role)
            VALUES (?, ?, ?)
            """,
            (username, password, role),
        )

        conn.commit()
        print("✅ User Added Successfully!")

    except Exception as e:
        print(f"❌ Error : {e}")

    finally:
        conn.close()

from database.database import connect_db

# view_users function is used to display all users in the database
def view_users():
    """
    Display all users.
    """

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, role
        FROM users
        ORDER BY id
    """)

    users = cursor.fetchall()

    print("\n========== USER LIST ==========")

    if not users:
        print("❌ No users found.")
    else:
        print(f"{'ID':<5}{'Username':<20}{'Role'}")
        print("-" * 40)

        for user in users:
            print(f"{user[0]:<5}{user[1]:<20}{user[2]}")

    conn.close()