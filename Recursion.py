# Recursion

# General formula for factorial:
# factorial(num) = 1, if num = 1 or num = 0 'Base Case'
# factorial(num) = num * factorial(num-1), for num > 1 'Recursive Case'
# 4! -> 4 * factorial(3) = 4 * 3 * factorial(2) = 4 * 3 * 2 * factorial(1)
# 4! = 4 * 3 * 2 * 1 = 24

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == '__main__':
    x = int(input('Enter a positive integer to calculate the factorial: '))
    try:
        res = factorial(x)
    except RecursionError:
        print('The number is too large or negative to calculate the factorial.')
    else:
        print(f'The factorial of {x} is {res}')