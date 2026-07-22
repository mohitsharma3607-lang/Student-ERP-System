import os
import shutil
from datetime import datetime

DATABASE_FILE = "database/student_erp.db"
BACKUP_FOLDER = "backups"


def create_backup():
    """
    Create SQLite database backup
    """

    if not os.path.exists(DATABASE_FILE):
        print("\n❌ Database file not found!")
        return

    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_file = os.path.join(
        BACKUP_FOLDER,
        f"student_erp_backup_{timestamp}.db"
    )

    shutil.copy2(DATABASE_FILE, backup_file)

    print("\n✅ Database Backup Created Successfully!")
    print(f"📁 {backup_file}")


def restore_latest_backup():
    """
    Restore latest database backup
    """

    if not os.path.exists(BACKUP_FOLDER):
        print("\n❌ No Backup Folder Found!")
        return

    backups = [
        os.path.join(BACKUP_FOLDER, file)
        for file in os.listdir(BACKUP_FOLDER)
        if file.endswith(".db")
    ]

    if not backups:
        print("\n❌ No Backup Available!")
        return

    latest_backup = max(backups, key=os.path.getmtime)

    shutil.copy2(latest_backup, DATABASE_FILE)

    print("\n✅ Database Restored Successfully!")
    print(f"📁 Restored From: {latest_backup}")


def backup_menu():

    while True:

        print("\n" + "=" * 50)
        print("         💾 BACKUP MENU")
        print("=" * 50)
        print("1. Create Backup")
        print("2. Restore Latest Backup")
        print("3. Back")
        print("=" * 50)

        choice = input("Enter Choice: ")

        if choice == "1":
            create_backup()

        elif choice == "2":
            restore_latest_backup()

        elif choice == "3":
            break

        else:
            print("❌ Invalid Choice!")