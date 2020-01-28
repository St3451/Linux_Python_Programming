# 3. In the file called handin6_test1.py, call the wordfile_differences_linear_search on the input files, using british-english as file1 and american-english as file2 (it is ok to test it on the test files first, but please switch to the full files before submitting), and saves the result in a variable called differences. 
import timeit
import handin6
start_time = timeit.default_timer()	# write code you want to measure execution time for here
differences = handin6.wordfile_differences_linear_search("british-english","american-english")

time_spent = timeit.default_timer() - start_time
print(time_spent)
