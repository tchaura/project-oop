from devices import Phone, TV, Notebook
from receipt import Receipt
import datetime
import random

receiptsdict = {}


def createrepairrequest():  # создание заявки на ремонт
    initials = input("Please, input your initials: ")

    print("Choose the type of product you want to repair: ")
    for i in range(len(Receipt.listOfProducts)):
        print(f"{i + 1}. {Receipt.listOfProducts[i]}")
    try:
        sw = Receipt.listOfProducts[int(input()) - 1]
    except:
        return "Wrong number"

    mark = input("Input mark: ")
    description = input("Input description: ")

    repairingdevice = None
    if sw == "Phone":
        os = input("Input OS: ")
        repairingdevice = Phone(mark, os, description)

    if sw == "Notebook":
        os = input("Input OS: ")
        dateofmanufacturing = input("Input date of manufacturing in the format \"YYYY-MM-DD\": ")
        repairingdevice = Notebook(mark, os, dateofmanufacturing, description)

    if sw == "TV":
        diagonal = input("Input diagonal: ")
        repairingdevice = TV(mark, diagonal, description)

    dateofreceiving = datetime.date.isoformat(datetime.date.today())
    status = "repairing"

    if not receiptsdict.keys():
        num = 1
    else:
        num = len(receiptsdict.keys()) + 1

    dateofrepair = datetime.date.today() + datetime.timedelta(random.randint(1, 5))

    r = Receipt(num, repairingdevice, dateofreceiving, dateofrepair, initials, status)

    receiptsdict[num] = r
    return receiptsdict[num]


def receiptsprint(sw):  # вывод квитанций на экран
    if sw == 0:
        for i, k in receiptsdict.items():
            print(f"Receipt number: {i}, Info: {k}")
    elif sw > 0 and sw in receiptsdict.keys():
        print(f"Receipt number: {sw}, Info: {receiptsdict.get(sw)}")


def receiptsinfo():  # получение информации о квитанции
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
                receiptsprint(i)
                isfound = True
        if not isfound:
            print("Receipts ordered with this initials are not found")


def menu():  # меню действий
    print("Choose an action:")
    print("1. Create repair request")
    print("2. Show info about receipt(s)")

    sw = int(input())

    if sw == 1:
        createrepairrequest()
    elif sw == 2:
        receiptsinfo()
    else:
        print("Please, enter the correct number")
        return 0
