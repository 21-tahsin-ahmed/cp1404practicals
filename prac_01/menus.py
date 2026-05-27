"""menu-driven program according to the pseudocode below:
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
name = input("Enter your name: ")
print("Here is the Menu: Q, H, G")
choice = input("Enter your choice: ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello, {name}")
    elif choice == "G":
        print("Goodbye, {name}")
    else:
        print("Invalid choice")
    choice = input("Enter your choice: ")
print("Finished.")

