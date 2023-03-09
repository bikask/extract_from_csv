import csv

with open("./input.csv", 'r') as file:
  cr = csv.reader(file)
  for row in cr:
    print(row[0].split('_')[-2:-1]) 
