from tgbot.files.config import db_path
import sqlite3


class SQLite:
    def __init__(self):
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def register_user(self, user_id, lang, full_name, phone_number):
        with self.connection:
            self.connection.execute("""INSERT INTO users (user_id, lang, full_name, phone_number) VALUES
            (?, ?, ?, ?)""", [user_id, lang, full_name, phone_number])

    def is_registered(self, user_id):
        with self.connection:
            self.cursor.execute("""SELECT user_id FROM users WHERE user_id == ? """, [user_id])
            rows = self.cursor.fetchone()
            if rows:
                return rows
            else:
                return False
    def get_user_lang(self, user_id):
        with self.connection:
            self.cursor.execute("""SELECT lang FROM users WHERE user_id == ? """, [user_id])
            row = self.cursor.fetchall()

            return row[0]

