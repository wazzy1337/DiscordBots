import os
import sqlite3

from Helpers.database_helper import DB_FILENAME, run_sql_file

def initialize_db():
    db_exists = os.path.exists(DB_FILENAME)

    if db_exists:
        print(f"Connected to existing database: {DB_FILENAME}")
    else:
        print(f"Database created and connected: {DB_FILENAME}")

        # Run DB Schema
        run_sql_file("schema.sql")

        # Run seed for Players (Sinners)
        run_sql_file("seed_players.sql")