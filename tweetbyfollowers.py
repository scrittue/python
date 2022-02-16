#a program that sorts tweets by follower count in descending order

#import the panda library
import pandas as pd

#open the file to read and store in a variable
tweets = pd.read_csv("pb1uniquetweets.csv")

#sort the data by follower count in descending order
follows = tweets.sort_values(by='followers_count', ascending=False)

#print the data
print(follows)
