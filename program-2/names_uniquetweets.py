#a program that displays real names associated with usernames

#import csv
import csv


#a loop that prints real names with corresponding usernames
with open('pb1uniquetweets.csv', newline='') as tweets:
    data = csv.DictReader(tweets)
    print("real name--                --username")
    for row in data:
        print(row['real_name'], "--                  --", row['username '])
