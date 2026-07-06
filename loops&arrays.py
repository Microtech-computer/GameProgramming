# ============================================================
# PYTHON LOOPS AND ARRAYS (LISTS) - BEGINNER TRAINING GUIDE
# ============================================================

"""
LOOPS

A loop is used when you want to repeat a task multiple times.

Instead of writing:

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

You can use a loop.

Python has two main loops:

1. for loop
2. while loop
"""

# ============================================================
# FOR LOOP
# ============================================================

print("\n========== FOR LOOP ==========")

"""
A for loop repeats a block of code a fixed number of times.

Syntax

for variable in sequence:
    code
"""

for number in range(5):
    print(number)

"""
Output

0
1
2
3
4

Notice that range(5) starts from 0.
"""

# ---------------------------------------

print("\nNumbers from 1 to 10")

for number in range(1, 11):
    print(number)

# ---------------------------------------

print("\nEven Numbers")

for number in range(2, 21, 2):
    print(number)

"""
range(start, stop, step)

start = first number

stop = last number + 1

step = how many numbers to jump
"""

# ---------------------------------------

print("\nOdd Numbers")

for number in range(1, 20, 2):
    print(number)

# ============================================================
# WHILE LOOP
# ============================================================

print("\n========== WHILE LOOP ==========")

"""
A while loop repeats as long as a condition is True.

Syntax

while condition:
    code
"""

count = 1

while count <= 5:
    print(count)
    count += 1

"""
Always increase the counter.

Otherwise the loop will never stop.
"""

# ============================================================
# NESTED LOOP
# ============================================================

print("\n========== NESTED LOOP ==========")

for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()

# ============================================================
# BREAK
# ============================================================

print("\n========== BREAK ==========")

for number in range(1,11):

    if number == 5:
        break

    print(number)

"""
break immediately stops the loop.
"""

# ============================================================
# CONTINUE
# ============================================================

print("\n========== CONTINUE ==========")

for number in range(1,11):

    if number == 5:
        continue

    print(number)

"""
continue skips the current iteration.
"""

# ============================================================
# LISTS (ARRAYS)
# ============================================================

"""
Python does not have traditional arrays like Java or C.

Instead, Python uses LISTS.

Lists can store:

Numbers
Strings
Booleans
Objects
Mixed data
"""

print("\n========== LIST OF NUMBERS ==========")

numbers = [10,20,30,40,50]

print(numbers)

# First item
print(numbers[0])

# Last item
print(numbers[-1])

# ============================================================

print("\n========== LIST OF STRINGS ==========")

names = ["John","Peter","Mary","James"]

print(names)

print(names[2])

# ============================================================

print("\n========== MIXED LIST ==========")

student = [

    "John",

    20,

    True,

    3.75

]

print(student)

# ============================================================

print("\n========== ADDING ITEMS ==========")

fruits = ["Apple","Orange"]

print(fruits)

fruits.append("Banana")

print(fruits)

fruits.insert(1,"Mango")

print(fruits)

# ============================================================

print("\n========== REMOVING ITEMS ==========")

colors = ["Red","Blue","Green","Black"]

print(colors)

colors.remove("Blue")

print(colors)

colors.pop()

print(colors)

# ============================================================

print("\n========== CHANGING ITEMS ==========")

cars = ["Toyota","Honda","BMW"]

print(cars)

cars[1] = "Mercedes"

print(cars)

# ============================================================

print("\n========== LIST LENGTH ==========")

numbers = [5,10,15,20,25]

print(len(numbers))

# ============================================================

print("\n========== LOOP THROUGH A LIST ==========")

numbers = [10,20,30,40,50]

for number in numbers:
    print(number)

# ============================================================

print("\n========== LOOP THROUGH STRINGS ==========")

names = ["John","Mary","Peter","Paul"]

for name in names:
    print(name)

# ============================================================

print("\n========== SUM OF ALL NUMBERS ==========")

numbers = [10,20,30,40,50]

total = 0

for number in numbers:
    total += number

print("Total =", total)

# ============================================================

print("\n========== FIND LARGEST NUMBER ==========")

numbers = [25,60,15,90,30]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print("Largest =", largest)

# ============================================================

print("\n========== SEARCH FOR A VALUE ==========")

numbers = [10,20,30,40,50]

search = 30

if search in numbers:
    print("Found")
else:
    print("Not Found")

# ============================================================

print("\n========== 2D LIST ==========")

matrix = [

    [1,2,3],

    [4,5,6],

    [7,8,9]

]

print(matrix)

print(matrix[0])

print(matrix[1][2])

# ============================================================

print("\n========== LOOP THROUGH 2D LIST ==========")

for row in matrix:

    for value in row:

        print(value, end=" ")

    print()

# ============================================================
# PRACTICE EXERCISES
# ============================================================

"""
Exercise 1
Print numbers from 1 to 100.

Exercise 2
Print all even numbers from 2 to 100.

Exercise 3
Print all odd numbers from 1 to 99.

Exercise 4
Create a list containing 10 numbers.

Exercise 5
Print every number in the list.

Exercise 6
Find the largest number.

Exercise 7
Find the smallest number.

Exercise 8
Calculate the total of all numbers.

Exercise 9
Calculate the average.

Exercise 10
Create a list of five students and print each student's name.
"""

print("\nEnd of Lesson")