from Auto import Auto

class Car(Auto):
    def __init__(self, reg_number, model, rental_price, seats):
        super().__init__(reg_number, "személygépkocsi", rental_price)
        self.model = model
        self.seats = seats

    def __str__(self):
        return f"{self.auto_type}, {self.reg_number}, {self.model}, {self.seats} ülés, {self.rental_price} Ft/nap"
