# name = 'Python Course'
# # letter = name[2]
# # print(letter)
# student = 'Junior'
#
# # print(len(name))
#
# print(name + ' with ' + student)

# phrase = 'Let\'s learn python today'
# words = phrase.split()
# print(words)
#
# phrase = 'Let\'s learn python today'
# words = phrase.split()
# print(words[1])
# for word in phrase:
#     print(word)

# email = input('Enter your email address: ')
# at_sign = email.find('@')
# print(at_sign)
# user = email[:at_sign]
# domain = email[at_sign+1:]


# products = 'sodium carbonate and zinc oxide'
# print('sodium' in products)
# print('magnesium' in products)

# item = 'hypochlorite'
# pos = item.find('chlor')
# print(pos)
# pos = item.find('flu')
# print(pos)

# celestial_object = 'spiral galaxy M31'
# print(celestial_object.upper())
# print(celestial_object.lower())
# print(celestial_object.title())
# print(celestial_object.capitalize())

# supplement = 'magnesium chloride'
# n_supplement = supplement.replace('magnesium', 'zinc')
# print(supplement)
# print(n_supplement)


# phrase = '     Omega 3 is good for health!     '
# print(phrase.lstrip())
# print(phrase.rstrip())
# print(phrase.strip())
#
# fruit = 'Avocado'
# print(fruit)
#
# print(fruit.rjust(20))
# print(fruit.center(20, "-"))
# print(fruit.ljust(20, "-"))

# p = 'Jnramoos Trainings'
# print(p.startswith('Jnr'))
# print(p.endswith('ramos'))

# Docstrings

text = '''
Docstrings are a type of documentation
that we can insert inside a module, function
or class in Python, among other places.
    It respects text indentation and is multiline
'''
print(text)