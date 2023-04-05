# Group: Michael Phelps
    # Name: Ethan Lansangan
    # Name: Jake Pielage
    # Name: James Keen
    # Name: Branden McKinney
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This demonstrates our ability to use APIs
# Citations: 
# Anything else that's relevant: data from https://api.fda.gov

# main.py

import json
import requests

# Our API is from the FDA and accesses the National Drug Code Directory
# the NDC Directory contains information about all drug products

# First, we query the NDC Directory
# Our query is for the first 30 drugs with Ibuprofen as an active ingredient
response = requests.get('https://api.fda.gov/drug/ndc.json?api_key=M3dA9e76eGod4aA3MmvFs4DwgdblAf85ZFtkcodp&search=active_ingredients.name:"ibuprofen"&limit=30')
json_string = response.content

# Now we parse the result into a dictionary     
parsed_json = json.loads(json_string)

# Now we can use this dictionary to visualize the results in different ways

# As a random example, we're going to show the labeler of each of the 30 NDC entries that we queried
# We'll also show the dosage form for each of these labelers' products

# We'll do this by making a dictionary, where the keys are the Labeler and the values are the dosage forms
mnfgDict = {}
for i in range(0,len(parsed_json['results'])):
    mnfgDict[parsed_json['results'][i]['labeler_name']] = parsed_json['results'][i]['dosage_form']

# Finally we'll print each key/value pair from the dictionary individually
for i in mnfgDict:
    print(i,'...',mnfgDict[i])

# This shows an easy-to-read list of different Labelers 
# This includes many companies we're unfamiliar with and a few recognizable sellers like Sam's Club and CVS
# This list only has a few different form of Ibuprofen
# The forms are Coated Tablets, Suspension, Capsules, Chewables, and Liquid-filled Capsules
