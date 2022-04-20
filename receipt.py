"""
    Module with Receipt class
"""


class Receipt:
    """ Class "Receipt" """
    def __init__(self, num, repairing_device, date_of_receiving, date_of_repair, initials, status):
        self._num = num
        self._repairing_device = repairing_device
        self._date_of_receiving = date_of_receiving
        self._date_of_repair = date_of_repair
        self._initials = initials
        self._status = status

    list_of_products = ["Phone", "Notebook", "TV"]
    list_of_statuses = ["repairing", "done", "issued"]

    @property
    def initials(self):
        """ Returns customer intitals"""
        return self._initials

    def __str__(self):
        return f"Number of receipt: {self._num}, {self._repairing_device},\nDate of receiving: " \
               f"{self._date_of_receiving}, Date of repair: {self._date_of_repair}, " \
               f"Initials: {self._initials}, Status: {self._status} "
