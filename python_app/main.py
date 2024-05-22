#!/usr/bin/env python

import sqlite3
import tables
import table_data

def create_sqlite_database(filename):
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_sqlite_database('python_sql_bids.db')
    tables.Create_tables('python_sql_bids.db')
    table_data.insert_data('python_sql_bids.db', table_data.insert_statements)

