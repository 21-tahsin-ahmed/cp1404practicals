MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the menu-driven score program."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Score {score} is {get_grade(score)}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")


def get_valid_score():
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Please enter a valid score.")
        score = float(input("Enter your score: "))
    return score


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


def show_stars(score):
    """Print stars equal to the score."""
    print("*" * int(score))


main()
