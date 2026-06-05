# Exceptions is a mechanism for handling errors
# try or except

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Type a number: '))
            n2 = int(input('Type another number: '))
            break
        except ValueError:
            print('An error occurred while reading the value. Please try again.')
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'Impossible to divide by zero')
    except:
        print(f'An unknown error occurred.')
    else:
        print(f'Result: {r}')
    finally:
        print(f'\nEnd of program.')




