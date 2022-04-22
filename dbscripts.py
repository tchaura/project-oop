"""Contains methods to read and write sql data"""
import sqlite3
from sqlite3 import Error


def create_connection(path):
    """Creates connection with database"""
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as new_error:
        print(f"The error '{new_error}' occurred")

    return connection


def execute_query(connection, query):
    """Executes query for SQL"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Data is saved successfully")
    except Error as new_error:
        print(f"The error '{new_error}' occurred")


def execute_read_query(connection, query):
    """Executes read query for SQL"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        result_list = []
        for i in result:
            result_list.append(list(i))
        return result_list
    except Error as new_error:
        print(f"The error '{new_error}' occurred")
        return None


new_connection = create_connection("database.sqlite")
