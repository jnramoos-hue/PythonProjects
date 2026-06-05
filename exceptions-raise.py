from math import sqrt

class NegativeNumberError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        num = int(input("Enter a possite number: "))
        if num < 0:
            raise ArithmeticError
    except ArithmeticError:
        print(f'A negative number was provided.')
    else:
        print(f'The square root of {num} is {sqrt(num)}')
    finally:
        print(f'End of calculations.')