# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance is {self.balance}.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds.")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance is {self.balance}.")


# # Create a Bank object
# account = Bank("Emmanuel", 5000)

# # Display account details
# print(f"Account Name: {account.name}")
# print(f"Current Balance: {account.balance}")

# # Deposit money
# account.deposit(2000)

# # Withdraw money
# account.withdraw(1500)

# # Try to withdraw more than the balance
# account.withdraw(10000)



class Cars:
    def __init__(self, name, model, colour, speed):
        self.name = name
        self.model = model
        self.colour = colour
        self.speed = speed

def car_details(car):
    print(f"{car.name} {car.model} {car.colour} {car.speed} km/h")

car1 = Cars("Toyota", "Corolla", "Red", 50)
car_details(car1)


car2 = Cars("Honda", "Civic", "Blue", 60)
car_details(car2)