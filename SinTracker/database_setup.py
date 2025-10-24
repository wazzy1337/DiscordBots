import os
import sqlite3

from Helpers.database_helper import run_sql_file

def initialize_db():
    db_filename = "sinTracker.db"

    db_exists = os.path.exists(db_filename)

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    if db_exists:
        print(f"Connected to existing database: {db_filename}")
    else:
        print(f"Database created and connected: {db_filename}")

        # Run DB Schema
        schema_path = os.path.join("SQLite", "schema.sql")
        run_sql_file(cursor, schema_path)

        # Run seed for Players (Sinners)
        seed_path = os.path.join("SQLite", "seed_players.sql")
        run_sql_file(cursor, seed_path)
    
    conn.commit()
    conn.close()