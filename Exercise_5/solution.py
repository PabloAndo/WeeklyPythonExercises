# Exercise 5 - WPE

# one function called "cities_to_csv"
# takes two arguments:
#   1 : URL which it will be used for download a JSON data
#   2 : filename where the JSON data will be written in a CSV format
# Use Tab rather than commas as CSV separator
# Data to be included:
#   City name   State name  City population City size rank


#!/usr/bin/env python3

import requests

gist_url = "https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json"

filename = "cities.csv"


def cities_to_csv(url, filename):

    req = requests.get(url)    
    f = open(filename, "w+")
    for city in req.json():  # city is a dictionary
        f.write(city["city"] + "\t" + city["state"] + "\t" +
                city["rank"] + "\t" + city["population"] + "\n")
    f.close()


if __name__ == '__main__':
    cities_to_csv(gist_url, filename)
