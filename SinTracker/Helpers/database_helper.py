import sqlite3
import os

DB_FILENAME = "sinTracker.db"

def run_sql_file(filename):
    """
    Read an SQL file and execute its contents.

    Args:
        filename (str): Name of .sql file
    """
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()

    file_path = os.path.join("SQLite", filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"SQL file not found: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            sql_script = f.read()
            cursor.executescript(sql_script)
            conn.commit()
    except sqlite3.DatabaseError as e:
        print(f"SQLite error while executing {file_path}: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error while reading {file_path}: {e}")
        raise
    finally:
        conn.close()