# Function that displays a welcome message:
def message():
    print('Jnr Trainings in Tech!\n')

# Function for calculating the factorial of a number:
def factorial(number):
    if number < 0:
        return 'Enter a value greater than or equal to zero'
    else:
        if number == 0 or number == 1:
            return 1
        else:
            return number * factorial(number - 1)

# Function to return a Fibonacci series up to a value x:
def fibo(n):
    result = []
    a, b = 0, 1
    while b <= n:
        result.append(b)
        a, b = b, a + b
    return result  # Indentação corrigida aqui para o loop funcionar