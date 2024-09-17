# Program Developer Name:  Vincent Landreth
#
# Date Program Developed:  8/27/2024
#
# Organization: CIS 202 - 301
#
# Lookup the proper formatting of the "print f" function and complete the output so it looks like:
# The number of cups of butter needed for 136 cookies is  2.83 cups 
#
# Document your givens below this line
# for 48 cookies: 1 cup butter, 1.5 cups sugar, 2.75 cups flour
#
# Document your inputs below this line
# quantity of cookies desired
#
# Document your outputs below this line
# cups of butter, cups of flour, cups of sugar
#
# Document your processes below this line
# multiplier = qtyIn / 48, sugar = multiplier * sugarGiven, butter = multiplier * butterGiven, flour = multiplier * flourGiven
#
# Start your program code after this line
flourGiven = 2.75
butterGiven = 1
sugarGiven = 1.5
qtyIn = int(input("How many cookies do you want? (only enter whole numbers in numeric form I.E. 96)"))
multiplier = qtyIn / 48
sugar = multiplier * sugarGiven
butter = multiplier * butterGiven
flour = multiplier * flourGiven
print(f'The number of cups of flour needed for {qtyIn} cookies is {flour:.2f}')
print(f'The number of cups of sugar needed for {qtyIn} cookies is {sugar:.2f}')
print(f'The number of cups of butter needed for {qtyIn} cookies is {butter:.2f}')
# This is the end of the program
