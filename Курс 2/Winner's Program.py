empty_list = []

friends = ['Max', 'Leo', 'Kate']

print(len(friends))

friends.append('Ron')

print(friends)
print(len(friends))

print(friends.pop())

print(friends)

friends.clear()
print(friends)

friends = ['Max', 'Leo', 'Kate']
print(friends)

friends.remove('Kate')
print(friends)

del friends[0]
print(friends)