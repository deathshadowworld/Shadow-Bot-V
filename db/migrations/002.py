from db import db

conn = db.get_conn()

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            discord_id VARCHAR(64),
                            nickname VARCHAR(64),
                            created_at DATETIME,
                            updated_at DATETIME
               )""")
cursor.close()
conn.close()
