import os
import sqlite3

def initialize_db():
    db_filename = "sinTracker.db"

    db_exists = os.path.exists(db_filename)

    conn = sqlite3.connect(db_filename)

    if db_exists:
        print(f"Connected to existing database: {db_filename}")
    else:
        print(f"Database created and connected: {db_filename}")

    conn.close()