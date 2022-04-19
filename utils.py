"""
    Module with functions
"""
import datetime
import random
from devices import Phone, TV, Notebook
from receipt import Receipt


receiptsdict = {1: Receipt(1, Phone("Xiaomi", "Android", "MIUI is shit pls help"),
                           "2022-02-24", "2022-02-26", "Antony", Receipt.list_of_statuses[2]),
                2: Receipt(2, TV("Samsung", "27", "Screen is white"), "2022-03-05",
                           "2022-03-11", "Andrey", Receipt.list_of_statuses[2]),
                3: Receipt(3, Notebook("Asus", "Windows 11", "2012-03-02", "Doesn't start"),
                           "2022-02-13", "2022-02-15", "Dmitry", Receipt.list_of_statuses[2]),
                4: Receipt(4, TV("LG", 40, "Doesn't work"), "2021-04-25", "2021-04-30", "Vitally",
                           Receipt.list_of_statuses[2]),
                5: Receipt(5, Phone("Samsung", "Android", "Works slowly"),
                           "2021-07-15", "2021-07-17", "Max", Receipt.list_of_statuses[2])}


def create_repair_request():
    """ Creates repair request """
    initials = input("Please, input your initials: ")

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

    if not receiptsdict.keys():
        num = 1
    else:
        num = len(receiptsdict.keys()) + 1

    date_of_repair = datetime.date.today() + datetime.timedelta(random.randint(1, 5))

    receipt = Receipt(num, repairing_device, date_of_receiving, date_of_repair, initials, status)

    receiptsdict[num] = receipt
    return receiptsdict[num]


def receipts_print(switch):
    """ Prints receipts in console"""
    if switch == 0:
        for value in receiptsdict.values():
            print(f"\nReceipt info: {value}")
    elif switch > 0 and switch in receiptsdict:
        print(f"\nReceipt info: {receiptsdict.get(switch)}")
    else:
        print("Unknown receipt number")


def administration_panel():
    """
    Shows an administration panel
    """

    _admins_dict = {"admin": ["password", "Ivanov Ivan Ivanovich"]}

    login = input("Input login: ")
    password = input("Input password: ")

    if login in _admins_dict and _admins_dict.get(login)[0] == password:
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
                view_admins_list(_admins_dict)

            elif switch == 2:
                remove_admin(_admins_dict)

            elif switch == 3:
                add_admin(_admins_dict)

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


def view_admins_list(_admins_dict):
    """
    Shows list of admins
    :param _admins_dict:
    """
    if len(_admins_dict) == 0:
        print("Admins list is empty")
        return 0

    counter = 1
    for i, k in _admins_dict.items():
        print(f"{counter}. Login: {i}, Password: {k[0]}, Initials: {k[1]}")
        counter += 1
        return 1


def remove_admin(_admins_dict):
    """
    Remove admin from admins list
    :param _admins_dict:
    """
    counter = int(input("Enter the number:"))
    _admins_dict.pop(list(_admins_dict.keys())[counter - 1])


def add_admin(_admins_dict):
    """
    Adds an admin to admins list
    :param _admins_dict:dict
    """
    login = input("Input new admin's login: ")
    password = input("Input new admin's password: ")
    initials = input("Input new admin's initials: ")
    _admins_dict[login] = [password, initials]


def change_repairing_status():
    """Change repairing status"""
    num = int(input("Input receipt number: "))
    if num in receiptsdict:
        status = int(input("Choose the status: \n(1. Repairing  2. Done  3.Issued)\n"))
        receiptsdict.get(num).status = Receipt.list_of_statuses[status - 1]
    else:
        print("Unknown number")


def change_date_of_repair():
    """
    Changes the date of repair
    """
    num = int(input("Input receipt number: "))
    if num in receiptsdict:
        new_date = input("Input date in format \"YYYY-MM-DD\": ")
        receiptsdict.get(num).date_of_repair = new_date
    else:
        print("Unknown number")


def receipts_info():
    """
    Gets info about receipt
    """
    info = input("Enter your receipt's number or initials: ")

    if info.isnumeric():
        info = int(info)
        if info in list(receiptsdict):
            receipts_print(info)
        else:
            print("Receipt with this number is not found")
    else:
        is_found = False
        for i in receiptsdict:
            if receiptsdict.get(i).initials == info:
                receipts_print(i)
                is_found = True
        if not is_found:
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
            receipts_info()
        elif switch == 3:
            administration_panel()
        elif switch == 4:
            break
        else:
            print("Please, enter the correct number")
