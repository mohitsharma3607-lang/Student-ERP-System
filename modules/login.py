import getpass
from database.database import connect_db


def login():

    max_attempts = 3

    for attempt in range(max_attempts):

        print("\n========== LOGIN ==========")

        username = input("Username : ").strip()
        password = getpass.getpass("Password : ")

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT role
            FROM users
            WHERE username = ? AND password = ?
            """,
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            print(f"\n✅ Login Successful! ({user[0]})")
            return True

        print("\n❌ Invalid Username or Password")
        print(f"Remaining Attempts : {max_attempts - attempt - 1}")

    print("\n❌ Too many failed attempts.")
    return False