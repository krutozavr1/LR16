#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from package import person, workers, docs

def main():
    persons = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и Имя? ")
            sign = input("Знак зодиака? ")
            date = input("Дата рождения? ")
            persons.append(person.create_person(name, sign, date))

            if len(persons) > 1:
                persons.sort(key=lambda item: item.get('sign', ''))

        elif command == 'list':
            workers.display_list_of_workers(persons)

        elif command == 'show sign':
            person.show_sign(persons)

        elif command == 'help':
            docs.provide_docs()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
