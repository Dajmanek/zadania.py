password = "haslo"
number_of_tries = 3
for i in range(number_of_tries):
    if input() == password:
        print("Gratulacje")
        break
else:
    print("Niestety, proba odgadniecia hasla nie powiodla sie")