"""
Exercise 3.11 (Miles Per Gallon)
Drivers are concerned with the mileage obtained by their automobiles. 
One driver has kept track of several tankfuls of gasoline by recording miles driven and gallons used for each tankful.
Develop a sentinel-controlled-repitition script that prompt the user to input the miles driven and gallons used for each tankful.
The script should calculate and display the miles per gallon obtained for each tankful. 
After processing all input information, the script should calculate and display the combined miles per gallon obtained for all tankfulls (that is, total miles driven divided by total gallons used).
"""

SENTINEL = -1
result = []
while True: 
    gallons = float(input("Enter the gallons used ( -1 to end ): "))
    if gallons == SENTINEL : break
    miles = float(input("Enter the miles: "))
    mpg = miles / gallons 
    print(f'The miles/gallon for this tank was {mpg}')
    result.append(mpg) #add the mpg result to the result list above
    
print("The overall average miles/gallon was",sum(result)/len(result))
