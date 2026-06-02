# Simple conditional deviation

n1 = n2 = 0.0
average = 0.0

n1 = float(input('Type de first note : '))
n2 = float(input('Type de second note : '))

# Calculate the arithmetic mean.
average = (n1 + n2) / 2

print('Your average is {}'. format(average))

if (average >= 7):
    print('Approved')
    print('congratulations')
elif (average >= 5):
   print('Student in remedial classes.')
else:
    print('Disapproved')

