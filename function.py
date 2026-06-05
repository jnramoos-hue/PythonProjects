# Functions
# Modularization, Code Reuse, Readability

# def <function_name>([arguments]):
#     <instructions>

# def message():
#     print("Jnramoos, technology development")
#     print("Complete Python Course.")
#
# message()


# Function with arguments
# def sum_func(a, b):
#     print(a + b)
#
# sum_func(12, 7)

# def mult(x, y):
#     return x * y
#
# a = 5
# b = 8
# c = mult(a, b)
#
# print(f'The product of {a} and {b} is {c}')

# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         print('It is not possible to divide by zero')
#
#
# if __name__ == '__main__':
#     a = int(input('Enter a number: '))
#     b = int(input('Enter another number: '))
#
#     r = div(a, b)
#     print(f'{a} divided by {b} equals {r}')

# def square(val):
#     squares = []
#     for x in val:
#         squares.append(x**2)
#     return squares
#
# if __name__ == '__main__':
#     values = [2, 5, 7, 9, 12]
#     result = square(values)
#     for g in result:
#         print(g)

# def count(num=11, character='+'):
#     for i in range(1, num):
#         print(character)
#
# if __name__ == '__main__':
#     count(6, '&')

x = 5
y = 6
z = 3

def sum_or_mult(a, b, c=0):
    if c == 0:
        return a * b
    else:
        return a + b

if __name__ == '__main__':
    res = sum_or_mult(x, y, z)
    print(res)