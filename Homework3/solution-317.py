"""
Exercise 3.17 (Nested Loops)
Write a script that displays the following triangle patterns seperately, one below the other. Seperate each pattern from the next one by one blank line.
Use for loops to generate the patterns. Display all asterisks(*) with a single statement of the form
print('*',end='')
which causes the asterisks to display side by side
"""

#Loop patter (a)
print('(a)')
for row in range(1, 11):
    for collumn in range(1, row + 1 ):
        print('*', end='')
    print()
print('\n')

#Loop pattern (b)
print('(b)')
for row in range (10, 0, -1):
    for column in range (1, row + 1):
        print('*',end = '')
    print()
print('\n')

#Loop third pattern (c)
print('(c)')
for row in range(10, 0, -1):
    for space in range(10, row, -1):
        print(' ', end='')
    for column in range(1, row + 1):
        print('*', end='')
    print()
print('\n')

#Nested fourth loop pattern (d)
print('(d)')
for row in range(10, 0, -1):
    for space in range(1, row):
        print(' ', end='')
    for column in range(10, row - 1, -1):
        print('*', end='')
    print()
