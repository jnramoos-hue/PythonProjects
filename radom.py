import random

# value = random.randint(1 , 20)
#
# print(value)

# print('Generate five random numbers between 1 and 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Generated number: {n}')

# valor = random.random()
# print(f'Generated number: {round(valor*10,2)}')

# valor = random.uniform(1,100)
# print(f'Generated number: {round(valor,4)}')

L = [2, 4, 6, 8, 10, 13, 14, 16, 18, 20, 21, 27, 33]
# n = random.choice(L)
# print(f'Chosen number: {n}')

# n = random.sample(L, 3)
# print(f'Chosen numbers: {n}')

print(f'Display the original list: {L} ')

n = random.shuffle(L)
print(f'Shuffle the list and display it: {L}')