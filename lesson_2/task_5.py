price = [58.8, 45.53, 89.90, 84.0, 50.5, 20.78, 17, 24.7]
x = sorted(price)
for i in price:
    rub = int(i)
    cop = str(round((i-rub)*100)).zfill(2)
    print(f'{rub} руб. {cop} коп.')
print(id(price), id(x))