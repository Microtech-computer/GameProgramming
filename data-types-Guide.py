# ==========================================================
# PYTHON DATA TYPES - BEGINNER TRAINING GUIDE
# ==========================================================

"""
WHAT IS A DATA TYPE?

A data type tells Python what kind of value is stored in a variable.

Think of it this way:

A variable is like a container.
The data type tells Python what is inside that container.

Examples:
    name = "John"      -> String
    age = 20           -> Integer
    height = 1.75      -> Float
    passed = True      -> Boolean
"""

print("=" * 50)
print("PYTHON DATA TYPES")
print("=" * 50)

# ==========================================================
# 1. STRING (str)
# ==========================================================

"""
A String stores text.

Strings are enclosed in:
    - Single quotes (' ')
    - Double quotes (" ")

Examples:
    "John"
    'Python'
"""

print("\n1. STRING (str)")

name = "Emmanuel"
course = 'Python Programming'

print(name)
print(course)

print(type(name))

# Common String Methods
print("\nCommon String Methods")

print(name.upper())      # Convert to uppercase
print(name.lower())      # Convert to lowercase
print(name.title())      # First letter capitalized
print(len(name))         # Length of string
print(name.replace("Emmanuel", "John"))

# ==========================================================
# 2. INTEGER (int)
# ==========================================================

"""
Integers are whole numbers.

Examples:
10
100
-25
0
"""

print("\n2. INTEGER (int)")

age = 25
salary = 50000

print(age)
print(salary)

print(type(age))

# Integer Arithmetic

print(age + 5)
print(age - 5)
print(age * 2)
print(age / 5)

# ==========================================================
# 3. FLOAT (float)
# ==========================================================

"""
Floats are numbers containing decimal points.

Examples:
10.5
3.14
100.75
"""

print("\n3. FLOAT (float)")

height = 1.75
price = 2500.99

print(height)
print(price)

print(type(height))

# ==========================================================
# 4. BOOLEAN (bool)
# ==========================================================

"""
Boolean has only TWO values:

True
False

Used in decision making.
"""

print("\n4. BOOLEAN (bool)")

is_student = True
is_married = False

print(is_student)
print(is_married)

print(type(is_student))

# ==========================================================
# 5. LIST (list)
# ==========================================================

"""
A List stores multiple values.

Characteristics

✔ Ordered
✔ Can be changed (Mutable)
✔ Allows duplicates
"""

print("\n5. LIST (list)")

fruits = ["Apple", "Orange", "Banana"]

print(fruits)

print(type(fruits))

print(fruits[0])

fruits.append("Mango")

print(fruits)

fruits.remove("Orange")

print(fruits)

# ==========================================================
# 6. TUPLE (tuple)
# ==========================================================

"""
Tuple stores multiple values.

Characteristics

✔ Ordered
✔ Cannot be changed (Immutable)
✔ Allows duplicates
"""

print("\n6. TUPLE (tuple)")

colors = ("Red", "Green", "Blue")

print(colors)

print(type(colors))

print(colors[1])

# ==========================================================
# 7. SET (set)
# ==========================================================

"""
Set stores unique values.

Characteristics

✔ Unordered
✔ No duplicates
✔ Mutable
"""

print("\n7. SET (set)")

numbers = {1,2,3,2,1,4}

print(numbers)

print(type(numbers))

numbers.add(10)

print(numbers)

# ==========================================================
# 8. DICTIONARY (dict)
# ==========================================================

"""
Dictionary stores data in key:value pairs.

Example

Name  -> John
Age   -> 20
Course -> Python
"""

print("\n8. DICTIONARY (dict)")

student = {
    "name":"John",
    "age":20,
    "course":"Computer Science"
}

print(student)

print(type(student))

print(student["name"])

print(student["age"])

student["age"] = 21

print(student)

# ==========================================================
# 9. NONE TYPE
# ==========================================================

"""
None means

"No value"

It is commonly used when a variable
does not yet contain data.
"""

print("\n9. NONE TYPE")

result = None

print(result)

print(type(result))

# ==========================================================
# TYPE CONVERSION
# ==========================================================

"""
Sometimes we need to convert one data type into another.

Python provides:

int()
float()
str()
bool()
list()
tuple()
set()
"""

print("\nTYPE CONVERSION")

text = "100"

print(text)
print(type(text))

number = int(text)

print(number)
print(type(number))

decimal = float(text)

print(decimal)
print(type(decimal))

number2 = 500

word = str(number2)

print(word)

print(type(word))

print(bool(1))
print(bool(0))
print(bool("Python"))
print(bool(""))

# ==========================================================
# CHECKING DATA TYPES
# ==========================================================

print("\nCHECKING DATA TYPES")

A = 10
B = 20.5
C = "Hello"
D = False
E = [1,2,3]

print(type(A))
print(type(B))
print(type(C))
print(type(D))
print(type(E))

# ==========================================================
# SUMMARY
# ==========================================================

print("\nSUMMARY")

print("str      -> Text")
print("int      -> Whole Numbers")
print("float    -> Decimal Numbers")
print("bool     -> True or False")
print("list     -> Ordered, Mutable")
print("tuple    -> Ordered, Immutable")
print("set      -> Unordered, Unique")
print("dict     -> Key : Value")
print("NoneType -> No Value")

# ==========================================================
# PRACTICE EXERCISES
# ==========================================================

"""
Exercise 1
Create a string variable called school.

Exercise 2
Create an integer variable called age.

Exercise 3
Create a float variable called salary.

Exercise 4
Create a boolean variable called is_employed.

Exercise 5
Create a list of five programming languages.

Exercise 6
Create a tuple containing the days of the week.

Exercise 7
Create a set containing numbers from 1 to 5.

Exercise 8
Create a dictionary containing:
Name
Age
Department

Exercise 9
Print the data type of every variable.

Exercise 10
Convert the string "250" into an integer.
"""

print("\nEnd of Data Types Lesson.")