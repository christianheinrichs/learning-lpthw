#!/usr/bin/env python2

def burgers_and_fries(burger_count, fries_count):
    print "You have %d burgers!" % burger_count
    print "You have %d boxes of fries!" % fries_count

amount_of_burgers = 10
boxes_of_fries = 10

burgers_and_fries(20, 30)
burgers_and_fries(20 / 5, 15)
burgers_and_fries(amount_of_burgers, 3)
burgers_and_fries(amount_of_burgers + boxes_of_fries, boxes_of_fries)
burgers_and_fries(boxes_of_fries / 2, amount_of_burgers * 3)
burgers_and_fries(20 + amount_of_burgers, amount_of_burgers - 4)
burgers_and_fries(60 * 2 / 120, 44 - 33)
burgers_and_fries(400 - 400 + 400 - 386, amount_of_burgers)
burgers_and_fries(boxes_of_fries / 2 * 5 / 5, boxes_of_fries)
burgers_and_fries(amount_of_burgers + 6 - 2 * 3, 43 - 23 + 2)
