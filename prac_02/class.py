# import random
#
# length = int(input("Length: "))
# width = random.randint(1, length)
# area = length * width
# print(f"Area of {length} x {width} is {area}")

# def print_grid(number_of_rows, number_of_columns):
#      version 3
#     print(f"{'*' * number_of_columns}\n" * number_of_rows)
    # version 2
    # for i in range(number_of_rows):
    #     print("*" * number_of_columns)
#     # version 1
#     for i in range(number_of_rows):
#         for j in range(number_of_columns):
#             print("*", end="")
#         print()
#
# print_grid(3, 7)

"""module-level docstring"""
def main():
    name = input("Enter your name: ")
    while name == "":
        print("invalid name")
        name = input("Enter your name: ")
    print("Welcome to Python")
main()


