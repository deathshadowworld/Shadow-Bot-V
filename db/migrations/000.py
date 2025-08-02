import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("DB_HOST") or "localhost"
user = os.getenv("DB_USER") or "root"
password = os.getenv("DB_PASS") or ""
conn = mysql.connector.connect(
    host = host,
    user = user,
    password = password
)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS shadowbot")

# cursor.execute("SHOW DATABASES")
# databases = cursor.fetchall()

# # List of system databases we do NOT want to drop
# system_dbs = {"information_schema", "mysql", "performance_schema", "sys"}

# for (db_name,) in databases:
#     if db_name not in system_dbs:
#         print(f"Dropping database {db_name}...")
#         cursor.execute(f"DROP DATABASE `{db_name}`")

conn.commit()
cursor.close()
conn.close()

print("shadowbot DROPPED")

