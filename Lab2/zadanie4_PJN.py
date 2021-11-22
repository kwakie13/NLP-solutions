import re

with open("source.html", "r", encoding="UTF-8") as file:
    lines = file.readlines()

    addresses = list()

    for line in lines:
        found = re.findall('[\w.+]+@[\w]+\.[\w.]+', line)
        addresses = addresses + found

    addresses = list(dict.fromkeys(addresses))

    print(addresses)
