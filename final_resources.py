# Swap values between two variables.

var1 = 62
var2 = 31
#
# var1, var2 = var2, var1
#
# print(f'var1 = {var1} and var2 = {var2}')

# Ternary conditional operator
# smaller = var1 if var1 < var2 else var2
# print(f'Smaller value: {smaller}')
# print(f'Smaller value: {(var2, var1)[var1 < var2]}')

# Generators

# values = [1,3,5,7,9,11,13,15]
# squares = (item ** 2 for item in values)
# print(squares)
# for value in squares:
#     print(value)

# enumerate() function
# drinks = ['coffee', 'tea', 'water', 'Juice', 'Soft drink']
# for i, item in enumerate(drinks):
#     print(f'index: {i}, Item: {item}')

# temperatures = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
# total = 0
#
# for i, t, in enumerate(temperatures):
#     if t < 0:
#         print(f'The temperature at {i} is negative, with {t}ºC.')

# Context management with with

try:
    a = open('frutas.txt', 'r', encoding='utf-8')
    print(a.read())
except IOError:
    print('Could not open the file.')
else:
    a.close()

with open('frutas.txt', 'r', encoding='utf-8') as a:
    for line in a:
        print(line, end='')