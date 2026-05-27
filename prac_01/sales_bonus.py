"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("(Put -1 to stop)Enter your sales: $"))
while sales >= 0:
    if sales < 1000:
        print(f"Your bonus is {(sales * 0.10):}")
    else:
        print(f"Your bonus is {(sales * 0.15):}")
    sales = float(input("(Put -1 to stop)Enter your sales: $"))
print("Thank you for using this program")
