try:
    with open("plik.txt", "r") as readFile:
        with open("plik1.txt", "w") as writeFile:
            writeFile.writelines(readFile.readlines())
except IOError as e:
    print(e)
