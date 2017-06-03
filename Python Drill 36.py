# Python: 2.7.13
#
# Author: CJ Jones
#
# Purpose: The Tech Academy - Python Course Drill 36 of 68
#          Demoonstrating various Python concepts.
#
#
# Assigning an interger to a Variable
a = 100

# Assiging a string to a variable
country = 'Theymscira'

# Assigning a Float to a variable
b = 2.5

# Printing to the console welcome
print ('\nWelcome to {}' .format(country))

# Printing operation values of A and B to console
x = b + 1
print (x)
x = a - 2
print (x)
x = a * 2
print (x)
x = a / 2
print (x)
a += b
print (a)
c = a + b
print (c)
a %= b
print (b)

# Print variables A AND B
print (a and b)
# Print variable A OR B
print (a or b)
# Print the value of A NOT B
print (not a and b)

#If conditional statement and  Else If conditional statement
a = 100
if (a == 102):
    print ('Value of Expressin is 100')
    print ('Thank You and Come Again!')
elif (a == 103):
    print ('\nNope wrong answer!')
else:
    print ('\nNope wrong answer! Thank You for Playing!')

# While Loop statement to increase the count
count = 0
while (count <5):
    print ('This count is:',count)
    count = count +1
    print ('\nThank you come again!!!')

# For Loop statement to display letters on shell
for letter in 'Baby Software Developer':
    print ('Current Letter:',letter)

# For loop state to display Muscle Cars on shell
cars = ['Camaro','Mustang','Charger','Challenger','Corvette']
for index in range(len(cars)):
    print ('\nCurrent Cars:',cars[index])
    print ('\nWant a ride?!')

#Created a tuple to iterate through a favorite SciFi movie list
tup1 = ('Star Trek The Motion Picture','Start Trek The Wrath Of Kahn',
        'Star Trek The Search For Spock','Star Trek The Voyage Home',
        'Star Trek The Final Frontier','Star Trek The Underdiscovered Country');
tup2 = ('Star Trek Generations','Star Trek First Contact',
        'Star Trek Insurrection','Star Trek Nemisis');
tup3 = ('Star Trek','Star Trek Into Darkness','Star Trek Beyond');
print ('\nSome of the favorite Star Trek Movies!')

for index in range(len (tup1)):
    print ('\nThe Original Series')
    print  (tup1[index])
for index in range(len (tup2)):
    print ('\nThe Next Generation')
    print   (tup2 [index])
for index in range(len (tup3)):
    print ('\nNot Your Mothers Star Trek')
    print  (tup3 [index])

# Define a Function and print the string to the shell
def country(str):
    print (str)
    return;
country ("\nThis is my first visit!")
country ("And I can't wait to return!")

