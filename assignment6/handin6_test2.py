# 5. The handin6_test2.py file should be similar to handin6_test1.py, but now instead call the wordfile_differences_binary_search on the input files, and saves the result in a variable called differences. 
import timeit
import handin6
start_time = timeit.default_timer()
# write code you want to measure execution time for here
differences = handin6.wordfile_differences_binary_search("british-english","american-english")
#print(differences)
time_spent = timeit.default_timer() - start_time
print(time_spent)


