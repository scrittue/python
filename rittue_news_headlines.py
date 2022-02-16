#a program to output the article headlines from our search, the term 'vaccine'

import json

#open file and load the data
with open('top_headlines.json') as headlines:
    data = json.load(headlines)

#extra, extra! read all about it! feeling loopy with these headlines    
for x in data['articles']: 
    print(x['title'])

#close it up!
headlines.close()