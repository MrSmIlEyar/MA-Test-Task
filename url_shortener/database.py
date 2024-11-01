import sqlite3
import os

DATABASE_URL = "sqlite:///./test.db"
DATABASE_FILE = "test.db"


def get_db():
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    if not os.path.exists(DATABASE_FILE):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT NOT NULL UNIQUE
        )
        """)
        conn.commit()
        conn.close()


create_tables()
