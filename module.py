import mod_func as mf
#import math
#from math import sqrt
#import math as m
#import mod_func as mf

# print(m.sqrt(81))
# print(sqrt(81))
# print(math.sqrt(81))

if __name__ == '__main__':
    mf.message()

    num = int(input('Enter an integer number: '))

    print(f'\nCalculating the factorial of a number: ')
    fat = mf.factorial(num)
    print(f'The factorial is {fat}.')

    print(f'\nCalculating Fibonacci sequence: ')
    fib = mf.fibo(num)
    print(f'The sequence is {fib}.')