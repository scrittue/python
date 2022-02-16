#a program that prints the titles of articles in a json file

#import json
import json

#open file and load
with open('top_headlines.json') as th:
    parsed = json.load(th)

#a loop that prints the titles   
for x in parsed['articles']: 
    print(x['title'])
