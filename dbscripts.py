import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection("database.db")

select_receipts = "SELECT * from receipts"
receipts = execute_read_query(connection, select_receipts)

for receipt in receipts:
    print(receipt)

# create_receipt = f"""
#         INSERT INTO
#           receipts (number, typeofdevice, mark, OS, date_of_manufacturing, diagonal, description, date_of_receiving, date_of_repair, initials, status)
#         VALUES
#           (NULL, "sdasdfadf", "sdf", "dfsdg", "asff", 23, "dfsg", "ssgfs", "sgfs", "dsfsg", "fsf");
#         """
# execute_query(connection, create_receipt)
# receiptsdict = {1: Receipt(1, Phone("Xiaomi", "Android", "MIUI is shit pls help"), "2022-02-24", "2022-02-26", "Antony",
#                            Receipt.list_of_statuses[2]),
#                 2: Receipt(2, TV("Samsung", "27", "Screen is white"), "2022-03-05", "2022-03-11", "Andrey",
#                            Receipt.list_of_statuses[2]),
#                 3: Receipt(3, Notebook("Asus", "Windows 11", "2012-03-02", "Doesn't start"), "2022-02-13", "2022-02-15",
#                            "Dmitry", Receipt.list_of_statuses[2]),
#                 4: Receipt(4, TV("LG", 40, "Doesn't work"), "2021-04-25", "2021-04-30", "Vitaly",
#                            Receipt.list_of_statuses[2]),
#                 5: Receipt(5, Phone("Samsung", "Android", "Works slowly"), "2021-07-15", "2021-07-17", "Max",
#                            Receipt.list_of_statuses[2])}