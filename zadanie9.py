try:
    readFile = open("plik.txt", "r")
    lines = readFile.readlines()
    readFile.close()
except:
    print("Blad podczas odczytu pliku \"plik.txt\"")
    exit()
try:
    writeFile = open("plik1.txt", "w")
    writeFile.writelines(lines)
    writeFile.close()
except:
    print("Blad podczas zapisu pliku \"plik1.txt\"")