# Dictionary

elements = {
    'z': 3,
    'name': 'lithium',
    'group': 'Alkali Metals',
    'density': 0.534
}

print(f'Elements: {elements['name']}')
print(f'Density: {elements["density"]}')
print(f'The dictionary have {len(elements)} elements.')

#Update
elements['group'] = 'Alkaline Earth Metals'
print(elements)

# Add new entry
elements['período'] = 1
print(elements)

# Delete entry
del elements['período']
print(elements)

elements.clear()
print(elements)