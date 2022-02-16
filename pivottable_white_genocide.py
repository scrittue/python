#a program that creates a pivot table

#import the panda library
import pandas as pd

#open the file to read and store in a variable
wg = pd.read_csv("white_genocide.csv")

#create a pivot table and store it in a variable
table = wg.pivot_table(['signatureCount'],['issues'],)

#print the pivot table
print(table)
