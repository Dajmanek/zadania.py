from random import randint
import time

long_list = [randint(0, 3000) for element in range(1000000)]
szukana = -1

# ----- sposób 1 -----
print("----- sposób 1 -----")
czas_start = time.time()

if szukana in long_list:
    print("Liczba znajduję się w liście.")
else:
    print("Liczba nie znajduję się w liście")

czas = time.time() - czas_start
print('Czas trwania przeszukiwania:', czas)

# ----- sposób 2 -----
print("----- sposób 2 -----")
czas_start = time.time()

count = long_list.count(szukana)
if count:
     print("Liczba występuje na liście {} razy.".format(count))
else:
    print("Liczba nie znajduję się w liście")

czas = time.time() - czas_start
print('Czas trwania przeszukiwania:', czas)

# ----- sposób 3 -----
print("----- sposób 3 -----")
czas_start = time.time()

if long_list.count(szukana):
    print("Liczba występuje na liście {} razy.".format(long_list.count(szukana)))
else:
    print("Liczba nie znajduję się w liście")

czas = time.time() - czas_start
print('Czas trwania przeszukiwania:', czas)

# ----- sposób 4 -----
print("----- sposób 4 -----")
czas_start = time.time()
result = False
for i in long_list:
    if i == szukana:
        print("Liczba wystepuje na liscie.")
        result = True
        break
if ~result:
    print("Liczba nie znajduje się na liście")

czas = time.time() - czas_start
print('Czas trwania przeszukiwania:', czas)

# ----- sposób 5 -----
print("----- sposób 5 -----")
czas_start = time.time()
len_list = len(long_list)
for i in range(len_list):
    if long_list[i] == szukana:
        print("Liczba wystepuje na liscie.")
        break
    if i+1 == len_list:
        print("Liczba nie znajduje się na liście")

czas = time.time() - czas_start
print('Czas trwania przeszukiwania:', czas)