'''a program to tell us the term for our search, 
the total number of results, and the different news sources that provided data
'''

import json 

#open file and load the data but formatted
with open('top_headlines.json') as headlines:
    data = json.load(headlines)
data = json.dumps(data, indent = 4)
data = data.split('""')
sourcesDict = {
    "ABC News": 0,
    "Associated Press": 0,
    "BBC News": 0,
    "CNN": 0,
    "NBC News": 0,
    "Newsweek": 0,
    "New Scientist": 0,
    "Politico": 0,
    "Reuters": 0,
    "Time": 0, 
    "The Wall Street Journal": 0,
    "The Washington Post": 0,
    "Vice News": 0
}

#loop de loop; count the times a source provided an article in the data and add to our count
for x in data: 
    for key in sourcesDict:
        if key in x:
            sourcesDict[key] +=1

#let's show you how many sources did stuff and give you those good good numbers
print("This is a list of all of the news sources present in our JSON data.")
print("The term we searched NewsAPI for is: 'vaccine'.")
print("The number associated with each source is the number of relevant articles they published.")
print(" ")
print(sourcesDict)
    
#close it up!
headlines.close()