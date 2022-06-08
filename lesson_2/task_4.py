list_name = ['инженер конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлитаэ']
for i in range(len(list_name)):
    x = list_name[i].split(' ')

    print('Привет', x[-1].capitalize())