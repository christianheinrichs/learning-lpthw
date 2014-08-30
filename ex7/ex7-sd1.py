#!/usr/bin/env python2

# Print out the sentence "Mary had a little lamb."
print "Mary had a little lamb."
# Print the sentence "Its fleece was white as snow"
print "Its fleece was white as %s." % 'snow'
# Print "And everywhere that Mary went."
print "And everywhere that Mary went."
# Print the "." character multiplied with 10, which results in the string:
# ..........
print "." * 10 # What'd that do?

# Assign the letter "C" to the variable end1
end1 = "C"
# Assign the letter "h" to the variable end2
end2 = "h"
# Assign the letter "e" to the variable end3
end3 = "e"
# Assign the letter "e" to the variable end4
end4 = "e"
# Assign the letter "s" to the variable end5
end5 = "s"
# Assign the letter "e" to the variable end6
end6 = "e"
# Assign the letter "B" to the variable end7
end7 = "B"
# Assign the letter "u" to the variable end8
end8 = "u"
# Assign the letter "r" to the variable end9
end9 = "r"
# Assign the letter "g" to the variable end10
end10 = "g"
# Assign the letter "e" to the variable end11
end11 = "e"
# Assign the letter "r" to the variable end12
end12 = "r"

# Watch that comma at the end. Try removing it to see what happens
# This line concatenates the strings from variables end1-end6, prints them
# and then combines them to the rest (end7-end12) with a space character
print end1 + end2 + end3 + end4 + end5 + end6,
# The following line prints out the letters from end7-end12
print end7 + end8 + end9 + end10 + end11 + end12
