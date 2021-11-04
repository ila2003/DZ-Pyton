n = int(input('введите число элементов'))
m = 1
spisok = []
while n >= m:
    spisok.append(input('Введите элемент '+str(m)))
    m = m + 1
print(spisok)


m = 1
while n >= m:
    tmp = spisok[m-1]
    spisok[m-1] = spisok[m]
    spisok[m] = tmp
    m = m + 2


print('Поменяный список')
print(spisok)


