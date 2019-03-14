import csv
import json

# Give path to your own json and csv files
csvfile = open('file.csv', 'r') 
jsonfile = open('file.json', 'w')

fieldnames = ("name","size","shape","type")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
