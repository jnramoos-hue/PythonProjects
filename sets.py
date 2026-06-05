# Set

dwarf_planets = {'Pluto', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(dwarf_planets))
# print('Moon' not in dwarf_planets)

# for celestial_body in dwarf_planets:
#     print(celestial_body.upper())

# celestial_bodies = ['Moon', 'Venus', 'Sirius', 'Mars', 'Moon']
# print(celestial_bodies, end='')
# body_set = set(celestial_bodies)
# print(body_set)

stars1 = {'Moon', 'Venus', 'Sirius', 'Mars', 'Moon', 'Io'}
stars2 = {'Moon', 'Venus', 'Sirius', 'Mars', 'Moon', 'Halley\'s Comet'}
# print(stars1 | stars2)
# print(stars1.union(stars2))
#
# print(stars1 & stars2)
# print(stars1.intersection(stars2))
#
# print(stars1 ^ stars2)
# print(stars1.symmetric_difference(stars2))

stars1.add('Sun')
print(stars1)
stars1.add('Uranus')
print(stars1)

stars1.remove('Mars')
print(stars1)
stars1.discard('Halley\'s Comet')
print(stars1)
stars1.pop()
print(stars1)
stars1.clear()
print(stars1)