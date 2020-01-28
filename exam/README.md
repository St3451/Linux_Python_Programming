# Linux and Python Programming, Exam, 2019


## Background

Climate change is a hotly debated issue these years. In this exam
project, we will look at two of the central data sources in the
discussion: the change in global temperatures, and the rise in CO2
emissions.

We will be working with the following data sets.

<dl>
<dt><code>data/Land_and_Ocean_summary.txt</code></dt>
<dd>This file comes from the
Berkeley Earth website (http://berkeleyearth.org/data/). It contains global
temperature <i>anomalies</i>, telling us  how much colder or warmer it
is compared to a reference value, which is chosen to be the the
average over the time period between 1951 and 1980. The header of
the file contains further details.</dd>
<dt><code>data/anomalies_per_latitude.txt</code></dt>
<dd>This file contains temperature anomalies per year, for different latitudes on earth. This 
data also originates from the Berkely Earth Website (under the Gridded Data section), but
we have preprocessed it to reduce it in size, by only including one value per year, reducing to 5 degree latitude bands, and averaging
over all longitude values.</dd>
<dt><code>data/annual-co-emissions-by-region.csv</code>
<dd>This file contains CO2 emissions for different countries and
regions. It was downloaded from the Our World in Data website
(https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions).</dd>
<dt><code>data/population.csv</code></dt
<dd>A file containing populations for different countries and regions over time. Downloaded
from the Our World in Data website (https://ourworldindata.org/grapher/population).
</dl>

We recommand that you start by briefly looking at the files manually
to get an idea of their format. Below, we will explore these data
files in various Unix and Python exercises. Before we begin, however,
please read carefully through the following practical details of the
exam. 

<table><tr><td>
<table><tr><td>
<div style="margin-top:1em; margin-bottom:2em; width:100%; border:1px solid grey; padding: 0em 1em 1em 1em; box-sizing:border-box">
  <h3 style="padding-top:0;text-align:center"><strong>Formal requirements:</strong></h3>

  <dl>
    <dt>How do I hand-in?</dt>
    <dd>We will be using a combination of the Digital Exam system (https://eksamen.ku.dk) and Github to submit the exams. Submission of the exam consists of two steps: 1) Commit&push your code to github just as we have done in the weekly hand-ins. 2) Within the digital exam itself, submit a link to your exam github repository (i.e. <code>https://github.com/UCPH-LPP2019/exam-YOUR-USER-NAME</code>). <strong>It is important that you do both these steps!</strong> Note that you can actually complete the second step whenever you want during the exam week - even if you haven't finished your exam yet. We will simply extract the latest version from your github repository that was pushed before the deadline. If possible, submit the link in digital exam as a comment within the submission form. If that's not possible, please submit a plain text file (.txt) containing only the github link.</dd>
    <dt>Format:</dt>
    <dd>You should modify the following files in your github repository:
      <ol>
        <li>A Python file called <code>exam.py</code>, containing the function and class definitions.</li>
        <li>A Python file called <code>exam_test.py</code>, containing test code for the individual questions.</li>
        <li>A plain text file called <code >exam.sh</code>, containing the Unix commands used. The commands should be separated by empty lines, just like in the handins. The commands should be written so that they can be executed from the top-level directory (i.e. the directory in which <code>exam.sh</code> is located).</li>
      </ol>
    </dd>
    <dt>Content:</dt>
    <dd>For the Python part, remember to use
      meaningful variable names, include docstrings for each
      function, and add comments when code is not self-explanatory. Also, limit yourself to the curriculum covered in
      the course, that is, <span style="font-weight:bold">do not use
  list and dict comprehension, map, zip, reduce, filter and
  lambda</span>. Also, <strong>please use external modules only when they
  are explicitly mentioned in the exercise</strong>. Failure to do
      any of these will force us to deduct points even for code that works.</dd>
    <dt>Can we work in groups?</dt>
    <dd><strong>No!</strong> You should do the exam <strong>by yourself</strong>, and <strong>not discuss or share your solutions with anyone</strong>.</span> We will systematically use plagiarism programs to catch similarities between the exam solutions, and if we detect any suspicious overlap we will be forced to report it to the University Study Administration, who will then act accordingly. Students have been expelled on the basis of plagiarism on this course
      previously, so please take this seriously. You are of course welcome to seek information online, but please try to avoid copying large blocks of code verbatim from online examples. If you for some reason find it necessary to copy code directly (without rewriting it), then please add a comment that specifies the source of this code.</dd>
  </dl>
</div>
</td></tr></table>
</td></tr></table>

## Part 1: Data exploration

We'll start by inspecting the data and doing some simple plotting.
<ol>
<li> (UNIX) Write a one-line Unix command that counts the number of entries (i.e. years) in the <code>Land_and_Ocean_summary.txt</code> and prints it to screen.</li>

<li>Now we will process the data in Python. Inside the <code>exam.py</code> file, write a function called <code>read_year_to_anomaly_data</code> that takes a single argument: a filename. The function should open the file, iterate over the entries using a for loop and extract the first two columns of the file (containing the year and temperature anomaly). The function should return a dictionary, in which the years are keys (integers) and the temperature anomalies are values (floats).

Inside the <code>exam_test.py</code> file, import the <code>exam</code> module, and test the <code>read_year_to_anomaly_data</code> function by calling it on the <code>Land_and_Ocean_summary.txt</code> file. Store the resulting dictionary in a variable called <code>year_to_anomaly_dict</code>. Check that the dictionary allows you to look up the temperature anomaly for 2018.

<table><tr><td>

If you have problems completing this exercise, and therefore do not
have the <code>year_to_anomaly_dict</code> dictionary, please
follow the following instructions in order to be able to complete
the remainder of the exercises:

Insert the following lines of code in your <code>exam_test.py</code> file:

```python
import json
with open('fallback_solutions/Land_and_Ocean_summary.json') as infile:
    year_to_anomaly_dict = dict(json.load(infile))
```

Note that this dictionary is not exactly identical to the one you get from solving the exercise yourself (so you cannot use it for verification purposes).

</td></tr></table></li>

<li>We now wish to create a simple line plot with years on the x-axis and temperature anomalies on the y-axis. Copy the following code to your <code>exam.py</code> as a starting point. Replace the <code># YOUR CODE HERE</code> line with code that creates such a line figure (using the <code>plot</code> function), and saves the result to the filename specified by the function argument. Import the necessary external modules to make it work.</li>

```python
def create_line_plot(data, out_filename):
    '''Creates line plot of the key,value pairs in the dictionary'''

    fig, ax = plt.subplots()

    # YOUR CODE HERE

    return fig, ax
```

Inside the <code>exam_test.py</code> file, test the plotting functionality by calling the function on the <code>year_to_anomaly_dict</code> dictionary, and an output file called <code>anomalies_per_year.png.</code>

</ol>


## Part 2: Stripes

Last year, Ed Hawkins from the University of Reading created a simple,
but striking visualization of the above temperature vs time data:
https://showyourstripes.info/. His visualization has since been used
on neckties, necklaces, coffee mugs etc - and recently made the cover
of the economist
(https://www.economist.com/leaders/2019/09/19/the-climate-issue). In
this sub-exercise we will try to reproduce this visualization.

<ol>
<li>First, we will need to be able to map temperature values to colors. We will do this by creating a class called ColorMapper. The idea is that when creating a new color mapper object, we provide all the temperature values, so that it can initialize the colors based on the full temperature range. Afterwards, we can then call the color mapper with a specific temperature anomaly to get the corresponding color.

We do not have to do all the work by ourselves. Matplotlib has built-in color map objects, as shown here (https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html). Each of these has a name, and using the <code>get_cmap</code> function within the <code>matplotlib.pyplot</code> module, we can get a specific color mapper (e.g. <code>get_cmap("RdBu")</code>). We can use the resulting color mapper function to associate a color with any numeric value between zero and one. In the case of "RdBu", zero will produce Red, and one will produce Blue. 

Within the <code>exam.py</code> file, create a <code>ColorMapper</code> class with a constructor that takes two arguments: 1) <code>values</code>: a list of temperatures, and 2) <code>cmap_str</code>: a string with a name of matplotlib color map object, which should default to <code>"RdBu_r"</code>. The constructor should define two attributes in the object it is creating: 1) <code>max_abs_value</code>, which contains the maximum absolute value of the temperature anomalies, and 2) <code>cmap</code>, which is the underlying matplotlib colormap function (the object you get when calling get_cmap as described above).

Within your class, create a method called <code>get_color</code> that takes a single temperature value as argument, and returns the corresponding color.

Inside the <code>exam_test.py</code> file, verify that the code works by instantiating a `ColorMapper` object called `color_mapper`, using values from the <code>year_to_anomaly_dict</code> dictionary. Test that you can use the `color_mapper` object to calculate the color corresponding to a specified temperature anomaly, for instance <code>0.0</code>, using the "RdBu_r" color scheme.

<table><tr><td>

If you have problems completing this exercise, and therefore do not
have the <code>color_mapper</code> object, please
follow the following instructions in order to be able to complete
the remainder of the exercises:

Insert the following lines of code in your <code>exam_test.py</code> file:

```python
import pickle
import matplotlib.pyplot as plt
with open('fallback_solutions/class_instance_1.pickle', 'rb') as infile:
    color_mapper = eval(pickle.load(infile))
```

Note that this object is not exactly identical to the one you get from solving the exercise yourself (so you cannot use it for verification purposes).

</td></tr></table>
</li>

<li>We will now create the function to create the vertical stripes. Write a function called <code>construct_blocks</code> that takes three arguments: 1) data: a dictionary with (year, temperature anomaly) values, 2) bottom: a value specifying the lower coordinate value of each stripe, which should default to <code>0.0</code>, and 3) height: a value specifying the height of each stripe, which should default to <code>1.0</code>. The function should return a list of tuples, each with 5 elements: (year, bottom, width, height, temperature anomaly), where width is the width of the stripe, measured in years, which we can just set to 1.

Inside the <code>exam_test.py</code> file, call the <code>construct_blocks</code> function and save the result in a variable called <code>year_blocks</code>. To verify that it worked, you can call the following provided function, which should produce a visualization close to the original one by Ed Hawkins.

```python
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
```

</li>

<li>To summarize the data in another way, we will now calculate the average anomaly per decade. Inside the <code>exam.py</code> file, write a function called <code>calculate_anomalies_per_decade</code> that takes a dictionary of (year,anomaly) values as input. The function should return a new dictionary, where the keys are (start,end) tuples (e.g. <code>(1950,1960)</code>) and the values are the average anomalies for that period of time. A decade should include the start-year of the period, but exclude the end-year (i.e. <code>(1950,1960</code>) does not include the year 1960). If a decade is incomplete, the average should be over the available years, and the key should be adjusted accordingly (e.g. <code>(2010,2019)</code>, when data for 2019 is missing).

In the <code>exam_test.py</code> file, call the <code>calculate_anomalies_per_decade</code> function on the <code>year_to_anomaly_dict</code>, and save the result in a variable called <code>anomalies_per_decade</code>.

</ol>

## Part 3: Looking at Latitudes

We now wish to explore how the temperature has changed at different latitudes. For this purpose, we will use the <code>anomalies_per_latitude.txt</code> file.

<ol>
<li>In <code>exam.py</code>, write a function called <code>read_latitude_year_to_anomaly_data</code>. The function should take a single filename as argument, and return a dictionary of dictionaries, such that the outer dictionary has latitudes (floats) as keys, and the inner dictionaries have years as keys (integers) and anomalies as values (floats).

In the <code>exam_test.py</code> file, test the function by calling it on the <code>anomalies_per_latitude.txt</code> file, and saving the result in a variable called <code>latitude_year_to_anomaly_dict</code>. Check that the dictionary allows you to look up the temperature anomaly for 2018 at latitude 87.5.

<table><tr><td>

If you have problems completing this exercise, and therefore do not
have the <code>latitude_year_to_anomaly_dict</code> object, please
follow the following instructions in order to be able to complete
the remainder of the exercises:

Insert the following lines of code in your <code>exam_test.py</code> file:

```python
import json
with open('fallback_solutions/anomalies_per_latitude.json') as infile:
    latitude_year_to_anomaly_dict = {k1:dict(v1) for k1,v1 in json.load(infile)}
```

Note that this object is not exactly identical to the one you get from solving the exercise yourself (so you cannot use it for verification purposes).

</td></tr></table>

</li>

<li>Since we now have a nested dictionary, we cannot easily access all values at once. In the <code>exam.py</code> file, write a function called <code>get_values_from_nested_dict</code> that takes a nested dictionary as input, and returns a list of all values contained in all the sub-dictionaries (in our case, the temperature anomalies at any latitude value).

In <code>exam_test.py</code>, test your function by calling it on <code>latitude_year_to_anomaly_dict</code> and save the result in <code>latitude_year_anomalies</code>.

We can now create a new ColorMapper object that is compatible with the range of temperatures in this new set. In your <code>exam_test.py</code> file, create such an object and save it as the variable <code>color_mapper_latitudes</code>.
<table><tr><td>

If you have problems completing this exercise, and therefore do not
have the <code>color_mapper_latitudes</code> object, please
follow the following instructions in order to be able to complete
the remainder of the exercises:

Insert the following lines of code in your <code>exam_test.py</code> file:

```python
import matplotlib.pyplot as plt
with open('fallback_solutions/class_instance_2.pickle', 'rb') as infile:
    color_mapper_latitudes = eval(pickle.load(infile))
```

Note that this object is not exactly identical to the one you get from solving the exercise yourself (so you cannot use it for verification purposes).

</td></tr></table>
</li>

<li>Rather than the long vertical stripes that we plotted in Part 2, we will now use the vertical dimension of the visualization to reflect the latitude (so the top of the image corresponds to the north pole and the bottom of the visualization corresponds to the south pole). Write a function called <code>construct_latitude_blocks</code> that takes a single argument: a dictionary of dictionaries as we have just created in the previous exercise. Similar to the <code>construct_blocks</code> function, this function should return a list of tuples, each with 5 elements: (year, latitude, width, height, temperature anomaly), where width is the width of the stripe, measured in years, which we can just set to 1. The height of each block should be the height of the latitude band: 5 degrees. If you want, you can simplify your code by calling the <code>construct_blocks</code> function from within this function, but this is entirely optional.

In the <code>exam_test.py</code> file, call the <code>construct_latitude_blocks</code> function on the <code>latitude_year_to_anomaly_dict</code> dictionary, and save the result in <code>year_latitude_blocks</code>.

Again, you can now test that the function works by calling the provided <code>plot_blocks</code> function. Remember that you should use the new colormapper (<code>color_mapper_latitudes</code>).
</li>
</ol>

## Part 4: CO2 emissions

Finally, we will take a brief look at CO2 emissions for different countries. 

<ol>
<li> (UNIX) Let's start by extracting the 10 most CO2 producing countries from the <code>annual-co-emissions-by-region.csv</code> file. Write a one-line Unix command that sorts the file by year (most recent first), and by CO2 value (largest first, if the year is equal) - excluding all lines that do not have a 3 character country code, selects the top 10, and saves the output to a new file called <code>top10_CO2.csv</code></li>

<li>We'll now do the same in Python. In the <code>exam.py</code> file, write a function called <code>find_top10_emitting_countries</code> that takes a filename as argument. The final result should be a list of the 10 highest emitting countries (i.e. entries with a 3-letter country code) in the most recent year, sorted by their CO2 emission. The function should return a list of (full country name, CO2 emission) tuples. 

In the <code>exam_test.py</code> file, call the <code>find_top10_emitting_countries</code> function on the <code>annual-co-emissions-by-region.csv</code> file and store the result in a variable called <code>top10_emitting_countries</code>.

You can call the following plot function to create a bar plot of the results (ignore the <code>population_dict</code> parameter for now). Import the necessary external modules to make it work.

```python
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
```

</li>

<li>In addition to comparing CO2 emissions by country, we also want to compare it by how much each individual person in these countries contribute (CO2 emission per capita). To do this, we need to read in population size data. In your <code>exam.py</code> file, write a function called <code>read_population_data</code> that takes two arguments: a filename and a year-value. The function should return a dictionary with country/region names as keys, and population sizes (at the given year) as values.

In the <code>exam_test.py</code> file, call the <code>read_population_data</code> function on the <code>population.csv</code> file, and save the result in a variable called <code>population_dict</code>.

You can now call the <code>plot_emissions</code> function with the additional <code>population_dict</code> argument to make it take the populations into account. Import the necessary external modules to make it work.
</li>

</ol>


## Final remarks

One last comment regarding help: while we can of course not help you
with solving the exam exercise itself, we are available for questions
regarding technical issues and in cases where you are in doubt about
how a question should be interpreted. In particular, if you experience
problems with your virtual machine that prevent you from solving the
exam, please contact us immediately so we can find a solution as
quickly as possible. Unlike the hand-ins throughout the course, you
will (of course) <strong>not</strong> be able to get detailed feedback on your solution
by submitting it to the automated correction server. However, we have
set up the system to allow you to test whether the basic structure of
your files is correct. It works exactly like the weekly handins: you
can either run <code>pytest</code> locally or use git commit and git push (and
receive an email). Please note that even if
tests pass, it says nothing about the correctness of your assignment,
so you cannot use it to validate your solution, but if a test fails,
it means that this particular exercise does not run, and will
therefore not be assessed for the exam. Using this service is entirely
optional, but we highly recommend using it to rule out any technical
issues.  If you experience code that works on your own machine but
fails on the server, feel free to contact us about this, as this will
fall under the category "technical issues" which we are allowed to
help with. <strong>It is extremely important to
note that the github submission by itself it not sufficient. YOU HAVE
TO SUBMIT A LINK TO DIGITAL EXAM AS WELL.</strong> Also note that pushing to github
once in a while is a good way to keep backups of your exam during
the exam week.


