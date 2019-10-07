#!/usr/bin/env python2

# Assign the integer 100 to the variable "cars"
cars = 100
# Assign the float number 4.0 to the variable "space_in_a_car"
space_in_a_car = 4.0
# Assign the integer 30 to the variable "drivers"
drivers = 30
# Assign the integer 90 to the variable "passengers"
passengers = 90
# Substract the variable "drivers" from the variable "cars", which is:
# 100 - 30 = 70
# Thus, the integer result of 70 gets assigned# to the variable
# "cars_not_driven"
cars_not_driven = cars - drivers
# Assign the integer of "drivers" to the variable "cars_driven"
cars_driven = drivers
# Multiply an integer (cars_driven) with a float number (space_in_a_car) and
# assign the result to the variable "carpool_capacity"
carpool_capacity = cars_driven * space_in_a_car
# Divide an integer (passengers) by another integer (cars_driven)
# Assign the result to the variable "average_passengers_per_car"
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
