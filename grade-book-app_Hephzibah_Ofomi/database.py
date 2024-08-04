import sqlite3

def connect():
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (email TEXT, names TEXT, GPA REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (name TEXT, trimester TEXT, credits INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS registrations (student_email TEXT, course_name TEXT, grade REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (student_email TEXT, course_name TEXT, attendance INTEGER)''')
    conn.commit()
    return conn

def add_student_to_db(email, names):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO students (email, names) VALUES (?, ?)''', (email, names))
    conn.commit()
    conn.close()

def add_course_to_db(name, trimester, credits):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO courses (name, trimester, credits) VALUES (?, ?, ?)''', (name, trimester, credits))
    conn.commit()
    conn.close()

def register_student_for_course(student_email, course_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO registrations (student_email, course_name) VALUES (?, ?)''', (student_email, course_name))
    conn.commit()
    conn.close()

def track_attendance(student_email, course_name, attendance):
    conn = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO attendance (student_email, course_name, attendance) 
                          VALUES (?, ?, ?)''', (student_email, course_name, attendance))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def update_student_GPA(email, gpa):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''UPDATE students SET GPA = ? WHERE email = ?''', (gpa, email))
    conn.commit()
    conn.close()

