# 8. The test code in handin6_test3.py should be similar to the two others, but now call the wordfile_differences_dict_search on the input files.
import timeit
import handin6
start_time = timeit.default_timer()
# write code you want to measure execution time for here
differences = handin6.wordfile_differences_dict_search("british-english","american-english")
#print(differences)
time_spent = timeit.default_timer() - start_time
print(time_spent)
