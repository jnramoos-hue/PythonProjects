# Lambda (anonymous) functions
# Syntax:
# lambda arguments: expression
from functools import reduce

# square = lambda x: x ** 2
#
# for i in range(1, 11):
#     print(square(i))

# x = int(input('Enter a number: '))
# is_even = lambda x: x % 2 == 0
#
# if is_even(x):
#     print('This number is even!')
# else:
#     print('This number is odd!')

# degrees = int(input('Enter the temperature in degrees Fahrenheit: '))
# f_to_c = lambda f: (f - 32) * 5 / 9
# print(f'The temperature in Celsius is: {f_to_c(degrees)}ºC ')

# map() function
# Syntax
# map(function, iterable)

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# double = list(map(lambda x: x * 2, nums))
# print(double)

# words = ['Python', 'is', 'a', 'language', 'of', 'programming']
# uppercase_words = list(map(str.upper, words))
# print(uppercase_words)

# filter() function
# Syntax
# filter(function, sequence)

# def even_numbers(n):
#     return n % 2 == 0
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# even_nums = list(filter(even_numbers, numbers))
# print(even_nums)

# reduce() function
# Syntax
# reduce(function, sequence, initial_value)

# from functools import reduce
#
# def multiply(x, y):
#     return x * y
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# total = reduce(multiply, numbers)
# print(total)

# Cumulative sum of the squares of values, using a lambda expression

numbers = [1, 2, 3, 4]
# ((1² + 2²)² + 3²)² + 4²

total = reduce(lambda x, y: x**2 + y**2, numbers)
print(total)

# ((1 + 4)² + 3²)² + 4²
# (5² + 3²)² + 4²
# (25 + 9)² + 4²
# 34² + 4²
# 1156 + 16
# 1172