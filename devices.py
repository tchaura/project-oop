"""
    Module with device classes
"""


class Device:
    """ Class "Device" """

    def __init__(self, mark, description, name):
        self._mark = mark
        self._description = description
        self._name = name

    def __str__(self):
        return f"Type of product: {self._name}, Mark: {self._mark}, Description: " \
               f"{self._description}"


class Phone(Device):
    """ Class "Phone" """
    def __init__(self, mark, os, description):
        super().__init__(mark, description, name="Phone")
        self._os = os

    def __str__(self):
        return f"{super().__str__()}, OS: {self._os}"


class Notebook(Device):
    """ Class "Notebook" """
    def __init__(self, mark, os, date_of_manufacturing, description):
        super().__init__(mark, description, name="Notebook")
        self._date_of_manufacturing = date_of_manufacturing
        self._os = os

    def __str__(self):
        return f"{super().__str__()}, OS: {self._os}, Date of manufacturing: " \
               f"{self._date_of_manufacturing}"


class TV(Device):
    """ Class "TV" """
    def __init__(self, mark, diagonal, description):
        super().__init__(mark, description, name="TV")
        self._diagonal = diagonal

    def __str__(self):
        return f"{super().__str__()}, Diagonal: {self._diagonal}"
