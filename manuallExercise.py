
# Exercise 1

# song = input("Enter the first line of your favourite song: ")

# print(len(song))

# start = int(input("Enter the starting index of your song: "))
# end = int(input("Enter the last index of your song: "))

# print(song)




# # Exercise 2

# print("1. SQUARE")
# print("2. TRIANGLE")
# number = int(input("Enter a number 1 or 2: "))


# if number == 1:
#     side = int(input("Enter length for one side of the object: "))
#     if side <= 20:
#         print("the side of the square you entered is: " + "LEFT HORIZONTAL: ")
#     else:
#         print("Invalid side length.")


# elif number == 2:
#     base = int(input("Enter the base of the object: "))
#     height = int(input("Enter the height of the object: "))
    
   
#     if 1 <= base <= 10 and 1 <= height <= 10:
#         print("the dimensions of the triangle you entered are: " + "TOP VERTICAL: ")
#     else:
#         print("Dimensions must be between 1 and 10.")


# else:
#     print("Invalid Number")



# # Exercise 3

# name = input("Enter your name: ")
# number = int(input("Enter a number: "))

# if number < 10:
#     for i in range(number):
#         print(name)
# else:
#     for i in range(3):
#         print("Too high")



# # Exercise 4
# for i in range(5, 0, -1):
#     print(i)





# Exercise 5

# def interest():
#     principal = float(input("Enter the principal amount: "))
#     duration = int(input("Enter duration"))
#     interest = (principal / 10) * duration
#     print(interest)   
# interest()




# Exercise 6

# people = []

# for i in range(4):
#     print(f"\nPerson {i+1}")

#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     shoe_size = int(input("Enter shoe size: "))

#     people.append({
#         "name": name,
#         "age": age,
#         "shoe_size": shoe_size
#     })

# print("\nNames and Ages")

# for person in people:
#     print("Name:", person["name"], "- Age:", person["age"])




# # Exercise 7

# import csv

# students = [
#     ["John", 18, "Male", "100"],
#     ["Mary", 19, "Female", "200"],
#     ["Peter", 20, "Male", "300"],
#     ["Grace", 18, "Female", "100"],
#     ["David", 21, "Male", "400"]
# ]

# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Name", "Age", "Gender", "Level"])
#     writer.writerows(students)

# print("students.csv has been created successfully.")




# # Exercise 8

# class Enemy:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"{self.name} attacks with power {self.power}")

# # Create object
# enemy1 = Enemy("Donald", 30)

# # Call the attack method
# enemy1.attack()





# # Exercise 9 (Bar Chart)
# import matplotlib.pyplot as plt

# languages = [
#     "Python",
#     "Java",
#     "C",
#     "C++",
#     "R",
#     "JavaScript",
#     "C#"
# ]

# popularity = [
#     100,
#     96.3,
#     94.4,
#     87.5,
#     81.5,
#     79.4,
#     74.5
# ]

# plt.bar(languages, popularity)

# plt.title("Popularity of Programming Languages (2019)")
# plt.xlabel("Programming Languages")
# plt.ylabel("Popularity")

# plt.show()