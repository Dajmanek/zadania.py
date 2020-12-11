try:
    readFile = open("plik.txt", "r")
    lines = readFile.readlines()
    readFile.close()
except IOError as e:
    print(e)
    print("Blad podczas odczytu pliku \"plik.txt\"")
    exit()
try:
    writeFile = open("plik1.txt", "w")
    writeFile.writelines(lines)
    writeFile.close()
except IOError as e:
    print(e)
    print("Blad podczas zapisu pliku \"plik1.txt\"")