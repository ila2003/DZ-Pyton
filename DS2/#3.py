n = int(input('введите номер месяца'))
vremenagoda = ['зима', 'весна', 'лето', 'осень']
if n<3 or n==12: print(vremenagoda[0])
if n>2 and n<6: print(vremenagoda[1])
if n>5 and n<9: print(vremenagoda[2])
if n>8 and n<12: print(vremenagoda[3])