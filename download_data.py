"""
This script downloads temperature measurements from http://berkeleyearth.org
(country mean) for all available countries listed in "countries.txt" plus the
data for Hawaii.

It uses the library "requests" to perform HTTP GET requests to the server and
get the respective data file. We have to do some clever manipulations because
the data files are encoded using Latin1 instead of Unicode. And life is so much
nicer when everything is Unicode.

All data files are placed in the "data" folder.
"""
import os
import requests

# If the 'data' folder doesn't exist, create it.
if not os.path.exists('data'):
    os.mkdir('data')
    print('Create "data" folder.')
else:
    print('Using existing "data" folder.')
    print('WARNING: Will overwrite any files in there!')
# Empty 'print' will print an empty line.
print()

# Load the list of countries
# Use the 'open' function to open a file for reading. The file content is
# accessed using the 'country_file' variable.
with open('countries.txt') as country_file:
    # We need to read in the country names, filter out empty strings from the
    # country list, and strip trailing white space and line breaks.
    # We'll start with an empty list and fill it with the names from our open
    # file.
    countries = []
    # Using an open file object in a 'for' loop will iterate over the lines of
    # that file, one at a time, until the end of the file.
    for line in country_file:
        # Remove trailing spaces and newlines.
        stripped = line.strip()
        # Check if the line is not an empty string after removing trailing
        # spaces and newlines.
        if stripped:
            # Add to the country list
            countries.append(stripped)
    # As a bonus, the above code could be substituted by a single line using
    # Pythons coolest feature: list comprehensions.
    # countries = [line.strip() for line in country_file if line.strip()]

# We'll be sneaky (lazy?) and add Hawaii to our list of countries to download
# the data from there as well.
countries.append('Hawaii')

baseurl = 'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/'

# We will collect the names of any country that we fail to download.
failed = []

print("Downloading data files:")

# The 'enumerate' function will produce an index number along with the list
# elements in a 'for' loop. It's very handy.
for country_number, country in enumerate(countries):
    # Print the number of the current country and its name. We add 1 because
    # enumerate starts from 0.
    print('    {}. {}... '.format(country_number + 1, country), end='')
    # Convert to lower case (lower) and use '-' instead of white space in case
    # of composite names.
    country_no_spaces = country.lower().replace(' ', '-')
    # The country names are Unicode strings (with some special characters, like
    # in "Åland"). To get those characters into URLs, we must encode them using
    # a specific notation (e.g., '%20' instead of ' '). We can do that using
    # requests. Another detail is that the file names on the server are
    # actually encoded using latin1 instead of Unicode :(
    country_quoted = requests.utils.quote(country_no_spaces, encoding='latin1')
    file_name =  country_quoted + '-TAVG-Trend.txt'
    url = baseurl + file_name
    # Now that we have a URL, we can make a GET request to get back our data
    # file.
    request = requests.get(url)
    # The status code tells us if the request was successful (200).
    if request.status_code != 200:
        failed.append(country)
        print('FAILED')
    else:
        # Save the downloaded text to a file in the "data" folder.
        # We can use the 'os' module to operate on paths in a
        # platform-independent way.
        # We need to open the file with write permission ('w')
        with open(os.path.join('data', file_name), 'w') as output_file:
            # Once again, text encoding is an issue. The data file is encoded
            # using latin1 instead of unicode (which is what Python likes), so
            # special characters will break when we read in the data.
            # Luckily, it's easy to convert the data file to unicode using the
            # 'decode' method.
            output_file.write(request.content.decode('latin1'))
        print('Success')

# An empty list will evaluate to False in an 'if' statement, so we can easily
# check if any of our downloads failed.
if failed:
    print("\nFailed to download data from the following countries:")
    for country in failed:
        print(country)
else:
    print('\nDone')
