import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENT_DB = os.path.join(BASE_DIR, "students.db")
USER_DB = os.path.join(BASE_DIR, "users.db")

# -------------------- STUDENT DATABASE --------------------
def init_db():
    conn = sqlite3.connect(STUDENT_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            education TEXT,
            stream TEXT,
            interest TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_student(name, education, stream, interest):
    conn = sqlite3.connect(STUDENT_DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, education, stream, interest) VALUES (?, ?, ?, ?)",
        (name, education, stream, interest)
    )
    conn.commit()
    conn.close()

# -------------------- USER DATABASE --------------------
def init_user_db():
    conn = sqlite3.connect(USER_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect(USER_DB)
    cursor = conn.cursor()
    try:
        hashed_pw = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_pw)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def validate_user(username, password):
    conn = sqlite3.connect(USER_DB)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return False
    stored_hash = row[0]
    return check_password_hash(stored_hash, password)
