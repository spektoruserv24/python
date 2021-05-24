age = int(input('Сколько вам лет?'))

if age < 18:
    print('Доступ запрещен')
elif age == 18:
    print('Вам ровно 18 лет')
    print('Что с вами делать')
else:
    print('Доступ разрешен')

print('Конец')