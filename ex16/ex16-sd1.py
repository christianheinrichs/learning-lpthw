#!/usr/bin/env python2

# Import the feature argv from the sys module
from sys import argv

# Assign and pass the variables filename and script to argv
script, filename = argv

# Tell the user which file is going to be erased
print "We're going to erase %r." % filename
# Instruct how to avoid this step
print "If you don't want that, hit CTRL-C (^C)."
# Instruct how to continue
print "If you do want that, hit RETURN."

# Prompt the user for one of the two actions
raw_input("?")

# Inform the user that the program is opening the file
print "Opening the file..."
# Open the file in (w)rite mode and save the file object to variable target
target = open(filename, 'w')

# Inform the user about deletion/truncation of the file
print "Truncating the file.  Goodbye!"
# Truncate the file
target.truncate()

# Tell the user what's going to happen in the next step
print "Now I'm going to ask you for three lines."

# Prompt user for input and save it to variable line1
line1 = raw_input("line 1: ")
# Prompt user for input and save it to variable line2
line2 = raw_input("line 2: ")
# Prompt user for input and save it to variable line3
line3 = raw_input("line 3: ")

# Inform the user about the file write process
print "I'm going to write these to the file."

# Write first line to file
target.write(line1)
# Write line break to file
target.write("\n")
# Write second line to file
target.write(line2)
# Write line break to file
target.write("\n")
# Write third line to file
target.write(line3)
# Write line break to file
target.write("\n")

# Tell the user, the file gets closed
print "And finally, we close it."
# Finally, close the file
target.close()
