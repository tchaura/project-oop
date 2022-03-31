class Receipt:

    def __init__(self, num, typeofproduct, dateofreceiving, dateofrepair, initials, status):
        self._num = num
        self._typeOfProduct = typeofproduct
        self._dateOfReceiving = dateofreceiving
        self._dateOfRepair = dateofrepair
        self._initials = initials
        self._status = status

    listOfProducts = ["Phone", "Notebook", "TV"]
    listOfStatuses = ["repairing", "done", "issued"]

    @property
    def initials(self):
        return self._initials

    def __str__(self):
        return f"Number of receipt: {self._num}, {self._typeOfProduct}, Date of receiving: " \
               f"{self._dateOfReceiving}, Date of repair: {self._dateOfRepair}, Initials: {self._initials}, Status: " \
               f"{self._status} "
