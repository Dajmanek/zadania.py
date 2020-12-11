def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


print_args("arg1", "arg2", key1="value1", key2="value2")


# parametr *others musi znajdować się na końcu
def person_print(name, last_name, age, *others):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


person_print("Damian", "Sternik", 21, "other1", "other2")
