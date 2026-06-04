# List: represents a sequence of values
# syntax list_name = [values]

# grades = [5, 7, 8, 6, 9]
# print(grades)

# n1 = [4, 6, 7, 8, 0, 3]
# n2 = [1, 6, 3, 0, 12, 9]
# values = n1 + n2
# print(values)
# print(type(values))

# print(values[-2])

# values[0] = 9
# print(values[0])

# print(values[0:2])

# print(len(values))
# print(sorted(values, reverse=True))
# print(sum(values))
# print(min(values))
# print(max(values))

# values.append(13)
# print(values)
# values.pop()
# print(values)
# values.pop(3)
# print(values)
# values.insert(3, 21)
# print(values)
# print(12 in values)

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for planet in planets:
#     print(planet)

drinks = []
for i in range(5):
    print(f'Enter a favorite drink: ')
    drink = input()
    drinks.append(drink)

drinks.sort()

print(f'\nFavorite drinks: ')
for drink in drinks:
    print(drink)
print('Cheers!')