# Handin3

## Unix:

Download the file: https://wouterboomsma.github.io/lpp2019/data/experimental_results.txt

1. Use <code>bzip2</code> to compress the file, but in a way that preserves the original.
2. Use <code>ls</code> to output how large the two files are. The output should contain two lines - the first displaying the size of the original file, and the second displaying the size of the compressed file. The two line should each contain only the size, i.e. just a single number. (Hint: first use <code>tr</code> to squeeze all spaces and then use cut with space as a delimiter).
3. The <code>tr</code> command has the functionality to recognise digits (see the man page). Use this to replace all the number in the original file with "0.000000" (i.e. replace each digit with a zero), and save this to a file called <code>experimental_results_zeros.txt</code>.
4. Check that the <code>experimental_results_zeros.txt</code> file has the same size as the <code>experimental_results.txt</code> file, using the same output format as in question 2.
5. Use <code>bzip2</code> to compress the <code>experimental_results_zeros.txt</code> file (again keeping the original), and print out the sizes of the original and compressed files, in the same output format as in question 2.
6. Try to explain why there is a difference - use <code>echo</code> and <code>tee</code> to write the explanation both to a file called <code>explanation.txt</code> and to <code>stdout</code>.

## Python

We will be working on the following file: https://wouterboomsma.github.io/lpp2019/data/alice.txt. Please download it and place it in your current directory (you don't have to do this in Python or using a Unix command).

1. Open the <code>alice.txt.txt</code> file, and read the file into a list variable called <code>lines</code> where each element in the list corresponds to a line in the file.
2. Calculate and print how many lines there are in the file.
3. Print the 41st line.
4. Count the number of words in the 43rd line and print the result.
5. Open a new file called <code>junk.txt</code>, saving it to a variable called <code>junk_file</code>. Use the writelines method to write the 9th to the 11th line (both included) from the <code>alice.txt.txt</code> file to this file. Remember to close the file when you are done.


