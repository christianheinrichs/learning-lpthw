#!/usr/bin/env python2

# Import argv from the sys module
from sys import argv

# Pass the variables input_file and script to argv
script, input_file = argv

# Define function print_all with parameter f
def print_all(f):
    # Print complete content of the passed file
    print f.read()


# Define function rewind with parameter f
def rewind(f):
    # Put the file pointer back to position 0,
    # which is the beginning of the file
    f.seek(0)

# Define function print_a_line with 2 parameters: line_count and f
def print_a_line(line_count, f):
    # Print the line number, followed by the line itself
    print line_count, f.readline()

# Open the file object and store it in current_file
current_file = open(input_file)

# Tell the user, the whole file gets printed
print "First let's print the whole file:\n"

# Output the complete file
print_all(current_file)

# Tell the user, the file cursor gets rewinded
print "Now let's rewind, kind of like a tape."

# Use seek(0) to return the pointer to position 0
rewind(current_file)

# Tell the user, 3 lines are going to be printed
print "Let's print three lines:"

# Store the current line number and let it begin at 1
current_line = 1
# Execute print_a_line function
print_a_line(current_line, current_file)

# Increment current line number by 1
current_line = current_line + 1
# Execute print_a_line function
print_a_line(current_line, current_file)

# Increment current line number by 1
current_line = current_line + 1
# Execute print_a_line function
print_a_line(current_line, current_file)
