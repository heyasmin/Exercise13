#!/usr/bin/env python

# Question 1
myfileobject = open("pelican.txt", 'a') #a will append
myfileobject.write("A wonderful bird is the pelican\n")
myfileobject.write("His bill holds more than his belican\n")
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
random_variable = myfileobject.writelines(lines)

# The \n creates a newline for each line of the poem.