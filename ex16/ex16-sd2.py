#!/usr/bin/env python2

from sys import argv

script, filename = argv

some_file = open(filename)
print some_file.read()
some_file.close()
