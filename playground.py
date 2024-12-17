import keyword

#

class car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = car(make="nissan", model="sk")
print(my_car.make)
print(my_car.model)
