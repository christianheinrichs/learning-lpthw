#!/usr/bin/env python2

formatter_tabby_cat = "%s %s %s"
formatter_persian_cat = "%s %s %s %s"
formatter_backslash_cat = "%s %s %s %s %s"
formatter_fat_cat = "%s %s %s %s"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print formatter_tabby_cat % ("\tI'm", "tabbed", "in.")
print formatter_persian_cat % ("I'm", "split\non", "a", "line.")
print formatter_backslash_cat % ("I'm", "\\", "a", "\\", "cat.")
print formatter_fat_cat % ("\nI'll do a list:", "\n\t* Cat food", "\n\t* Fishies", "\n\t* Catnip\n\t* Grass")
