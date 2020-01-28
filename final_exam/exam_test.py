# Part 1

# 1.2
import exam
year_to_anomaly_dict = exam.read_year_to_anomaly_data("data/Land_and_Ocean_summary.txt")    
print(year_to_anomaly_dict[2018])

# 1.3
exam.create_line_plot(year_to_anomaly_dict, "anomalies_per_year.png")                   


# Part 2

# 2.1                                                           
from exam import ColorMapper                                    
color_mapper = ColorMapper(year_to_anomaly_dict.values())     
print(color_mapper.get_color(0.0))

# 2.2
year_blocks = exam.construct_blocks(year_to_anomaly_dict)       # call the function that return a list of tuples each containing: year, bottom, width, height, temperature anomaly

import matplotlib
import matplotlib.pyplot as plt
def plot_blocks(list_of_blocks, color_mapper,                         
                colorbar=True,
                figure_width=20, figure_height=5):
    '''
    Visualize list of blocks, where each block is specified in the format
    (x-coordinate, y-coordinate, width, height, value). The color_mapper is
    used to look up colors corresponding to the values provided in each block.

    :param list_of_blocks: List of (x-coordinate, y-coordinate, width, height, value) tuples
    :param color_mapper: Used to lookup values for each block
    :param colorbar: Whether to include a color bar
    :param figure_width: Width of figure
    :param figure_height: Height of figure
    :return: None
    '''

    fig, ax = plt.subplots(1, figsize=(figure_width, figure_height))
    x_values = []
    y_values = []
    for block in list_of_blocks:
        rect = matplotlib.patches.Rectangle(block[:2], block[2], block[3],
                                            linewidth=1, edgecolor='none',
                                            facecolor=color_mapper.get_color(block[-1]))
        ax.add_patch(rect)
        x_values += [block[0], block[0]+block[2]]
        y_values += [block[1], block[1]+block[3]]

    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values), max(y_values))

    if colorbar:
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(plt.gca())
        ax_cb = divider.new_horizontal(size="1%", pad=0.1)
        matplotlib.colorbar.ColorbarBase(ax_cb, cmap=color_mapper.cmap,
                                         orientation='vertical',
                                         norm=matplotlib.colors.Normalize(
                                             vmin=-color_mapper.max_abs_value,
                                             vmax=color_mapper.max_abs_value))
    plt.gcf().add_axes(ax_cb)
    plt.show()

plot_blocks(year_blocks, color_mapper)                          # call the provided function to verify that the construct_blocks function works

# 2.3
anomalies_per_decade = exam.calculate_anomalies_per_decade(year_to_anomaly_dict) 


# Part 3

# 3.1
latitude_year_to_anomaly_dict = exam.read_latitude_year_to_anomaly_data("data/anomalies_per_latitude.txt")             
print(latitude_year_to_anomaly_dict[87.5][2018])                                                            # check

# 3.2
latitude_year_anomalies = exam.get_values_from_nested_dict(latitude_year_to_anomaly_dict)                   # get all values (anomalies of temperature) from a dictionary of dictionaries                                              
color_mapper_latitudes = ColorMapper(latitude_year_anomalies)                                               # color mapper for the latitude

# 3.3
year_latitude_blocks = exam.construct_latitude_blocks(latitude_year_to_anomaly_dict)                        # create a list of tuples from the nested dictionary, in order to plot
plot_blocks(year_latitude_blocks, color_mapper_latitudes)                                                   # plot the anomaly of temperatures at different latitude and year 


# Part 4

# 4.2
top10_emitting_countries = exam.find_top10_emitting_countries("data/annual-co-emissions-by-region.csv")  

import numpy as np
def plot_emissions(list_of_tuples, population_dict=None, figure_width=15, figure_height=5):
    '''
    Create a bar plot of CO2 emissions. If population_dict is provided, resize
    bars so that width reflect population size and height denotes emission per
    capita.

    :param list_of_tuples: List of (country-name, value) tuples
    :param population_dict: Dictionary of (country-name, population) pairs
    :param figure_width: Width of figure
    :param figure_height: Height of figure
    :return:
    '''

    # Create new figure
    fig,ax = plt.subplots(1, figsize=(figure_width, figure_height))

    # Choose color map
    cmap = plt.get_cmap("Spectral")

    heights = []
    labels = []
    widths = []
    colors = []
    for i, entry in enumerate(list_of_tuples):
        heights.append(entry[1])
        # Scale down height of bar with population size
        if population_dict is not None:
            heights[-1] /= population_dict[entry[0]]
        labels.append(entry[0])
        colors.append(cmap(i/len(list_of_tuples)))
    if population_dict is None:
        x = range(len(list_of_tuples))
        widths = [0.9] * len(list_of_tuples)
    else:
        max_width = 0
        for entry in list_of_tuples[:-1]:
            max_width = max(max_width, population_dict[entry[0]])
        x = np.arange(len(list_of_tuples)) * max_width
        for entry in list_of_tuples:
             widths.append(population_dict[entry[0]])

    # Create bar plot and set tick values
    plt.bar(x, height=heights, width=widths, color=colors)
    plt.ylabel("Annual CO2 emissions (tonnes)")
    plt.xticks(x, labels, rotation=45, ha="right")
    plt.show()

plot_emissions(top10_emitting_countries)

# 4.3
population_dict = exam.read_population_data("data/population.csv", 2017)                            # I added year 2017 as argument because the top 10 emitting countries are relative to this year (most recent one from the file "annual-co-emission-by-region.csv")

def plot_emissions(list_of_tuples, population_dict=None, figure_width=15, figure_height=5):         # I just changed the plot_emissions function to display "Annual CO2 emission per capita" instead of "Annual CO2 emissions (tonnes)"
    '''
    Create a bar plot of CO2 emissions. If population_dict is provided, resize
    bars so that width reflect population size and height denotes emission per
    capita.

    :param list_of_tuples: List of (country-name, value) tuples
    :param population_dict: Dictionary of (country-name, population) pairs
    :param figure_width: Width of figure
    :param figure_height: Height of figure
    :return:
    '''

    # Create new figure
    fig,ax = plt.subplots(1, figsize=(figure_width, figure_height))

    # Choose color map
    cmap = plt.get_cmap("Spectral")

    heights = []
    labels = []
    widths = []
    colors = []
    for i, entry in enumerate(list_of_tuples):
        heights.append(entry[1])
        # Scale down height of bar with population size
        if population_dict is not None:
            heights[-1] /= population_dict[entry[0]]
        labels.append(entry[0])
        colors.append(cmap(i/len(list_of_tuples)))
    if population_dict is None:
        x = range(len(list_of_tuples))
        widths = [0.9] * len(list_of_tuples)
    else:
        max_width = 0
        for entry in list_of_tuples[:-1]:
            max_width = max(max_width, population_dict[entry[0]])
        x = np.arange(len(list_of_tuples)) * max_width
        for entry in list_of_tuples:
             widths.append(population_dict[entry[0]])

    # Create bar plot and set tick values
    plt.bar(x, height=heights, width=widths, color=colors)
    plt.ylabel("Annual CO2 emission per capita (tonnes)")
    plt.xticks(x, labels, rotation=45, ha="right")
    plt.show()

plot_emissions(top10_emitting_countries, population_dict)