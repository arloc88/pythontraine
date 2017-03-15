#questo script accede ad un file di testo lorem.txt e ne stampa il contenuto
in_file = open("lorem.txt", "rt") # open file lorem.txt for reading text data
contents = in_file.read() # read the entire file into a string variable 
in_file.close() # close the file 
print(contents) # print contents

