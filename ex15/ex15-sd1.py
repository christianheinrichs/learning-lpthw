#!/usr/bin/env python2

# Import argv from the sys module
from sys import argv

# Pass the variables filename and script to argv
script, filename = argv

# Open the file contained in the argument
txt = open(filename)

# Print out the file's name
print "Here's your file %r:" % filename
# Read the file and thus, print it to the screen
print txt.read()

# Prompt the user to type in the filename again
print "Type the filename again:"
# Store user input in the variable file_again
file_again = raw_input("> ")

# Open the entered file and store this action in txt_again
txt_again = open(file_again)

# Read the lastly entered file
print txt_again.read()
