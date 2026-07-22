import csv
import os
import database.database

EXPORT_FOLDER = "exports"


def export_to_csv():
    """
    Export students data to CSV.
    """

    students = database.database.get_all_students()

    if not students:
        print("\n❌ No Student Found!")
        return

    os.makedirs(EXPORT_FOLDER, exist_ok=True)

    file_path = os.path.join(EXPORT_FOLDER, "students.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Student ID", "Name", "Age", "Course"])

        for student_id, name, age, course in students:
            writer.writerow([student_id, name, age, course])

    print("\n✅ CSV Export Successful!")
    print(f"📁 File Saved: {file_path}")