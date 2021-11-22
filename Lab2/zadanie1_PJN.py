import re

print("Podaj imię:")
name = str(input())
name_check = re.search(r'^[A-Z]', name)

print("Podaj nazwisko:")
surname = str(input())
surname_check = re.search(r'^[A-Z]', surname)

print("Podaj telefon:")
phone = str(input())
phone_check = re.search(r'^\([0-9]{2}\)[0-9]{3}\-[0-9]{2}\-[0-9]{2}$', phone)

print("Podaj kod pocztowy:")
code = str(input())
code_check = re.search(r'^[0-9]{2}\-[0-9]{3}$', code)

print("Podaj miasto:")
city = str(input())
city_check = re.search(r'^[A-Z]', city)

print("")

try:
    name_check.group()
except:
    print("Imię nie rozpoczyna się od dużej litery!")

try:
    surname_check.group()
except:
    print("Nazwisko nie rozpoczyna się od dużej litery!")

try:
    city_check.group()
except:
    print("Miasto nie rozpoczyna się od dużej litery!")

try:
    code_check.group()
except:
    print("Kod pocztowy jest w złym formacie!")

try:
    phone_check.group()
except:
    print("Telefon jest w złym formacie!")