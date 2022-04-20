"""
    Module with Receipt class
"""


class Receipt:
    """ Class "Receipt" """
    def __init__(self, num, repairing_device, date_of_receiving, arguments: list):
        self._num = num
        self._repairing_device = repairing_device
        self._date_of_receiving = date_of_receiving
        self._date_of_repair = arguments[0]
        self._initials = arguments[1]
        self._status = arguments[2]

    list_of_products = ["Phone", "Notebook", "TV"]
    list_of_statuses = ["repairing", "done", "issued"]

    @property
    def initials(self):
        """ Returns customer initials"""
        return self._initials

    @property
    def status(self):
        """Changes the status of receipt"""
        return self._status

    @status.setter
    def status(self, value):
        """Changes the status of receipt"""
        self._status = value

    @property
    def date_of_repair(self):
        """Changes the date of repair of receipt"""
        return self._date_of_repair

    @date_of_repair.setter
    def date_of_repair(self, value):
        """Changes the date of repair of receipt"""
        self._date_of_repair = value

    def __str__(self):
        return f"Number of receipt: {self._num}, {self._repairing_device},\nDate of receiving: " \
               f"{self._date_of_receiving}, Date of repair: {self._date_of_repair}, " \
               f"Initials: {self._initials}, Status: {self._status} "
