#!/usr/bin/env python
myfileobject = open("pelican.txt", 'r')
# myfileobject is the variable we are assigning the file to
#  we are opening it to read

readfile = myfileobject.read()
# readfile is the variable that we are saving the file to
# using the .read function to read and store what's in the file to the variable readfile
#print(readfile)
# it has read the file as one long string
print(type(readfile))
# this is how we prove the type of the data (string)

# created an empty list
lines = []
for line in open("pelican.txt"):  # for loop with a loop variable of line that's opening the file
    lines.append(line)  # using the append function to add the loop variable to the empty list we created
    
    #**** Ellen has added this paragraph

    #We need to add this line
    print(line, end='') # the named parameter 'end' changes the default so that it doesn't start a new line each time, so now only the \n in the list item is used
    #We can proove this is the case:
        # if we use the print statement here but remove ,end='' the poem prints with extra line spacing
        # if we add it back in the extra line spacing is gone
        # if we then remove the \n in the pelican file and run this again, the lines will print in a list all on one line because we have removed the \n default in the print function using ,end='' and removed the newline instruction at the end of each line in the poem.
        # to be correct we need the \n in the pelican file and the ,end='' in the print function

    #**** 

print(lines)  # printing the list and proving the data type
print(type(lines))
print(len(lines))

# if we had an extra blank line, we could have used wildcard unpacking to remove it.
# *poemlines, blank_line = lines
# print(poemlines)

myfileobject.close() # safely closing the file now we have finished with it
