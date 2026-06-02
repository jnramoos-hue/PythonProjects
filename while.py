# num  = 1
#
# while (num <= 10):
#     print(num)
#     num += 1
# print('Loop closed!')

name = None

while True:
    print('Type your name, or x for exit: ')
    name = input()
    if name == 'x' or name == 'X':
        break

    print(f'Welcome, {name}')
print('Goodbye!')