viruchka = int(input('Введите выручку'))
izderzki = int(input('Введите издержки'))
if viruchka < izderzki:
    print('Фирма работает в убыток')
else:
    print('Фирма работает с прибылью, рентабельность - ',(viruchka - izderzki)/viruchka*100,'%')
    sotr = int(input('Введите число сотрудников'))
    print('Прибыль на сотрудника равна - ', (viruchka-izderzki)/sotr)
    