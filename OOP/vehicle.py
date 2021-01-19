class Vehicle:
    def __init__(self, make, model , year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f"{self.year} {self.make} {self.model}")

car = Vehicle("Ford", "F150", "2004")

car.print_info()

