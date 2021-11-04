n = int(input('Введите число'))
maxcifra = 0
while n > 0:
    if n % 10 > maxcifra:
        maxcifra = n % 10
    n = n // 10

print('Максимальная цифра', maxcifra )
