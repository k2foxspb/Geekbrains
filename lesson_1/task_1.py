duration= int(input('введите время в секундах\n'))
count_day = 0
count_hour = 0
count_min = 0
for i in range(0, duration+1, 86400):
    if i // 86400 > 0:
        count_day += 1
if count_day > 0:
    print(count_day, 'дн', end=' ')


duration %= 86400
for i in range(0, duration+1, 3600):
    if i // 3600 > 0:
        count_hour += 1
if count_hour > 0:
    print(count_hour, 'час', end=' ')


duration %= 3600
for i in range(0, duration+1, 60):
    if i // 60 > 0:
        count_min += 1
if count_min > 0:
    print(count_min, 'мин', end=' ')


duration %= 60
if duration > 0:
    print(duration, 'сек')