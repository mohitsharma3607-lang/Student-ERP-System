import sqlite3

DATABASE_NAME = "database/student_erp.db"


# ==========================================
# Database Connection
# ==========================================

def connect_db():
    return sqlite3.connect(DATABASE_NAME)


# ==========================================
# Create Students Table
# ==========================================

def create_students_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            attendance_date TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('P','A')),
            FOREIGN KEY(student_id)
            REFERENCES students(student_id)
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# Create Users Table
# ==========================================

def create_users_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# Default Admin
# ==========================================

def create_default_admin():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users
        (username,password,role)
        VALUES(?,?,?)
    """, ("admin", "admin123", "Admin"))

    conn.commit()
    conn.close()


# ==========================================
# Initialize Database
# ==========================================

def initialize_database():

    create_students_table()
    create_users_table()
    create_default_admin()

    print("✅ Database Ready!")


# ==========================================
# Generate Student ID
# ==========================================

def generate_student_id():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id
        FROM students
        ORDER BY CAST(student_id AS INTEGER) DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return "1001"

    return str(int(row[0]) + 1)
# ==========================================
# Insert Student
# ==========================================

def insert_student(student_id, name, age, course):

    conn = connect_db()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            INSERT INTO students
            (student_id, name, age, course)
            VALUES (?, ?, ?, ?)
        """, (student_id, name, age, course))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


# ==========================================
# Get All Students
# ==========================================

def get_all_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, age, course
        FROM students
        ORDER BY student_id
    """)

    students = cursor.fetchall()

    conn.close()

    return students


# ==========================================
# Search Student
# ==========================================

def search_student(search_value):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, age, course
        FROM students
        WHERE student_id = ?
        OR LOWER(name) = LOWER(?)
    """, (search_value, search_value))

    student = cursor.fetchone()

    conn.close()

    return student


# ==========================================
# Update Student
# ==========================================

def update_student(student_id, name, age, course):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET
            name = ?,
            age = ?,
            course = ?
        WHERE student_id = ?
    """, (name, age, course, student_id))

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return updated > 0


# ==========================================
# Delete Student
# ==========================================

def delete_student(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM students
        WHERE student_id = ?
    """, (student_id,))

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted > 0


# ==========================================
# Show All Students
# ==========================================

def show_all_students():

    students = get_all_students()

    if not students:
        print("\n❌ No Students Found!")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<10}{'Name':<25}{'Age':<10}{'Course'}")
    print("=" * 70)

    for student in students:
        print(
            f"{student[0]:<10}"
            f"{student[1]:<25}"
            f"{student[2]:<10}"
            f"{student[3]}"
        )

    print("=" * 70)
# ==========================================
# Mark Attendance
# ==========================================

def mark_attendance(student_id, attendance_date, status):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO attendance
        (student_id, attendance_date, status)
        VALUES (?, ?, ?)
    """, (student_id, attendance_date, status))

    conn.commit()
    conn.close()


# ==========================================
# Get All Attendance
# ==========================================

def get_all_attendance():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            attendance.id,
            students.student_id,
            students.name,
            attendance.attendance_date,
            attendance.status
        FROM attendance
        INNER JOIN students
            ON attendance.student_id = students.student_id
        ORDER BY attendance.attendance_date DESC,
                 students.student_id
    """)

    records = cursor.fetchall()

    conn.close()

    return records


# ==========================================
# Search Attendance
# ==========================================

def search_attendance(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            attendance.id,
            students.student_id,
            students.name,
            attendance.attendance_date,
            attendance.status
        FROM attendance
        INNER JOIN students
            ON attendance.student_id = students.student_id
        WHERE students.student_id = ?
        ORDER BY attendance.attendance_date DESC
    """, (student_id,))

    records = cursor.fetchall()

    conn.close()

    return records


# ==========================================
# Update Attendance
# ==========================================

def update_attendance(attendance_id, status):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE attendance
        SET status = ?
        WHERE id = ?
    """, (status, attendance_id))

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return updated > 0


# ==========================================
# Delete Attendance
# ==========================================

def delete_attendance(attendance_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM attendance
        WHERE id = ?
    """, (attendance_id,))

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted > 0

# ==========================================
# Check Attendance Already Exists
# ==========================================

def attendance_exists(student_id, attendance_date):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1
        FROM attendance
        WHERE student_id = ?
        AND attendance_date = ?
    """, (student_id, attendance_date))

    exists = cursor.fetchone() is not None

    conn.close()

    return exists

def attendance_exists(student_id, attendance_date):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1
        FROM attendance
        WHERE student_id = ?
        AND attendance_date = ?
    """, (student_id, attendance_date))

    exists = cursor.fetchone() is not None

    conn.close()

    return exists