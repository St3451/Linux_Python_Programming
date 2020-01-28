# 1. Create a module called handin5, and inside that module define a function called read_fasta. This function should take one argument: a string that is a filename (or full path) to a fasta file. This function should open and read the supplied fasta file, then create and return a dictionary, where the keys are the names of the proteins (without the > character) and the sequences are the values. Make sure to add a docstring to your function.
def read_fasta(stringfile):
    """take a fasta file as argument and extract a dictionary, with headers as keys and relative sequences as values"""
    file_opened = open(stringfile, "r")
    dictio = {}
    for line in file_opened:
        if line[0] == ">":                      # if the line is the header
            key = line.strip(">\n")             # create a key
            #key = key[1:]                      # alternative way to cut the ">"
            dictio[key] = ""                    # assign the key to an empty value in the dictionary

        else:                                   # if the line is not an header
            dictio[key] += line.strip("\n")     # add the line to the value of the key assigned in the if statement
    return dictio

# 3.
def find_prot(dictionary,protein):
    """ Take a dictionary and a protein header as an argument. If protein header is present in the dictionary keys, return it's value, else print error """
    if protein in dictionary.keys():
        return (dictionary[protein])
    else:
        print("Error: protein name " + str(protein) +  " not found")


# 6. In the handin5 module, create a function called find_prot2 that takes a dictionary and regular expression (as a string), and returns a list of all of the keys in the dictionary that the pattern matches. Make sure to include a docstring.
def find_prot2(dictionary,regex):
    """ Find keys in dictionary from a regex created pattern"""
    import re
    pattern = re.compile(regex)
    list_of_matched_keys = []
    for key in dictionary.keys():
        match = pattern.match(key)
        if match:
            list_of_matched_keys.append(key)
    return list_of_matched_keys
