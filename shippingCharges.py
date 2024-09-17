# Program Developer Name:  Vincent Landreth
#
# Date Program Developed:  9/5/2024
#
# Organization: CIS 202 - 301
#
# The Fast Freight Shipping Company charges the following rates:
# 2 pounds or less - $1.50
# Over 2 pounds but not more than 6 pounds - $3.00
# Over 6 pounds but not more than 10 pounds - $4.00
# Over 10 pounds - $4.75
# Write a program that asks the user to enter the weight of a
# package then displays the shipping charges
#
# Document your givens below this line
# 2 pounds or less - $1.50
# Over 2 pounds but not more than 6 pounds - $3.00
# Over 6 pounds but not more than 10 pounds - $4.00
# Over 10 pounds - $4.75
#
# Document your inputs below this line
# Weight of package
#
# Document your outputs below this line
# Shipping cost
#
# Document your processes below this line
# if x>10, 4.75 | elif x>6, 4 | elif x>2, 3 | elif x>0, 1.5 | else 0
#
# Start your program code after this line
weight = float(input('Weight of item? (input a decimal value i.e 3.8) '))
if weight > 10:
    rate = 4.75
elif weight > 6:
    rate = 4
elif weight > 2:
    rate = 3
elif weight > 0:
    rate = 1.5
else:
    rate = 0
print(f'The shipping charge is ${weight * rate:.2f}')
# This is the end of the program
