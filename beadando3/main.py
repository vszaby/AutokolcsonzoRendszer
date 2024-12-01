from AutoRent import AutoRent
from Car import Car
from Truck import Truck
from datetime import datetime

class AutoRentSystem:
    def __init__(self):
        self._rent = AutoRent("AutoRent")
        self._init_data()

    def _init_data(self):
        self._rent.autos.append(Car("ABB-123", "Toyota Corolla", 10000, 5))
        self._rent.autos.append(Car("XXX-999", "Volkswagen Golf", 10000, 5))
        self._rent.autos.append(Truck("ZTT-885", "Mercedes Sprinter", 15000, 2000))

        self._rent.auto_rent("ABB-123", "2024-12-28", "Kovács Péter")
        self._rent.auto_rent("XXX-999", "2024-12-29", "Nagy Ádám")

    def user_interact(self):
        while True:
            print("\n=== Autókölcsönző ===")
            print("1. Autók listázása")
            print("2. Bérlések listázása")
            print("3. Autó bérlése")
            print("4. Bérlés lemondása")
            print("5. Kilépés")

            choice = input("Válasszon egy lehetőséget: ")

            if choice == "1":
                self._rent.auto_list()

            elif choice == "2":
                self._rent.rents_list()

            elif choice == "3":
                while True:
                    reg_number = input("Adja meg az autó rendszámát: ")
                    if any(auto.reg_number == reg_number for auto in self._rent.autos):
                        break
                    else:
                        print(f"Nincs ilyen rendszámú autó az adatbázisban: {reg_number}")

                while True:
                    date = input("Adja meg a bérlés dátumát (YYYY-MM-DD): ")
                    try:
                        rent_date = datetime.strptime(date, "%Y-%m-%d").date()
                        if rent_date < datetime.today().date():
                            print(f"A megadott dátum ({date}) nem lehet korábbi, mint a mai nap ({datetime.today().date()}).")
                        else:
                            break
                    except ValueError:
                        print("A dátum formátuma helytelen. Használja a következőt: YYYY-MM-DD.")

                renter_name = input("Adja meg a bérlő nevét: ")
                self._rent.auto_rent(reg_number, date, renter_name)

            elif choice == "4":
                while True:
                    reg_number = input("Adja meg az autó rendszámát: ")
                    if any(auto.reg_number == reg_number for auto in self._rent.autos):
                        break
                    else:
                        print(f"Nincs ilyen rendszámú autó az adatbázisban: {reg_number}")

                while True:
                    date = input("Adja meg a bérlés dátumát (YYYY-MM-DD): ")
                    try:
                        datetime.strptime(date, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("A dátum formátuma helytelen. Használja a következőt: YYYY-MM-DD.")

                renter_name = input("Adja meg a bérlő nevét: ")

                self._rent.rent_cancel(reg_number, renter_name, date)

            elif choice == "5":
                print("Kilépés a rendszerből.")
                break

            else:
                print("Érvénytelen választás!")

if __name__ == "__main__":
    autorent_system = AutoRentSystem()
    autorent_system.user_interact()