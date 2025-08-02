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
cursor.execute("CREATE DATABASE IF NOT EXISTS shadowbot")

cursor.close()
conn.close()
