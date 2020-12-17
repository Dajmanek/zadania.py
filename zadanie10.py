import re

bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!'''

# 1 rozwiązanie
word_list = re.sub("[-.?!]", "", re.sub("\n", " ", bridge_of_death)).split(" ")
filtered_word_list = list(filter(lambda element: len(element) >= 4, word_list))
print(filtered_word_list)

# 2 rozwiązanie
pattern = re.compile(r'[a-zA-ZąćęłńóśźżĄĘŁŃÓŚŹŻ]{4,}')
print(list(pattern.findall(bridge_of_death)))
