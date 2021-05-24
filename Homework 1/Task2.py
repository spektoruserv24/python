number = int(input('Введите число '))
while True:
        if number >= 0 and number <= 10:
            sumo = number ** 2
            print(sumo)
            break
        else:
            number = int(input('Введите число '))