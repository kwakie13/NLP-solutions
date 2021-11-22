class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary


class ReceivedInvoice:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount


class IssuedInvoice:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount
