class Vehicle:
    def __init__(self, cost, mileage):
        self.cost = cost
        self.mileage = mileage

    def show_vehicle_details(self):
        print(f"This is Vehicle from parent class of cost:{self.cost} and mileage of {self.mileage}")

class Car(Vehicle):
    def __init__(self,cost,mileage,color,tyres):
        super().__init__(cost, mileage)
        self.color = color
        self.tyres = tyres

    def show_car_details(self):
        print(f"This is car from child class of color:{self.color} and tyres:{self.tyres}")

I20 = Car(1100000, 20, "Red", 4)
I20.show_vehicle_details()
I20.show_car_details()