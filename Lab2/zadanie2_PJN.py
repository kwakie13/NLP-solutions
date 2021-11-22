import re

with open("file.csv", "r") as file:
    lines = file.readlines()

    print("Błędne wiersze z pliku CSV:")

    for line in lines:
        checker = re.search(r"^.+\;\d+\;\d+\n$", line)

        try:
            checker.group()
        except:
            print(line)
