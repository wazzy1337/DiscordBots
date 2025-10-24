import sqlite3
import os

def run_sql_file(cursor, path):
    """
    Read an SQL file and execute its contents.

    Args:
        cursor: sqlite3.Cursor object
        path (str): Path to the .sql file
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"SQL file not found: {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            sql_script = f.read()
            cursor.executescript(sql_script)
    except sqlite3.DatabaseError as e:
        print(f"SQLite error while executing {path}: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error while reading {path}: {e}")
        raise