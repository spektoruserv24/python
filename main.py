number = 75

value = int(input('Ввдите чистло от 1 до 100'))

if value == number:
    print('Вы угадали!')
else:
    if value > number:
        print('Нужно меньше')
    else:
        print('Нужно больше')