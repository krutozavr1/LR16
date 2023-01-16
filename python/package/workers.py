import datetime
import sys
from datetime import date

def display_list_of_workers(persons):
    """ prints charicteristics of all persons"""
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)

    print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "No",
            "Ф.И.О.",
            "Знак",
            "Дата рождения"
        )
    )
    print(line)

    for idx, worker in enumerate(persons, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                worker.get('name', ''),
                worker.get('sign', ''),
                worker.get('date', 0)
            )
        )
    print(line)