def print_message():
    """matches name and surname and prints message """
    name = ""
    surname = ""

    def match_data(n, s):
        nonlocal name
        nonlocal surname
        name = n
        surname = s
        sample = f"Уважаемый {name} {surname}! Вы делаете работу по замыканиям функций."
        print(sample)

    return match_data