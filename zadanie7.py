def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


print_args("arg1", "arg2", key1="value1", key2="value2")



def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

# Trzeba określić, że liczba 21 będzie przypisana do parametru age
person_print("Damian", "Sternik", "other1", "other2", age=21)
