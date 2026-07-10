
# # for loop

# numbers = [1, 2, 3, 4, 100]
# count = numbers[0]
# for number in numbers:
#    if number > count:
#        count = number
# print(count / len(numbers))



# whileloop
# number = int(input("Enter a number (1-10): "))

# while number > 10:
#     print("Invalid number")
   
#     number = int(input("Enter a number (1-10): "))

# print("Valid number")


# cours = input("Enter a cours: ")
# score = int(input("Enter score: "))
# ca = int(input("Enter CA Score"))
# cu = int(input("Enter total credit units: "))
# average = score + ca / cu
# A = 75
# B = 55
# C = 45
# D = 30


# if average >= A:
#     (print("A"))

# elif average >= B:
#     (print("B"))


# elif average >= C:
#     (print("C"))

# elif average >= D:
#     (print("D"))
# else:
#     (print("F"))





# SET DATA STRUCTURE

courses = {
   "Course": "English", "Grade": "A",
   "Course": "English", "Grade": "A",
   "Course": "English", "Grade": "A",
   "Course": "English", "Grade": "A",
   "Course": "English", "Grade": "A",
   "Course": "English", "Grade": "A",
   "Course": "English", "Grade": "A",
   "Course": "English", "Grade": "A",
   "Course": "English", "Grade": "A",
}

for course in courses:
    print(course, courses[course])





# # # LIST DATA STRUCTURE
# #     courses = [
# #     {"course": "English", "grade": "A"},
# #     {"course": "Mathematics", "grade": "B"},
# #     {"course": "Biology", "grade": "A"},
# #     {"course": "Geography", "grade": "C"},
# # ]

# # for item in courses:
# #     print(item["course"], item["grade"])





# # DICTIONARY DATA STRUCTURE
#     courses = {
#     "course": [
#         "English",
#         "Mathematics",
#         "Biology",
#         "Geography"
#     ],
    
#     "grade": [
#         "A",
#         "B",
#         "A",
#         "C"
#     ]
# }

# for i in range(len(courses["course"])):
#     print(courses["course"][i], courses["grade"][i])