import sqlite3
from encryption import encrypt_password, decrypt_password

DB_FILE = "passwords.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT UNIQUE,
            username TEXT,
            password TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS masters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            name TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_password(website, username, password):
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                       (website, username, encrypted_password))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def get_password(website):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE website=?", (website,))
    data = cursor.fetchone()
    conn.close()
    if data:
        return data[0], decrypt_password(data[1])
    return None

def save_master(username, name, password):
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO masters (username, name, password) VALUES (?, ?, ?)",
                       (username, name, encrypted_password))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def get_master(username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, password FROM masters WHERE username=?", (username,))
    data = cursor.fetchone()
    conn.close()
    if data:
        return data[0], decrypt_password(data[1])
    return None