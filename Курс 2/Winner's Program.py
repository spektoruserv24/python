print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место '.format(i))
    members.append(name)
    i-=1

print('В соеревновании участвовали: ', sorted(members))

members.reverse()

result = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)