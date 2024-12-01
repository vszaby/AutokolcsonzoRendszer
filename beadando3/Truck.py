from Auto import Auto

class Truck(Auto):
    def __init__(self, reg_number, model, rental_price, capacity):
        super().__init__(reg_number, "teherautó", rental_price)
        self.model = model
        self.capacity = capacity

    def __str__(self):
        return f"{self.auto_type}, {self.reg_number}, {self.model}, {self.capacity} kg teherbírás, {self.rental_price} Ft/nap"
