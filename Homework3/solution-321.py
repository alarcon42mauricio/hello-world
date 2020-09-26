"""
Exercise 3.21 (Calculate Change Using Fewest Number of Coins)
Write a script that inputs a purchase price of a dollar or less for an item. Assume the purchaser pays with a dollar bill.
Detemrine the amount of change the cashier should give back to the purchaser.
Display the change using the fewest number of pennies, nickels, dimes and quarters. For example, if the purhcaser is due 73 cents in change,
the script would output:
Your change is:
2 quarters
2 dimes
3 pennies
"""

price = int(input('Please enter the purchase price amount(Quarters, Dimes, Nickles or Pennies): ')

change = 100 - price
print('Change is: ')

#Quarters
quarters = change // 25 
if quarters != 0:
    print(f'quarters: {quarters}')

#Dimes
change % = 25
dimes = change // 10
if dimes != 0:
    print(f'dimes: {dimes}')

#Nickles
change % = 5
nickles = change // 5
if nickles != 0:
    print(f'nickles: {nickles} ')

#Pennies
pennies = change % 5
if pennies != 0:
    print(f'pennies: {pennies}')


