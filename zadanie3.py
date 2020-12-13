password = "haslo"
number_of_tires = 3
for i in range(number_of_tires):
    if input() == password:
        print("Gratulacje")
        break
else:
    print("Niestety, proba odgadniecia hasla nie powiodla sie")