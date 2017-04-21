# Lecturer notes for Day 3

## Recap

* Numpy arrays
* Indexing
* Loading data from text file
* Making plots with matplotlib

### Recap Exercise

Using the Hawaii temperature data that we downloaded, write code that:

* Loads the data using numpy.loadtxt
* Generate a plot of the monthly temperature anomaly per decimal year
* Add labels and a title to your plot
* Make a second plot with the temperature in Fahrenheit

Optional:

* Add the yearly anomaly to your plots using a different color line


## Repeating actions

* Need to repeat something for every item in a list
* Can do it by indexing if list is short but it gets tedious
* Use the for loop
* Read as "for item in sequence: do something to item"
* Example: Calculating the mean


### Exercise

Given a list of country names:

    countries = ['Afghanistan', 'Antarctica', 'Bolivia', 'Canada', 'Congo',
                 'Egypt', 'Finland', 'Ghana', 'Haiti', 'Japan', 'Kenya',
                 'Malaysia', 'Nepal', 'Norway', 'Pakistan', 'Qatar', 'Spain',
                 'Switzerland', 'Yemen', 'Zimbabwe']

Write code that prints the URL for downloading the temperature data for each
country from Berkeley Earth. The URL should have the format
"http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/country_name-TAVG-Trend.txt".
The country name has to be lower case.


## Conditional execution

* Only run if a condition is True
* Boolean types and operators in Python
* Example: calculate the min


### Exercise

Create a folder called "data". Using the same list of country names, write code
that for each country:

* Makes the URL for downloading from Berkeley Earth
* Uses requests.get to download the data
* Checks if the status code is equal to 200. If it isn't, print a message
  saying that the download failed.
* If the status code is 200, save the data to a file using the name
  "country_name-TAVG-Trend.txt" (like the URL). These files should be placed in
  the "data" folder.


## Creating functions

* Reuse code without copy/paste
* The def operator
* Input arguments
* return
* Scope: variables inside the function don't affect the outside (usually)
* Docstrings
* Example: A function that calculates the mean of a sequence
* Example: A function that replaces a '.txt' with '.png'
* Default arguments


### Exercise

Create a function to download the temperature for a given country and save it
to a file. The function should be defined as follows:

    def download_data(country, folder='data'):


The function should return the data file name. If the download wasn't
successful, the function should return None.


### Exercise

Create a function that plots the temperature data and saves the figure to a
file. The function should be defined as

    def plot_temperature(month, year, anomaly, file_name):

month, year, and anomaly are numpy arrays. file_name is a string that should be
the same as the data file name but with '.png' instead of '.txt'. The figure
should have axis labels. The title should be the country name (tip: get it
from the file name).


## Putting it all together

Using our list of countries and the functions we created, write code that, for
each country:

* Downloads the data
* Saves it to a file in the "data" folder
* Loads the data using numpy
* Creates a figure of that data
* Saves the figure to png file in a "figures" folder
