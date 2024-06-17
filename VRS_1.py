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
#Creating polymorphic methods for Car
    def rent(self):
        return self.get_rent()
    
    def retain(self):
        return self.get_retain()
    
    def maintenance(self):
        return self.get_maintenance()
        
class Bike(Vehicle):
    def __init__(self, vhname, rent, retain, maintenance):
        super().__init__(vhname, rent, retain, maintenance)
#Creating polymorphic methods for Bike    
    def rent(self):
        return self.get_rent() * 0.25
    
    def retain(self):
        return self.get_retain()
    
    def maintenance(self):
        return self.get_maintenance()
        
class Truck(Vehicle):
    def __init__(self, vhname, rent, retain, maintenance):
        super().__init__(vhname, rent, retain, maintenance)
#Creating polymorphic methods for Truck     
    def rent(self):
        return self.get_rent() * 1.5
    
    def retain(self):
        return self.get_retain()
    
    def maintenance(self):
        return self.get_maintenance()
    
        
class Customer:
#Creating private fields for customer data
    def __init__(self, cname, tag):
        self.__cname = cname
        self.__tag = tag      
#Creating the getters and setters for Customer data   
    def get_cname(self):
        return self.__cname

    def set_cname(self, name):
        self.__cname = cname

    def get_tag(self):
        return self.__tag

    def set_tag(self, tag):
        self.__tag = tag
        
          
class Rental:
    def __init__(self, customer, vehicle, days):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days
#Function to calculate rental fees based on vehicle type.
    def calculate_rental_fee(self):
        return (self.vehicle.rent() + self.vehicle.retain() + self.vehicle.maintenance()) * self.days
  
    
class Payment:
    def __init__(self, customer_data, rental, amount):
        self.customer_data = customer_data
        self.rental = rental
        self.amount = amount

    def process_payment(self):
        print(f"{self.customer_data.get_cname()} with tag {self.customer_data.get_tag()}")
        print(f"Your total payment is: ${self.amount} for the {self.rental.vehicle.get_vhname()}")
        
#Creating objects to test the system
car = [Car("Bugatti", 150, 50 ,12), Car("Toyota camry", 80, 35, 9)]

bike = [Bike("BMS", 90, 4, 2), Bike("Bianchi", 95, 6, 9)]

truck = [Truck("MAN", 200, 60, 15), Truck("Ford F-150", 250, 65, 20)]

customer1 = Customer("Miss Adwoaa", "01A")
car_rental = Rental(customer1, car[1], 2)
bike_rental = Rental(customer1, bike[0], 2)
customer1_carpayment = Payment(customer1, car_rental, car_rental.calculate_rental_fee())

