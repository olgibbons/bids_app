import sqlite3
import sql_statements

def Create_tables(db):
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            for statement in sql_statements.statements:
                cursor.execute(statement)
            
            conn.commit()
    except sqlite3.Error as e:
        print(e)
