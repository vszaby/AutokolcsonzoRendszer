class Rent:
    def __init__(self, auto, date, renter_name):
        self.auto = auto
        self.date = date
        self.renter_name = renter_name

    def __str__(self):
        return f"Bérlés: {self.renter_name}, {self.auto.reg_number}, {self.date}, {self.auto.rental_price} Ft"
