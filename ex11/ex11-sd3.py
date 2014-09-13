#!/usr/bin/env python2

print "What country are you from?",
country = raw_input()
print "What state are you from?",
state = raw_input()
print "What is your native language?",
language = raw_input()

print "So, you're from %r, %r and your native language is %r." % \
      (state, country, language)
