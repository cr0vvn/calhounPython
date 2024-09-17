# Program Developer Name:  Vincent Landreth
#
# Date Program Developed:  9/2/2024
#
# Organization: CIS 202 - 301
#
# Write a program that will ask the user to enter the amount of a purchase.
# The program should then compute the state and county sales tax.
# Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent.
# The program should display the amount of the purchase, the state sales tax,
# the county sales tax, the total sales tax, and the total of the sale
# (which is the sum of the amount of purchase plus the total sales tax). 
#
# Document your givens below this line
# state sales tax is 5 percent, county sales tax is 2.5 percent
#
# Document your inputs below this line
# price of purchase
#
# Document your outputs below this line
# amount of the purchase, the state sales tax,
# the county sales tax, the total sales tax, and the total of the sale
#
# Document your processes below this line
# stateTax = subtotal * .05
# countyTax = subtotal * .025
# totalTax = stateTax + countyTax
# total = subtotal + totalTax
#
# Start your program code after this line
subtotal = float(input('Price of item? (input a decimal value i.e 5.99) '))
stateTax = subtotal * .05
countyTax = subtotal * .025
totalTax = stateTax + countyTax
total = subtotal + totalTax
print(f'{'Subtotal':<12} {'State Tax':<12} {'County Tax':<12} {'Total Tax':<12} {'Total':<12}')
print(f'${subtotal:<12.2f}${stateTax:<12.2f}${countyTax:<12.2f}${totalTax:<12.2f}${total:<12.2f}')
# This is the end of the program
