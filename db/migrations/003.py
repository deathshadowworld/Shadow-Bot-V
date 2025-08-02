from db import db

conn = db.get_conn()

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        message VARCHAR(1024) NOT NULL,
                        status BOOLEAN NOT NULL DEFAULT 1,
                        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                    );
               """)
cursor.close()
conn.close()
