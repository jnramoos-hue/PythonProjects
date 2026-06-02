x = y = z = False
n1 = n2 = 0

print('Type a number: ')
n1 = int(input())

n2 = int(input('Type another number: '))

x = n1 == n2
print('Are they same? ', x, '\n')

z = n1 > n2
print(n1, 'is greater than ', n2, '?', z, '\n')

y = n1 != n2
print('Are they different?' + str(y))