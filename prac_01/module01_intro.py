# name = input("Enter your name: ")
# print("Hello", name)
"""pseudocode(algorithm)

get monthly_cost 
yearly_cost = monthly_cost * 12
return yearly_cost
"""
# monthly_cost = float(input("Enter your monthly cost: "))
# yearly_cost = monthly_cost * 12
# print(f"Your yearly tv streaming cost is ${yearly_cost:.2f}")

"""

0-4 = baby, 5-17 = child, 18-65 = adult, 66+ = old
"""
# age = int(input("Enter your age: "))
# while age < 0 or age > 120: # input is bad
#     print("Invalid age")
#     age = int(input("Enter your age: "))
# if age < 5:
#     category = "baby"
# elif age < 18:
#     category = "child"
# elif age < 65:
#     category = "adult"
# else:
#     category = "old"
# print(f"Your age {age} is considered {category}")


"""Practice"""
# name = input("Enter your name: ")
# while name.strip() == "": # .strip() removes all leading/trailing spaces before checking
#     print("Invalid name")
#     name = input("Enter your name: ")
# print(f"Your name is {name}, hello")

# SECRET = 6
# number = int(input("Guess the secret number between 1 and 10: "))
# while number != SECRET:
#     print("Wrong guess. Try again.")
#     number = int(input("Guess the secret number between 1 and 10: ", ))
# print("Congrats you gussed it")

# total = 0
# n = int(input("How many ages to enter: "))
# for i in range(n):
#     age = int(input("Enter age: "))
#     total += age
# average = total / n
# print(f"Total age is {total} and the average age is {average}")

total_age = 0
number_of_people = 0
age = int(input("Enter age: "))
while age > 0: # no negative
    total_age = total_age + age
    number_of_people = number_of_people + 1
    age = int(input("Enter age: "))
if number_of_people == 0:
    print("No total or average")
else:
    average = total_age / number_of_people
    print(f"Average age {number_of_people} people is {average:.2f}")