file = open("plik.txt", "w+")
file.writelines(["linia 1\n", "linia 2"])
file.seek(0)
print([line.rstrip("\n") for line in file.readlines()])
file.close()