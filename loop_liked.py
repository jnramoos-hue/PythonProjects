# for cont_ex in range(1,6):
#     print(f'\nRound: {cont_ex}')
#     for cont_ex in range(5,0,-1):
#         print(f'Value: {cont_ex}')
#
#
# print('End of loop.')

import random

for A in range(1,6):
    print(f'\nSet {A}')
    for B in range(5):
        num = random.randint(1,100)
        print(f'Value: {num}')