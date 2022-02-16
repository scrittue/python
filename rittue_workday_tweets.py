'''
a program to separate the time from the date and time column
then it will return tweets posted between 9AM and 5PM

check out this YT video for other cool tricks you can do with pandas; this is from trick #16
https://www.kdnuggets.com/2019/08/25-tricks-pandas.html
'''

import pandas as pd

#read the data from the csv file
tweets = pd.read_csv('pb1uniquetweets.csv', encoding ='latin1')

#open the tweets dataframe; split the string in the object_posted_time column on the space character
tweets.object_posted_time.str.split(' ', expand=True)

#adds the time column to the table from the data we just split
tweets['time'] = tweets.object_posted_time.str.split(' ', expand=True)[1]

#this identifies tweets from the dataset posted between 9:00AM and 5:00PM
#using positional indexing in the dataframe
workday = tweets.loc[(tweets['time'] >= '09:00') & (tweets['time'] <= '17:00')]

print(workday)

'''
let it be known that this program supports labor unions and workers rights, not spying on workers!!
however, when analyzing data and how people interact (or don't) with information, 
knowing WHEN they do so can provide insight!

anyways, thanks for coming to my pandas-talk
'''