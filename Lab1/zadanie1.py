from datetime import datetime
import csv
import zadanie1_classes as classes

months = {1: "styczeń", 2: "luty", 3: "marzec", 4: "kwiecień", 5: "maj", 6: "czerwiec", 7: "lipiec",
          8: "sierpień", 9: "wrzesień", 10: "październik", 11: "listopad", 12: "grudzień"}


def reading_csv(file):
    with open(file, "r") as input_file:
        read_file = csv.reader(input_file, delimiter=",")
        list_read_elements = list(read_file)

        return list_read_elements


def parse_month(date_to_parse):
    return datetime.strptime(date_to_parse, '%Y-%m-%d').month


if __name__ == '__main__':
    employees = reading_csv("Employee.csv")
    received = reading_csv("ReceivedInvoice.csv")
    issued = reading_csv("IssuedInvoice.csv")

    c_employees = list()
    c_received = list()
    c_issued = list()

    for name, surname, salary in employees:
        o_employee = classes.Employee(name, surname, salary)
        c_employees.append(o_employee)

    for date, amount in received:
        o_received = classes.ReceivedInvoice(date, amount)
        c_received.append(o_received)

    for date, amount in issued:
        o_issued = classes.IssuedInvoice(date, amount)
        c_issued.append(o_issued)

    for month in range(1, 13):
        income = 0
        costs = 0

        for invoice in c_issued:
            if month == parse_month(invoice.date):
                income += int(invoice.amount)

        for invoice in c_received:
            if month == parse_month(invoice.date):
                costs += int(invoice.amount)

        for employee in c_employees:
            costs += int(employee.salary)

        print("Miesiąc: {}\nPrzychody: {}\nWydatki: {}\nBilans: {}\n".format(months[month], income, costs, income - costs))
