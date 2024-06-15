from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, vhname, rent, retain, maintenance):
#Creating private fields for Vehicle class
        self.__vhname = vhname 
        self.__rent = rent
        self.__retain = retain
        self.__maintenance = maintenance 
        
#Defining the abstruct methods
    @abstructmethod
    def rent(self):
        pass
    
    @abstructmethod
    def retain_vehicle(self):
        pass
    
    @abstructmethod
    def perform_maintenance(self):
        pass
    
#Creating the getter method
    def get_price(self):
        return self.__vhname, self.__maintenance, self.__retain
    
#Creating subclasses with Vehicle as the parent class of the classes Car, Bike and Truck 
class Car(Vehicle):
    def __init__(self, vhname, rent, retain, maintenance):
        super().__init__(vhname, rent, retain, maintenance)
        
class Bike(Vehicle):
    def __init__(self, vhname, rent, retain, maintenance):
        super().__init__(vhname, rent, retain, maintenance)
    def 
        if vhname == 'Bike':
            rent = rent * 0.25
        else:
            pass
        
class Truck(Vehicle):
    def __init__(self, vhname, rent, retain, maintenance):
        super().__init__(vhname, rent, retain, maintenance)
        
# class Customer

# class Rental
    
# class Payment



Adwoaa_car = Car('Bike', 50, 100, 20)
print(Adwoaa_car.get_price()) 



