# list = [2,6,9,4,0,12,3,7]
# word = 'Python'
# for letter in word:
#     print(letter)
#

# for number in range(1,11):
#     print(number)

# name = input('Type your name: ')
# for x in range(10):
#     print(f'{x+1} {name}')

# range(value_initial, value_final, increment)
# for x in range(20,1,-2):
#     print(x)

rock = ('Ruby', 'Emerald', 'Quartz', 'Sapphire', 'Diamond', 'Tourmaline')

for rock in rock:
    if rock == 'Quartz':
        continue
    print(rock)