from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, pid, pname, cat, quantity, unit, price):
        self.pid = pid
        self.pname = pname
        self.cat = cat
        self.quan = quantity
        self.unit = unit
        self.price = price

    @abstractmethod
    def calculateGst(self):
        pass
