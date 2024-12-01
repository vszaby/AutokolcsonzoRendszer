from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, reg_number, auto_type, rental_price):
        self.reg_number = reg_number
        self.auto_type = auto_type
        self.rental_price = rental_price

    @abstractmethod
    def __str__(self):
        pass
