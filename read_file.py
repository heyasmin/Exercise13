#!/usr/bin/env python
myfileobject = open("pelican.txt", 'r')
# myfileobject is the variable we are assigning the file to
#  we are opening it to read

readfile = myfileobject.read()
# readfile is the variable that we are saving the file to
# using the .read function to read and store what's in the file to the variable readfile
print(readfile)
# it has read the file as one long string
print(type(readfile))
# this is how we prove the type of the data (string)

# created an empty list
lines = []
for line in open("pelican.txt"):  # for loop with a loop variable of line that's opening the file
    lines.append(line)  # using the append function to add the loop variable to the empty list we created
print(lines)  # printing the list and proving the data type
print(type(lines))
print(len(lines))
