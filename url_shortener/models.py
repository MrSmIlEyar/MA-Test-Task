import sqlite3
from database import get_db


def create_short_url(original_url: str, short_url: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
    conn.commit()
    conn.close()


def get_original_url(short_url: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT original_url FROM urls WHERE short_url = ?", (short_url,))
    result = cursor.fetchone()
    conn.close()
    return result['original_url'] if result else None
