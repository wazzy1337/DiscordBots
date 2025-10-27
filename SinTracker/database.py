import os
import sqlite3

from Helpers.database_helper import DB_FILENAME, run_sql_file, run_sql_file_select, run_sql_file_write

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

        # Run seed for Sins
        run_sql_file("seed_sins.sql")


def add_sin_to_player(player_id, sin_name):
    return run_sql_file_write("add_sin.sql", (player_id, sin_name))

def get_total_sins():
    total = run_sql_file_select("get_total_sins.sql")
    return total[0][0] if total and total[0][0] is not None else 0

def get_total_sins_by_player(player_name):
    total = run_sql_file_select("get_total_sins_player.sql", (player_name,))
    return total[0][0] if total and total[0][0] is not None else None

def get_sins():
    return run_sql_file_select("get_sins.sql")