#!/usr/bin/env python2

my_name = 'Zed A. Shaw'
my_age = 35 # Not a lie
my_height = 74 # Inches
my_height_converted = my_height * 2.54 # Centimeters
my_weight = 180 # lbs
my_weight_converted = my_weight * 0.454 # Kilograms
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d centimeters tall." % my_height_converted
print "He's %d kilograms heavy." % my_weight_converted
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_converted, my_weight_converted, my_age + \
    my_height_converted + my_weight_converted)
