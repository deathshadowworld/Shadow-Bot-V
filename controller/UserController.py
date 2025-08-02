from db.db import get_conn
import datetime

class User :
    def __init__(self, user_id=None, nickname=None):
        self.user_id = user_id
        self.nickname = nickname

    @staticmethod
    def checkExist (id):
        _exist = False
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE discord_id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            _exist = True
        return _exist

    def find (id):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE discord_id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def get():
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        list = []
        for row in rows:
            list.append(row)
        cursor.close()
        conn.close()
        return list

    def create(user):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users(discord_id, nickname, created_at, updated_at) VALUES (%s, %s, NOW(), NOW())", 
            (user.user_id, user.nickname)
            )
        conn.commit()
        cursor.close()
        conn.close()
        return



