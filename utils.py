"""
    Module with functions
"""
import datetime
import random
from devices import Phone, TV, Notebook
from receipt import Receipt
from dbscripts import execute_query, execute_read_query, new_connection


def create_repair_request():
    """ Creates repair request """
    initials = input("Please, input your initials: ")

    operating_system = "null"
    date_of_manufacturing = "null"
    diagonal = "null"
    print("Choose the type of product you want to repair: ")
    k = 1
    for i in Receipt.list_of_products:
        print(f"{k}. {i}")
        k += 1
    try:
        switch = Receipt.list_of_products[int(input()) - 1]
    except ValueError:
        return "Wrong number"

    mark = input("Input mark: ")
    description = input("Input description: ")

    repairing_device = None
    if switch == "Phone":
        operating_system = input("Input OS: ")
        repairing_device = Phone(mark, operating_system, description)

    if switch == "Notebook":
        operating_system = input("Input OS: ")
        date_of_manufacturing = input("Input date of manufacturing in the format \"YYYY-MM-DD\": ")
        repairing_device = Notebook(mark, operating_system, date_of_manufacturing, description)

    if switch == "TV":
        diagonal = input("Input diagonal: ")
        repairing_device = TV(mark, diagonal, description)

    date_of_receiving = datetime.date.isoformat(datetime.date.today())
    status = "repairing"

    if execute_read_query(new_connection,
                          "select num from receipts order by num desc limit 1"):
        num = execute_read_query(new_connection,
                                 "select num from receipts order by num desc limit 1")[0][0] + 1
    else:
        num = 1

    date_of_repair = datetime.date.today() + datetime.timedelta(random.randint(1, 5))

    receipt = Receipt(num, repairing_device, date_of_receiving, [date_of_repair, initials, status])
    create_receipt = f"""
           INSERT INTO
             receipts (num, mark, operating_system, diagonal, date_of_manufacturing, description, 
             date_of_receiving, date_of_repair, initials, status)
           VALUES
             ({num}, '{mark}', '{operating_system}', {diagonal}, '{date_of_manufacturing}', 
             '{description}', '{date_of_receiving}', '{date_of_repair}', '{initials}', '{status}');
           """
    execute_query(new_connection, create_receipt)
    return receipt


def receipts_print(switch):
    """ Prints formatted info about receipts in console"""
    if isinstance(switch, list):
        temp = []
        for i in switch:
            temp.append(i[0])
        for i in temp:
            receipts_print(i)
    elif switch > 0 and execute_read_query(new_connection, f"SELECT num from receipts "
                                                           f"where num = {switch}"):
        print("\nReceipt info:")
        receipts = execute_read_query(new_connection, f"select * from receipts "
                                                      f"where num = {switch}")
        for receipt in receipts:
            if receipt[3] is not None:
                print("Type: TV")
                print(f"Mark: {receipt[1]},")
                print(f"Diagonal: {receipt[3]}")
            elif receipt[4] is not None:
                print("Type: Notebook")
                print(f"Mark: {receipt[1]}")
                print(f"Operating system: {receipt[2]}")
                print(f"Date of manufacturing: {receipt[4]}")
            else:
                print("Type: Phone")
                print(f"Mark: {receipt[1]}")
                print(f"Operating system: {receipt[2]}")
            print(f"Description: {receipt[5]}\nDate of receiving: {receipt[6]},\n"
                  f"Date of repair: {receipt[7]},\nInitials: {receipt[8]},\n"
                  f"Status: {receipt[9]}.")
    else:
        print("Unknown receipt number")


def administration_panel():
    """
    Shows an administration panel
    """

    login = input("Input login: ")
    password = input("Input password: ")

    if execute_read_query(new_connection, f"select login, password from admins "
                                          f"where login = '{login}' and password = '{password}'"):
        print("Login is successful.")
        while True:
            print("\nChoose action:")
            print("\nActions with admins:")
            print("  1. View admins list")
            print("  2. Remove an admin from admins list")
            print("  3. Add new admin")
            print("\nActions with receipts:")
            print("  4. Change repairing status")
            print("  5. Change date of repair")
            print("  6. View receipt information")

            print("\n7. Exit")
            switch = int(input())

            if switch == 1:
                view_admins_list()

            elif switch == 2:
                remove_admin()

            elif switch == 3:
                add_admin()

            elif switch == 4:
                change_repairing_status()

            elif switch == 5:
                change_date_of_repair()

            elif switch == 6:
                num = int(input("Input receipt number: "))
                receipts_print(num)

            elif switch == 7:
                break

    else:
        print("Login and/or password is incorrect")


def view_admins_list():
    """
    Shows list of admins
    """
    if not execute_read_query(new_connection, "select * from admins"):
        print("Admins list is empty")
        return 0

    admins = execute_read_query(new_connection, "select * from admins")
    for admin in admins:
        print(f"Login: {admin[0]}, Password: {admin[1]}, Initials: {admin[2]}")
    return 1


def remove_admin():
    """
    Remove admin from admins list
    """
    login = input("Enter login of admin you want to delete:")
    if execute_read_query(new_connection, f"select * from admins where login = '{login}'"):
        execute_query(new_connection, f"delete from admins where login = '{login}'")


def add_admin():
    """
    Adds an admin to admins list
    """
    login = input("Input new admin's login: ")
    password = input("Input new admin's password: ")
    initials = input("Input new admin's initials: ")
    execute_query(new_connection, f"insert into admins(login, password, initials) "
                                  f"values ('{login}', '{password}', '{initials}')")


def change_repairing_status():
    """Changes repairing status"""
    num = int(input("Input receipt number: "))
    receipts_print(num)
    if execute_read_query(new_connection, f"SELECT num from receipts "
                                          f"where num = {num}"):
        status = int(input("Choose the status: \n(1. Repairing  2. Done  3.Issued)\n"))
        execute_query(new_connection, f"update receipts "
                                      f"set status = '{Receipt.list_of_statuses[status - 1]}' "
                                      f"where num = {num}")


def change_date_of_repair():
    """
    Changes the date of repair
    """
    num = int(input("Input receipt number: "))
    receipts_print(num)
    if execute_read_query(new_connection, f"SELECT num from receipts "
                                          f"where num = {num}"):
        new_date = input("Input date in format \"YYYY-MM-DD\": ")
        execute_query(new_connection, f"update receipts "
                                      f"set date_of_repair = '{new_date}' "
                                      f"where num = {num}")


def receipts_search(info=None):
    """
    Searches for receipts matching given parameters
    """
    if info is None:
        info = input("Enter your receipt's number or initials: ")

    if info.isnumeric():
        info = int(info)
        if info > 0 and execute_read_query(new_connection, f"SELECT num from receipts "
                                                           f"where num = {info}"):
            receipts_print(info)
        else:
            print("Receipt with this number is not found")
    else:
        if execute_read_query(new_connection, f"SELECT num from receipts "
                                              f"where initials = '{info}'"):
            receipts_print(execute_read_query(new_connection, f"SELECT num from receipts "
                                                              f"where initials = '{info}'"))
        else:
            print("Receipts ordered with this initials are not found")


def menu():
    """ Menu of actions with receipts """
    while True:
        print("\nChoose an action:")
        print("1. Create repair request")
        print("2. Show info about receipt(s)")
        print("3. Show admin panel")
        print("4. Exit")

        switch = int(input())

        if switch == 1:
            create_repair_request()
        elif switch == 2:
            receipts_search()
        elif switch == 3:
            administration_panel()
        elif switch == 4:
            break
        else:
            print("Please, enter the correct number")
