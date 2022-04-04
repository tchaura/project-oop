from devices import Phone, TV, Notebook
from receipt import Receipt
import datetime
import random

receiptsdict = {}


def create_repair_request():  # создание заявки на ремонт
    initials = input("Please, input your initials: ")

    print("Choose the type of product you want to repair: ")
    for i in range(len(Receipt.list_of_products)):
        print(f"{i + 1}. {Receipt.list_of_products[i]}")
    try:
        sw = Receipt.list_of_products[int(input()) - 1]
    except:
        return "Wrong number"

    mark = input("Input mark: ")
    description = input("Input description: ")

    repairing_device = None
    if sw == "Phone":
        os = input("Input OS: ")
        repairing_device = Phone(mark, os, description)

    if sw == "Notebook":
        os = input("Input OS: ")
        date_of_manufacturing = input("Input date of manufacturing in the format \"YYYY-MM-DD\": ")
        repairing_device = Notebook(mark, os, date_of_manufacturing, description)

    if sw == "TV":
        diagonal = input("Input diagonal: ")
        repairing_device = TV(mark, diagonal, description)

    date_of_receiving = datetime.date.isoformat(datetime.date.today())
    status = "repairing"

    if not receiptsdict.keys():
        num = 1
    else:
        num = len(receiptsdict.keys()) + 1

    date_of_repair = datetime.date.today() + datetime.timedelta(random.randint(1, 5))

    r = Receipt(num, repairing_device, date_of_receiving, date_of_repair, initials, status)

    receiptsdict[num] = r
    return receiptsdict[num]


def receipts_print(sw):  # вывод квитанций на экран
    if sw == 0:
        for i, k in receiptsdict.items():
            print(f"Receipt number: {i}, Info: {k}")
    elif sw > 0 and sw in receiptsdict.keys():
        print(f"Receipt number: {sw}, Info: {receiptsdict.get(sw)}")


def receipts_info():  # получение информации о квитанции
    print(list(receiptsdict.keys()))

    info = input("Enter your receipt's number or initials: ")

    if info.isnumeric():
        info = int(info)
        if info in list(receiptsdict.keys()):
            for i in receiptsdict.keys():
                if i == info:
                    print(receiptsdict[i])
        else:
            print("Receipt with this number is not found")
    else:
        isfound = False
        for i in receiptsdict.keys():
            if receiptsdict.get(i).initials == info:
                receipts_print(i)
                isfound = True
        if not isfound:
            print("Receipts ordered with this initials are not found")


def menu():  # меню действий
    print("Choose an action:")
    print("1. Create repair request")
    print("2. Show info about receipt(s)")

    sw = int(input())

    if sw == 1:
        create_repair_request()
    elif sw == 2:
        receipts_info()
    else:
        print("Please, enter the correct number")
        return 0
