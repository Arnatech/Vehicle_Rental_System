from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, vhname, rent, retain, maintenance):
#Creating private fields for Vehicle class
        self.__vhname = vhname 
        self.__rent = rent
        self.__retain = retain
        self.__maintenance = maintenance 
    
#Defining the abstruct methods
    @abstractmethod
    def rent(self):
        pass
    
    @abstractmethod
    def retain(self):
        pass
    
    @abstractmethod
    def maintenance(self):
        pass
    
#Creating the getter and setter methods for vehicle data
    def get_vhname(self):
        return self.__vhname

    def set_vhname(self, vhname):
        self.__vhname = vhname

    def get_rent(self):
        return self.__rent

    def set_rent(self, rent):
        self.__rent = rent

    def get_retain(self):
        return self.__retain

    def set_retain(self, retain):
        self.__retain = retain

    def get_maintenance(self):
        return self.__maintenance

    def set_maintenance(self, maintenance):
        self.__maintenance = maintenance
    
#Creating subclasses with Vehicle as the parent class of the classes Car, Bike and Truck as child classes
class Car(Vehicle):
    def __init__(self, vhname, rent, retain, maintenance,):
        super().__init__(vhname, rent, retain, maintenance)
#Creating polymorphic method for Car
    def rent(self):
        return self.get_rent()
    
    def retain_vehicle():
        return self.get_retain()
    
    def perform_maintenance():
        return self.get_maintenance()
        
class Bike(Vehicle):
    def __init__(self, vhname, rent, retain, maintenance,):
        super().__init__(vhname, rent, retain, maintenance)
#Creating polymorphic method for Bike    
    def rent(self):
        return self.get_rent() * 0.25
    
    def retain(self):
        return self.get_retain()
    
    def maintenance(self):
        return self.get_maintenance()
        
class Truck(Vehicle):
    def __init__(self, vhname, rent, retain, maintenance, days):
        super().__init__(vhname, rent, retain, maintenance, days)
#Creating polymorphic method for Truck     
    def rent(self):
        return self.get_rent() * 1.5
    
    def retain(self):
        return self.get_retain()
    
    def maintenance(self):
        return self.get_maintenance
        
class Customer:
    def __init__(self, cname, tag):
        self.__cname = cname
        self.__tag = tag
        
#Creating the getters and setters for Customer data   
    def get_name(self):
        return self.__cname

    def set_name(self, name):
        self.__name = name

    def get_tag(self):
        return self.__tag

    def set_tag(self, tag):
        self.__tag = tag

    
        
    
class Rental:
    def __init__(self, customer, vehicle, days):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days

    def calculate_rental_fee(self):
        return (self.vehicle.rent() + self.vehicle.retain() + self.vehicle.maintanence()) * self.rental_period
    
# class Payment



Adwoaa_car = 
print(Adwoaa_car.get_vhname()) 



