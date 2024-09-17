# Program Developer Name:  Vincent Landreth
#
# Date Program Developed:  9/17/2024
#
# Organization: CIS 202 - 301
#
# Write a program that, given the speed and hours traveled,
# outputs the distance traveled each hour of the trip
#
# Document your givens below this line
# distance = speed * time
#
# Document your inputs below this line
# speed, hrsTraveled
#
# Document your outputs below this line
# distance traveled at hours 1-input
#
# Document your processes below this line
# for loop 0 - hoursTraveled:
#   distance = speed * time
#
# Start your program code after this line
speed = int(input('What is the speed of the vehicle in mph? '))
hrsTraveled = int(input('How many hours has it traveled? '))
print()
print(f'Hour\tDistance Traveled')
print('________________________')
print()
for hrs in range(1, hrsTraveled + 1):
    distance = hrs * speed
    print(f'{hrs}\t{distance}')
# This is the end of the program
