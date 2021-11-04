stroka = input('Введите слова через пробел')
stroka_list = stroka.split(" ")
for el in stroka_list:
    print(el[:10])
