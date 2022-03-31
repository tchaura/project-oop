class Device:

    def __init__(self, mark, description, name):
        self._mark = mark
        self._description = description
        self._name = name

    def __str__(self):
        return f"Type of product: {self._name}, Mark: {self._mark}, Description: {self._description}"


class Phone(Device):

    def __init__(self, mark, os, description):
        super(Phone, self).__init__(mark, description, name="Phone")

        self._os = os

    def __str__(self):
        return f"{super().__str__()}, OS: {self._os}"


class Notebook(Device):

    def __init__(self, mark, os, dateofmanufacturing, description):
        super(Notebook, self).__init__(mark, description, name="Notebook")
        self._dateOfManufacturing = dateofmanufacturing
        self._os = os

    def __str__(self):
        return f"{super().__str__()}, OS: {self._os}, Date of manufacturing: {self._dateOfManufacturing}"


class TV(Device):

    def __init__(self, mark, diagonal, description):
        super(TV, self).__init__(mark, description, name="TV")
        self._diagonal = diagonal

    def __str__(self):
        return f"{super().__str__()}, Diagonal: {self._diagonal}"
