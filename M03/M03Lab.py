class Vehicle():

    def __init__(self,vehicleType):
        self.vehicleType=vehicleType
class Car(Vehicle):
    def __init__(self,year,make,model,doorCount,roof):
        super().__init__("Car")
        self.year = year
        self.make = make
        self.model = model
        self.doorCount = doorCount
        self.roof = roof
        
def makeCar():
    car = Car(input("What Year is the car?"),input("What Make is the car?"),input("What Model is the car?"),input("How many doors does the car have?"),input("What kind of roof?"))
    return car
def printCar(car):
    print("Vehicle Type:",car.vehicleType)
    print("Year:",car.year)
    print("Make:",car.make)
    print("Model:",car.model)
    print("Number of Doors:",car.doorCount)
    print("Type of roof:",car.roof)

printCar(makeCar())

