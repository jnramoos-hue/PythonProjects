# Text file handling



# print(f'read() method: \n')
# print(handler.read())

# print(f'readline() method: \n')
# print(handler.readline())
# print(handler.readline())

# print(f'readlines() method: \n')
# print(handler.readlines())

# text = input('Which term do you want to search for in the file? ')
# try:
#     handler = open('arquivo.txt','r', encoding='utf-8')
#     for line in handler:
#         line = line.rstrip()
#         if text in line:
#             print(f'The string was found!')
#             print(line)
#         else:
#             print(f'The string was not found!')
# except IOError:
#     print('Could not open the file.')
# else:
#     handler.close()

# Write to text files

# try:
#     handler = open('arquivo.txt','w', encoding='utf-8')
#     handler.write('Jose da Silva Ramos Junior\n')
#     handler.write('How to create a text file in Python? \n')
# except IOError:
#     print('Could not open the file.')
# else:
#     handler.close()

# text = '\nPython is used extensively in Data Science.'
# try:
#     handler = open('arquivo.txt','a', encoding='utf-8')
#     handler.write(text)
# except IOError:
#     print('Could not open the file.')
# else:
#     handler.close()

fruits = ['Strawberry\n', 'Grape\n', 'Banana\n', 'Mango\n', 'Orange\n','Soursop']
# Create and write a text file
try:
    handler = open('frutas.txt','w', encoding='utf-8')
    handler.writelines(fruits)
except IOError:
    print('Could not open the file.')
else:
    handler.close()

# Read the created file
try:
    handler = open('frutas.txt','r', encoding='utf-8')
    print(handler.read())
except IOError:
    print('Could not open the file.')
else:
    handler.close()