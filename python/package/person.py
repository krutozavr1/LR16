import datetime
import sys
from datetime import date

def create_person(name, sign, date):
    """ creates person variable with its fields"""
    person = {
        'name': name,
        'sign': sign,
        'date': date,
    }
    return person

def show_sign(persons):
    """prints all persons with inputed sign"""
    selected_sign = input("What sign? ")
    date_format = "%d.%m.%Y"

    for person in persons:
        right_person_found = False
        if person['sign'] == selected_sign:
            print(person['name'], person['sign'], datetime.datetime.strptime(person['date'], date_format))
            right_person_found = True
        if not right_person_found:
            print("Нет людей со знаком ", selected_sign)