"""
write a program to read a file and print
ONLY the lines that start with a #
"""
# FILENAME = "test.txt"
# in_file = open(FILENAME, "r")
# for line in in_file:
#     if line.startswith("#"):
#         print(line, end="")
# in_file.close()
"""Write code to read a file like this and print each part separately 
with the price formatted like currency"""
FILENAME = "guiter.txt"
in_file = open(FILENAME, "r")
for line in in_file:
    parts = [part.strip().replace("\\n", "") for part in line.split(",")]
    name = parts[0]
    year = parts[1]
    price = float(parts[2])
    print(f"{name} ({year}) - ${price:.2f}")
in_file.close()
