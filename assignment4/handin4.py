# 1. Create a function called read_data, that takes a filename as argument. The function should open the file, and read its contents into a list of list of floats, where the outer list corresponds to the lines of the file, and the inner lists correspond to the columns (that is, convert the strings of each line to a list of two numeric values, and append them to an outer list). The function should return this list.
def read_data(file):
    """ Comments """
    opened_file = open(file,"r")
    list_of_list = []
    for line in opened_file:                # dividi ogni linea presente nel file in una lista di elementi (line.split)
        list_of_list.append(line.split())   # ,add each list (each line) to the list lista.prova
    return list_of_list
list_of_rows = read_data("./experimental_results.txt")
print(list_of_rows)

# 2. Write a function called calc_averages that takes a list of list of floats as input, and calculates the average value for each column by iterating over the rows. The function should return these two values. Test the function by calling it like this:
def calc_averages(list):
    """ Comments """
    sum1col = 0.
    sum2col = 0.
    for element in list:                   # the lines corresponds to the elements of the list
        sum1col += float(element[0])	   # add each value of the column 1 to sum1col and each of column 2 to sum2col
        sum2col += float(element[1])
    avg1col = sum1col / len(list)	   # calculate the avarege of each column
    avg2col = sum2col / len(list)
    return (avg1col,avg2col)		   # return the average valus of the two columns
col1_avg, col2_avg = calc_averages(list_of_rows)
print(col1_avg, col2_avg)

# 3: Write a function called transpose_data that turns the list of lists around so that it becomes a list of columns, rather than a list of rows.
def transpose_data(lista):
    """turns the list of lists around so that it becomes a list of columns, rather than a list of rows"""
    list_of_columns1 = []
    list_of_columns2 = []
    new_list = []
    for element in lista:
        list_of_columns1.append(element[0])         # per ogni elemento della lista (per ogni riga), estrai 1 num e aggiungi a list_of_columns1
        list_of_columns2.append(element[1])         # "     "     uguale per il secondo
    new_list.append(list_of_columns1)           # appendo la lista della colonna 1 e 2 alla new_list
    new_list.append(list_of_columns2)
    return (new_list)
list_of_columns = transpose_data(list_of_rows)
print (list_of_columns)

