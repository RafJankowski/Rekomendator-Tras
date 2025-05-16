import sqlite3
from pathlib import Path

def create_database_from_schema():

    current_dir = Path(__file__).parent
    with open(current_dir / "db_schema.sql", 'r', encoding='utf-8') as file:

        schema_sql = file.read()
        db_path = current_dir / "sqlite.db"
        connection = sqlite3.connect(db_path)
        connection.executescript(schema_sql)
        connection.close()

if __name__ == "__main__":
    
    create_database_from_schema()