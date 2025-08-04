from db.db import get_conn
import datetime

class Message :
    def __init__(self, msg_id=None, msg=None, status=None):
        self.msg_id = msg_id
        self.msg = msg
        self.status = status

    @staticmethod
    def queue (msg):
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO messages(message) VALUES (%s)", (msg,))
        conn.commit()
        row = cursor.rowcount
        cursor.close()
        conn.close()

        if row > 0:
            return msg
        else:
            return False
    
    @staticmethod
    def view():
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM messages LIMIT 20")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        results = []
        string = ""
        for x in rows:
            string += "`" + x[0] + "` `" + ('AWAIT' if x[2] == 1 else 'DONE' ) + "` | " + x[1] +"\n"
        if string:
            return string
        else:
            return 'No message in database'

    @staticmethod
    def pop():
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM messages WHERE status = 1 ORDER BY id ASC LIMIT 1")
        row = cursor.fetchone()
        if not row:
            cursor.close()
            conn.close()
            return 'No more message queued.'
        cursor.execute("UPDATE messages SET status = 2 WHERE id = %s", (row[0],))
        conn.commit()
        cursor.close()
        conn.close()
        return row[1]
    
    @staticmethod
    def resetAll():
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("UPDATE messages SET status = 1", ())
        conn.commit()
        row = cursor.rowcount
        cursor.close()
        conn.close()
        if row > 0:
            return True
        else:
            return False





