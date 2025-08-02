import mysql.connector
import os
from dotenv import load_dotenv
import importlib.util
import sys
load_dotenv()



def get_conn():
    host = os.getenv("DB_HOST") or "localhost"
    user = os.getenv("DB_USER") or "root"
    password = os.getenv("DB_PASS") or ""
    database = os.getenv("DB_") or "shadowbot"
    conn =  mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return conn

def getToken():
    token = os.getenv("BOT_TOKEN") or ""
    return token
    
def migrate():
    MIGRATIONS_DIR = "db/migrations"
    migrations = sorted(
        f for f in os.listdir(MIGRATIONS_DIR)
        if f.endswith(".py") and not f.startswith("__")
    )

    for migration_file in migrations:
        migration_path = os.path.join(MIGRATIONS_DIR, migration_file)
        print(f"Running migration: {migration_file}")
        spec = importlib.util.spec_from_file_location("migration", migration_path)
        migration = importlib.util.module_from_spec(spec)
        sys.modules["migration"] = migration
        spec.loader.exec_module(migration)
        print(f"Finished: {migration_file}\n")
    print ("--------- MIGRATIONS FINISHED -----------")
