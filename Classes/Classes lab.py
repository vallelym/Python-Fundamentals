#Exercise One - Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print(f"Area: {rect.area()}")         
print(f"Perimeter: {rect.perimeter()}") 

# Exercise Two - Bank Account
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

account = BankAccount("123456789")
account.deposit(1000)
account.withdraw(500)
account.withdraw(600)

#Exercise Three - Car
class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self._year = year

car = Car("Toyota", "Corolla", 2020)

print(f"Make: {car.get_make()}")
print(f"Model: {car.get_model()}")
print(f"Year: {car.get_year()}")

car.set_make("Honda")
car.set_model("Civic")
car.set_year(2022)

print(f"Updated Make: {car.get_make()}")
print(f"Updated Model: {car.get_model()}")
print(f"Updated Year: {car.get_year()}")

#Exercise Four - Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def add_items(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Added {amount} items. New quantity is {self.quantity}.")
        else:
            print("Amount to add must be positive.")

    def remove_items(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            print(f"Removed {amount} items. New quantity is {self.quantity}.")
        elif amount > self.quantity:
            print("Cannot remove more items than are in inventory.")
        else:
            print("Amount to remove must be positive.")


product = Product("Laptop", 1000, 5)

print(f"Total value of the product: {product.total_value()}")  # Output: 5000

product.add_items(3)  
product.remove_items(2) 