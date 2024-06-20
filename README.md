# **Overview:**

This code implements a vehicle rental system using object-oriented programming principles in Python. The system is designed to handle different types of vehicles (Cars, Bikes, Trucks) and calculate rental fees based on various parameters such as rent, retain, and maintenance costs. It also includes customer management and payment processing.

# **Classes and Structure**

The code defines the following main classes:

**_Vehicle (Abstract Base Class):_**

Vehicle is an abstract base class that defines the common properties and methods for all vehicles.
It includes private fields for vhname (vehicle name), rent, retain, and maintenance.
Abstract methods rent, retain, and maintenance must be implemented by subclasses.
Car, Bike, Truck (Subclasses of Vehicle):

Each subclass implements the abstract methods with specific behavior.

**_Car:_** Returns the rent as it is.

**_Bike:_** Rent is reduced to 25% of the base rent.

**_Truck:_** Rent is increased to 150% of the base rent.

**_Customer:_**

Manages customer data with private fields cname (customer name) and tag.
Includes getter and setter methods for accessing and modifying customer data.

_**Rental:**_

Links a customer to a vehicle and the number of rental days.
Calculates the total rental fee based on the vehicle type and rental period.

**Payment:**

Processes the payment for the rental.
Prints the payment details including the customer name, tag, and total amount.

# **How to Run the Code**

**Define Vehicle Objects:**

Create variables/lists of vehicle objects for cars, bikes, and trucks.

**Instantiate  customer, rental and payment objects**.

Create/instantiate a customer object with the customer's name and tag as the value of the parameters 'cname' and 'tag' in the customer class

Create a rental object linking the customer to a vehicle and specifying the number of rental days.

Create a payment object to help you calculate the rental fee and process the payment.


Here is an example of how to run the code:


# Creating objects to test the system

car = [Car("Bugatti", 150, 50 ,12), Car("Toyota Camry", 80, 35, 9)]

bike = [Bike("BMS", 90, 4, 2), Bike("Bianchi", 95, 6, 9)]

truck = [Truck("MAN", 200, 60, 15), Truck("Ford F-150", 250, 65, 20)]

# Testing for customer
customer = Customer("Miss Adwoaa", "01A")

car_rental = Rental(customer, car[1], 2)

customer_carpayment = Payment(customer, car_rental, car_rental.calculate_rental_fee())

customer_carpayment.process_payment()

This example creates a customer, links them to a car rental for 2 days, calculates the rental fee, and processes the payment, displaying the payment details.





