from Rent import Rent
from datetime import datetime

class AutoRent:
    def __init__(self, name):
        self.name = name
        self.autos = []
        self.rents = []

    def auto_list(self):
        for auto in self.autos:
            print(auto)

    def auto_rent(self, reg_number, date, renter_name):
        try:
            rent_date = datetime.strptime(date, "%Y-%m-%d").date()
            if rent_date < datetime.today().date():
                print(f"A megadott dátum ({date}) nem lehet korábbi, mint a mai nap ({datetime.today().date()}).")
                return None
        except ValueError:
            print(f"A dátum formátuma helytelen! Használja a következőt: YYYY-MM-DD.")
            return None

        for rent in self.rents:
            if rent.auto.reg_number == reg_number and rent.date == date:
                print(f"Az autó ({reg_number}) már bérlés alatt van ezen a napon: {date}.")
                return None

        for auto in self.autos:
            if auto.reg_number == reg_number:
                rent = Rent(auto, date, renter_name)
                self.rents.append(rent)
                print(f"Sikeres bérlés: {auto.reg_number}, Bérlő: {renter_name}, Dátum: {date}, Bérlés ára: {auto.rental_price}")
                return auto.rental_price

        print("Az autó nem található.")
        return None

    def rent_cancel(self, reg_number, renter_name, date):
        for rent in self.rents:
            if rent.auto.reg_number == reg_number and rent.renter_name == renter_name and rent.date == date:
                self.rents.remove(rent)
                print(f"Bérlés lemondva: {reg_number}, Bérlő: {renter_name}, Dátum: {date}")
                return True

        for rent in self.rents:
            if rent.auto.reg_number == reg_number:
                if rent.renter_name != renter_name:
                    print(f"A bérlő neve nem egyezik.")
                    return False
                if rent.date != date:
                    print(f"A bérlés dátuma nem egyezik.")
                    return False

        print("A megadott bérlés nem található.")
        return False

    def rents_list(self):
        for rent in self.rents:
            print(rent)
