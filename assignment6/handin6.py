# 1. In the module file called handin6.py, create a function called wordfile_to_list, which takes a single argument called filename. This function should read the file, and return a list with words. You can assume that each line in the file only contains a single word. Please remember to the remove newlines at the end of each line.
def wordfile_to_list(filename):
    """Read the file, and return a list with words. Assume that each line in the file only contains a single word"""
    file_opened = open(filename)
    word_list = []
    file_list = file_opened.readlines()
    for word in file_list:
        word_list.append(word.rstrip())
    return word_list


# 2. Add a function to the handin6 module called wordfile_differences_linear_search, which takes two filenames as arguments, and calls wordfile_to_list to create a list for each of these files. The function should contain a loop that for each word in the first list looks through the second list to see if there is a match. It should return a list of words that are in the first file but not in the second file.
def wordfile_differences_linear_search(filename1,filename2):
    """Create a list for each of these files. Return a list of words that are in the first file but not in the second file"""
    wordlist_file1 = wordfile_to_list(filename1)
    wordlist_file2 = wordfile_to_list(filename2)
    different_wordlist = []
    for word in wordlist_file1:                            # create a list of word that are present in file 1 but not in file 2
        if word not in wordlist_file2:
            different_wordlist.append(word)
    return different_wordlist

# 4. It is much more efficient to find elements in a sorted list. One way of doing this is by using a method called binary search. 
def binary_search(sorted_list, element):
    """Search for element in list using binary search."""
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False

def wordfile_differences_binary_search(filename1,filename2):
    """use binary search and find differences"""
    wordlist_file1 = wordfile_to_list(filename1)
    wordlist_file2 = wordfile_to_list(filename2)
    different_wordlist = []
    for word1 in wordlist_file1:
        if not binary_search(wordlist_file2,word1):
            different_wordlist.append(word1)
    return different_wordlist


# 6. Create a function called wordfile_to_dict in the handin6 module. This function should be identical to wordfile_to_list, but save the results as keys in a dictionary rather than in a list.
def wordfile_to_dict(filename):
    """Take a filename and create add each line (word) to a dictionary key"""
    file_opened = open(filename,"r")
    dictionary = {}
    file_list = file_opened.readlines()
    for word in file_list:
        dictionary[word.rstrip()] = ""
    return dictionary


# 7. Add a function to the handin6 module called wordfile_differences_dict_search, which takes two filenames as arguments, and calls wordfile_to_list on the first file and wordfile_to_dict on the second file. 
def wordfile_differences_dict_search(filename_to_list,filename_to_dict):
    """Generate a list from one file and a dict from an other file, then create a list with the words present in the list but not in the dict"""
    wordfile_list = wordfile_to_list(filename_to_list)
    wordfile_dict = wordfile_to_dict(filename_to_dict)
    different_wordlist = []
    for word in wordfile_list:
        if word not in wordfile_dict:
            different_wordlist.append(word)
    return different_wordlist
