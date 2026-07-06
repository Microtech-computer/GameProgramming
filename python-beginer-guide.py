# ============================================================
# PYTHON FOR ABSSOLUTE BEGINNERS (PART 1)
# ============================================================

"""
This file is a classroom training guide.
Read the comments before each example and run the code section by section.
"""

print("Welcome to Python!")

# -------------------------
# LESSON 1: COMMENTS
# -------------------------

# This is a single-line comment.

"""
This is a multi-line comment.
Python ignores comments.
"""

# -------------------------
# LESSON 2: VARIABLES
# -------------------------

# Variables store values.

name = "Alice"      # String
age = 20            # Integer
height = 1.68       # Float
is_student = True   # Boolean

print(name)
print(age)
print(height)
print(is_student)

# -------------------------
# LESSON 3: DATA TYPES
# -------------------------

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# -------------------------
# LESSON 4: USER INPUT
# -------------------------

user = input("Enter your name: ")
print("Hello,", user)

# -------------------------
# LESSON 5: TYPE CASTING
# -------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", num1 + num2)

# -------------------------
# LESSON 6: OPERATORS
# -------------------------

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# -------------------------
# LESSON 7: COMPARISON OPERATORS
# -------------------------

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# -------------------------
# LESSON 8: LOGICAL OPERATORS
# -------------------------

x = 10
print(x > 5 and x < 20)
print(x > 20 or x < 20)
print(not(x > 5))

# -------------------------
# LESSON 9: IF STATEMENTS
# -------------------------

score = int(input("Enter your score: "))

if score >= 50:
    print("PASS")
else:
    print("FAIL")

# -------------------------
# EXERCISES
# -------------------------

# 1. Create variables for your name, age and state.
# 2. Ask the user for two numbers and multiply them.
# 3. Check whether a person's age is 18 or above.
