from newsapi import NewsApiClient

# Initialize with the api key they gave you
newsapi = NewsApiClient(api_key='a0c463ee1c6748309b39f7734b7fe4e5')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='vaccine',#change this to your topic
                                          sources='abc-news,associated-press,cnn,nbc-news,politico,reuters,usa-today,vice-news,time,the-washington-post,the-wall-street-journal,newsweek,new-scientist,bbc-news')#The more sources you have the more results you will get
print(top_headlines)#this will tell you how many results you have

import json#you need this library to work with json
with open('top_headlines.json', 'w') as outfile: #this writes the file, the next line prints the json
                                                 #file as a string so you want to include parameters to make the file easy to read
    json.dump(top_headlines, outfile, indent = 4)#indent is a parameter that makes the file easy to read when you open it
    
