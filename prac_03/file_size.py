def get_line_count(filename):
    """Open a file and return the number of lines in it."""
    with open(filename, "r") as file:
        return len(file.readlines())


def main():
    """Ask user for filenames and print line counts until empty input."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            line_count = get_line_count(filename)
            print(f"{filename} has {line_count} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


main()