some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
some_list[1]= '05'; some_list[8] = '+05'

for i in range(len(some_list)):
    if some_list[i].isdigit() or some_list[i] == chr(43)+'05':
        some_list[i] = '"' + some_list[i] + '"'
print(*some_list)