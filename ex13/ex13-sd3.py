#!/usr/bin/env python2

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print

question1 = int(raw_input("How many arguments does this script accept? "))

if question1 == 3:
    print "Correct!"
else:
    print "Wrong! The answer was 3."

question2 = int(raw_input("How many variables are defined for argv in this script? "))

if question2 == 4:
    print "Correct!"
else:
    print "Wrong! The answer was 4."
