import os

# Enters the test folder located on the macOS Desktop
os.chdir(os.path.expanduser('~/Desktop/teste'))

print(f'Current directory: {os.getcwd()}')

name_pattern = input('What file name pattern should be used? Without the extension: ')

for counter, file in enumerate(sorted(os.listdir()), start=1):
    if os.path.isfile(file):
        file_name, file_extension = os.path.splitext(file)

        file_name = name_pattern + ' ' + str(counter)

        new_name = f'{file_name}{file_extension}'

        os.rename(file, new_name)

print('\nFiles renamed successfully!')