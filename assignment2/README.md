# Handin 2
1. We would like to know the various backgrounds of the students attending the course. So start by writing a Unix command that simply prints this information (e.g. "Biology", "Physics", "Computer Science", ...), and redirects it to a file called background.txt.
2. Next, write a command that downloads the following file
http://people.binf.ku.dk/wb/data/th_en_US_v2.dat
This is a file with synonyms for words in the dictionary.
3. Within this file, search for all lines that contain the word "hacker"
4. Repeat 3), but now include only the lines that start with a "(" character.
5. Repeat 4), but now only include the first result.
6. Repeat 5), but now output the individual synonyms on separate lines (hint: replace the "|" characters in the input with "\n", which means new-line).
7. Repeat 6), but omit the first line in the output (the one that just says "(noun)").
8. Repeat 7), but now add line numbers to the output.
9. Repeat 8), but now save the output to a file called "hacker_output.txt", instead of outputting it to screen.
