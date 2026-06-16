# 1
# name = input("Enter your name: ")
# file = open("name.txt", "w")
# file.write(name)
# file.close()

# 2
# file = open('name.txt', 'r')
# print(file.read())
# file.close()

# 3
# file = open("numbers.txt", "r")
# number_1 = int(file.readline())
# number_2 = int(file.readline())
# file.close()
#
# total = number_1 + number_2
# print(f"{number_1} + {number_2} = {total}")

# 4
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(f"Total: {total}")