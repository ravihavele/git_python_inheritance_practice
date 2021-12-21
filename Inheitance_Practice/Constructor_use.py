class Car:
    def __init__(self, color, mileage, cost, tyres):
        self.color = color
        self.mileage = mileage
        self.cost = cost
        self.tyres = tyres

    def show_car_details(self):
        print(f"car color is {self.color}")
        print(f"car mileage is {self.mileage}")
        print(f"car cost is {self.cost}")
        print(f"car tyres is {self.tyres}")

I20 = Car("Red", 20, 1100000, 4)
I20.show_car_details()