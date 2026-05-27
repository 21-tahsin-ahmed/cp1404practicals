"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def get_grade(score):
    """Return the grade for a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    """Ask the user for score and print the grade result."""
    score = float(input("Enter score: "))
    result = get_grade(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")
    random_score = random.randint(0, 100)
    print(f"Random: {random_score} = {get_grade(random_score)}")


main()