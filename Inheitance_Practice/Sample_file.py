from Single_Inheritance import Vehicle

class Sedan(Vehicle):
    def __init__(self,cost,mileage,sedan_name):
        super().__init__(cost, mileage)
        self.sedan_name = sedan_name

verna=Sedan(15000000,18,"Verna")
verna.show_vehicle_details()
