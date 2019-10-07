#!/usr/bin/env python2

# Store the sentence "There are 10 types of people." in the variable x
x = "There are %d types of people." % 10
# Assign the string "binary" to the variable "binary"
binary = "binary"
# Assign the string "don't" to the variable "do_not"
do_not = "don't"
# Store the sentence "Those who know binary and those who don't" in the
# variable y
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the content of variable x
print x
# Print the content variable y
print y

# Print "I said: 'There are 10 types of people.'."
print "I said: %r." % x
# Print "I also said: 'Those who know binary and those who don't.'."
print "I also said: '%s'." % y

# Store the boolean value False in the variable "hilarious"
hilarious = False
# Store the String "Isn't that joke so funny?!" in the variable
# "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! %r"

# Print out "Isn't that joke so funny?! False" by assigning the %r character
# to hilarious of which the value is False
print joke_evaluation % hilarious

# Store the sentence "This is the left side of..." in the variable w
w = "This is the left side of..."
# Store the sentence "a string witih a right side." in the variable e
e = "a string with a right side."

# Combine the strings from variables "w" and "e". After that, print them.
print w + e
