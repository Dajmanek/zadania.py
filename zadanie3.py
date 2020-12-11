password = "haslo"
number_of_tires = 3
while True:
    print("Podaj haslo: ")
    if number_of_tires > 0:
        if input() == password:
            print("Gratulacje")
            break
    else:
        print("Niestety, proba odgadniecia hasla nie powiodla sie")
        break
    number_of_tires-=1