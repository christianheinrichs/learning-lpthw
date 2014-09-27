#!/usr/bin/env python2

# Define the function cheese_and_crackers with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print out amount of cheese
    print "You have %d cheeses!" % cheese_count
    # Print out amount of boxes
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Inform the user, that the amount of cheese and crackers
    # is sufficient for a party
    print "Man that's enough for a party!"
    # Print "Get a blanket."
    print "Get a blanket.\n"


# Tell the user, functions can accept numbers as arguments directly
print "We can just give the function numbers directly:"
# Call the function with integers 20 and 30
cheese_and_crackers(20, 30)


# Inform the user, that it's also possible to pass variables to a function
print "OR, we can use variables from our script:"
# Assign integer 10 to variable amount_of_cheese
amount_of_cheese = 10
# Assign integer 50 to variable amount_of_crackers
amount_of_crackers = 50

# Call the function with the just recently mentioned variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Inform the user about the possibility to pass math calcuations as arguments
print "We can even do math inside too:"
# Call the function with integers 30 and 11
cheese_and_crackers(10 + 20, 5 + 6)


# Inform about combining variables and math to pass as arguments
print "And we can combine the two, variables and math:"
# Call the function with a combination of variables and math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
