# def greet(name):
#     print("Helloe " + name + " Welcome to FULAFIA " )
# greet("Emmanuel Ajoo")





# def info(name, age, country):
#     print("Welcome, your name is " + name + "," " and you are " + age +" years old, " + " you lives in " + country)
# info("Emmanuel Ajoo", "20", "Nigeria")



def result(score, average):
    result = score/average
    if result >= 5.0:
        print("Congratulations, you have scored " +str(round(result, 0)) + " which is the requirement, visit: https://microtechniques.kesug.com for interview")
    else:
        print("Sorry, you have scored  " + str(round(result, 0)) + " which is below expectation, try again next time: ")
score = float(input("Enter Score: "))
average = float(input("Enter Average: "))
result(score, average)



