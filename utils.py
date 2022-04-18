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


def receipts_info():
    """ Gets info about receipt """

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
        print("3. Exit")

        switch = int(input())

        if switch == 1:
            create_repair_request()
        elif switch == 2:
            receipts_info()
        elif switch == 3:
            break
        else:
            print("Please, enter the correct number")
