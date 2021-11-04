sec = int( input('введите время в секундах'))
chas = sec // 3600
min = (sec % 3600) // 60
sec = (sec % 3600) % 60
print(chas,':',min,':',sec)

