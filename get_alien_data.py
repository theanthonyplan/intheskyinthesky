from bs4 import BeautifulSoup as bs4
import requests as r
import json
from pprint import pprint as p
import random
# the url of the data we are going to rip
url = "http://www.nuforc.org/webreports/ndxe202008.html"



def build_training_data(debug=False):
    """
    Load our data source and start preprocessing the data
    """
    # this is where our data will be gathered
    data = []

    # first we want to open up our database rip
    for line in open('data.json', 'r'):
        # now we are going to go through and load each line as json
        # and we will appaend it to our data list
        data.append(json.loads(line))

    # check its length
    print(len(data))

    # if debug was passed, loop through and see whats there
    if debug is True:
        for i in data:
            p(i)
            input()
    # okay lets send the data back to whoever
    # requested it
    return data

def write_training_data(data, max_size=2000):
    """
    This function will actually write the data the file that is
    imported by the modedl trainer.
    """
    all_data = data                     # list of all data
    random_data = []                    # list of the selected data

    # randomly select data based on max_size
    for i in range(max_size):
        # remove a random record and append it to our random_data list
        random_data.append(all_data.pop(random.randrange(len(all_data))))

    # lets get a handle to a new file, overwrite it if it already exists
    f = open("training_data_2000.txt", "w")
    # Lets go through each line of data, and dump it as a string in a file
    for record in random_data:                        # for each record
        f.write(json.dumps(record['text']))       # dump record text
        f.write('\n')                          # append a new line
    # dont forget to clean up
    f.close()

if __name__ == '__main__':

    data = build_training_data()
    write_training_data(data, 2000)
