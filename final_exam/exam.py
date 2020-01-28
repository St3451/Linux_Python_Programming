# Part 1

# 1.2
def read_year_to_anomaly_data(filename):
    """Take a file as argument and extract the first two columns (years and 
    temperature anomaly). It return a dictionary in which the years are keys 
    (integers) and the temperature anomalies are values (floats)."""
    file_opened = open(filename, "r")
    dictio = {}

    for line in file_opened:
        line = line.strip()
        if len(line) == 0 or line[0] == "%":           # skip the header and the empty lines
            continue        
        else:
            lineX = line.split()                       
            dictio[int(lineX[0])] = float(lineX[1])    # assign years and temperature anomalies of the file to keys and values of the dictionary
    
    file_opened.close()
    return dictio

# 1.3
def create_line_plot(data, out_filename):
    '''Take a dictionary and the name of the output file as arguments. Create a 
    simple line plot with years on the x-axis (dictionary keys) and temperature 
    anomalies on the y-axis (dictionary values).'''
    import matplotlib.pyplot as plt                         # I decided to import matplotlib.pyplot and the other modules in each function, when it was needed.
                                                            # I thought it could be handy in case I want to import only the function itself and not the entire module    
    fig, ax = plt.subplots()                                                     

    x = list(data.keys())                                   # I used list() to make it works on the server, on my local machine it works fine without it (pytest)          
    y = list(data.values())                       
    ax.plot(x, y)                           
    plt.savefig(out_filename)               

    return fig, ax


# Part 2

# 2.1
class ColorMapper:
    """Map temperature values to colors. It convert data values (floats) from the 
    interval [0, 1] to the RGBA color that the respective Colormap represents"""

    def __init__(self, values, cmap_str="RdBu_r"):
        """Constructor with a max absolute value as first attribute and the color 
        mapper as second attribute"""
        import matplotlib.pyplot as plt
        
        abs_values = []                         
        for element in values:                          
            abs_value = abs(element)       
            abs_values.append(abs_value)

        self.max_abs_value = max(abs_values)         
        self.cmap = plt.get_cmap(cmap_str)                        

    def get_color(self, value):
        """Take a temperature value and return the corresponding color"""
        color = self.cmap(value)
        return color

# 2.2
def construct_blocks(data, bottom=0.0, height=1.0):
    """Create the vertical stripes for the visualization of the temperature 
    anomaly vs time data. Return a list of tuples each containing 5 elements
    (year, bottom, width, height, temperature anomaly)"""
    list_of_tuples = []
    
    for element in data:
        list_of_tuples.append([element, bottom, 1, height, data[element]])
    
    return list_of_tuples

# 2.3
def calculate_anomalies_per_decade(dictionary):
    """Take a dictionary (year,anomaly) as input and calculate the temperature 
    average anomaly per decade. It return a new dictionary, where the keys are 
    (start,end) tuples and the values are the average anomalies for that period 
    of time."""
    dictionary_decades = {}                     
    decade_keys_list = []                            
    decade_value = 0                                            # create a variable that will be used to count the sum of the decade temperature anomalies
    
    for element in dictionary:
    
        if len(decade_keys_list) < 9:                                                # if decade_keys contain less than 9 elements
            decade_keys_list.append(element)                                         # add the year in the decade_keys_keys
            decade_value += dictionary[element]                                      # add the temperature anomaly value to the decade_value variable 
            
            if element == list(dictionary.keys())[-1]:                                                                                      # if element is the last key of the dictionary
                dictionary_decades[(decade_keys_list[0], decade_keys_list[len(decade_keys_list)-1]+1)] = decade_value/len(decade_keys_list) # assign the first and last element of the decade_keys_list (add 1 to the last year) as key of the dictionary_decade, assign it the average temperature anomalies for the n years

        else:                                                                                                                                   # if decade_keys contain 9 elements
            decade_keys_list.append(element)                                                                                                    # add the 10th year of the decade to decade_keys_list
            decade_value += dictionary[element]                                                                                                 # add the 10th temp anomaly value to decade_value
            dictionary_decades[(decade_keys_list[0], decade_keys_list[len(decade_keys_list)-1]+1)] = decade_value/len(decade_keys_list)         # assign the first and the last element of the decade_keys_list (add 1 to the last year) as key of the dictionary_decades, assign it the average temperature anomalies for the decade
            decade_keys_list = []                                                                                                               # reset the value of the decade_keys_list and the variable for counting the sum of the decade temperature anomalies
            decade_value = 0
    
    return dictionary_decades


# Part 3

# 3.1
def read_latitude_year_to_anomaly_data(filename):
    """Take a filename as argument, and return a dictionary of dictionaries. 
    The outer dictionary has latitudes (floats) as keys, and the inner dictionaries 
    have years as keys (integers) and anomalies as values (floats)."""
    file_opened = open(filename)                                        
    dictionary_lat = {}                                                             
    
    for line in file_opened:                                            # for each line in the file
        line = line.split()                                             # convert the line in a list of strings
        if float(line[1]) not in dictionary_lat.keys():                 # if not present, add the second element of the list (latitude) to the dictionary keys as float
            dictionary_lat[float(line[1])] = {}                         # and assign to this key an inner empty dictionary as value                      

        dictionary_lat[float(line[1])][int(line[0])] = float(line[2])   # for each latitude keys, create an element of the inner dictionary that has the year(int) as key and the temperature anomaly as value(float)  
    
    file_opened.close()
    return dictionary_lat

# 3.2
def get_values_from_nested_dict(nested_dictionary):
    """takes a nested dictionary as input, and returns a list of all values contained 
    in all the sub-dictionaries (the temperature anomalies at any latitude value)"""
    list_of_all_values = []                                             
    
    for key in nested_dictionary:                                                           # access to the nested data structure
        for subkey in nested_dictionary[key]:
            list_of_all_values.append(nested_dictionary[key][subkey])
    
    return list_of_all_values

# 3.3
def construct_latitude_blocks(nested_dictionary):
    """Take a dictionary of dictionary and return a list of tuples, each with 5
    elements (year, latitude, width, height, temperature anomaly)"""
    list_of_tuples = []
    
    for lat in nested_dictionary:
        for year in nested_dictionary[lat]:
            list_of_tuples.append((year, lat, 1, 5, nested_dictionary[lat][year]))          # for each year in each latitude, append to the list a tuple with 5 element (year, latitude, width, height, temperature anomaly)     
    
    return list_of_tuples           


# Part 4

# 4.2
def find_top10_emitting_countries(filename):
    """Take a file and return a list of 10 tuples each containing: full country 
    name, CO2 emission in the most recent year. The list is sorted for CO2 emission"""
    import re
    file_opened = open(filename)
    pattern = re.compile(r"(.+),([a-zA-Z]{3}),([\d]+),(.+)")

    list_of_lines = []
    list_of_years = []
    list_of_tuples = []
    ordered_tuples_list = []

    for line in file_opened:                            # for each line in my file, if the string in the line match to my pattern
        line = line.rstrip()                            # remove the empty space at the end of the line and append the string to my list_of_lines 
        match = pattern.search(line)                    # also add each year (that are not present already) to the list_of_years, sort the list (not necessary)
        if match:           
            list_of_lines.append(line)
            if match.group(3) not in list_of_years:
                list_of_years.append(match.group(3))    
    list_of_years.sort()  

    for element in list_of_lines:                                                       # for each string (that are the lines of my file that match the pattern)
        splitted_matching_line = element.split(",")                                     # split the string in a list of strings (name, 3 character country code, year, CO2 emission) 
        if splitted_matching_line[2] >= max(list_of_years):                             # if the line refer to the emission from the most recent year
            tuplito = (float(splitted_matching_line[3]), splitted_matching_line[0])     # add to the tuple (CO2 emission, name) where the CO2 emission is the first element for sorting purpose)
            list_of_tuples.append(tuplito)                                              
    list_of_tuples.sort()                                                               # sort the list by the first element of the tuple (which is CO2 emission)
    
    for element in list_of_tuples[len(list_of_tuples):len(list_of_tuples)-11:-1]:           # for the last ten element of the list_of_tuples, iterete in reverse order (take the last 10 elements and revert the order of the list and )
        tuplito = (element[1], element[0])                                                  # revert the order of the element of each tuple
        ordered_tuples_list.append(tuplito)                                                 # append the new ordered element to the ordered_tuples_list
    
    file_opened.close()
    return ordered_tuples_list

# 4.3
def read_population_data(filename, year):
    """Take a filename and a year-value and return a dictionary with 
    country/region names as keys, and population sizes (at given year) as values"""
    import re
    file_opened = open(filename)
    dictionary_years = {}                                                             
    pattern = re.compile(r"[\d]{4}")                  # if it is present, the pattern match the year in each line (string)     

    for line in file_opened:                                                                                                                           
        line = line.rstrip()
        line = line.split(",")                                             
        match = pattern.search(line[2])
        if match:                                                   # include only the line that has a 4 digits number as 3th element (year), after they are splitted in a list of string (skip the first line)
            if int(line[2]) not in dictionary_years.keys():         # repeat the iteration I used to generate a dictionary of dictionary in read_latitude_year_to_anomaly function               
                dictionary_years[int(line[2])] = {}                 # the main differences are the index used and the data types                                
        else:
            continue
        dictionary_years[int(line[2])][str(line[0])] = int(line[3])   

    
    file_opened.close()
    return dictionary_years[year]
