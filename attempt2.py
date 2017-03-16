''' # with open ('lorem.txt', 'rt') as in_file: # Open file lorem.txt for reading of text data.
 #   for line in in_file: # Store each line in a string variable "line"
  #      print(line) # prints that line '''

''' lines = [] # Declare an empty list named "lines"
with open ('lorem.txt', 'rt') as in_file: # Open file lorem.txt for reading of text data.
    for line in in_file:# For each line of text, store it in a string variable named "line", and 
        lines.append(line) # add that line to our list of lines.
    print(lines[3]) # print the list object. '''
        
lines = [] # Declare an empty list named "lines"
with open ('lorem.txt', 'rt') as in_file: # Open file lorem.txt for reading of text data.
    for line in in_file: # For each line of text in in_file, where the data is named "line",
        lines.append(line) # add that line to our list of lines.
    for element in lines: # For each element in our list,
        print(element) # print it.

