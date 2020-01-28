# 1. Open the alice.txt file, and read the file into a list variable called lines where each element in the list corresponds to a line in the file.
alice_file = open("./alice.txt")
lines = alice_file.readlines()

# 2. Calculate and print how many lines there are in the file.
number_lines = len(lines)
print (number_lines)

# 3. Print the 41st line.
print (lines[40])

# 4. Count the number of words in the 43rd line and print the result.
line_words = lines[42].split() # create a list variable where each element of the list corrispond to a word
line_words_number = len(line_words)
print (line_words_number)

# 5. Open a new file called junk.txt, saving it to a variable called junk_file. Use the writelines method to write the 9th to the 11th line (both included) from the alice.txt.txt file to this file. Remember to close the file when you are done.
junk_file = open("junk.txt","w+")
junk_file.writelines(lines[8:11]) 
junk_file.close()
