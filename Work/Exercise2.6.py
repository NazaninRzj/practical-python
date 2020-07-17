import csv
from pprint import pprint

def read_prices(filename):
     prices = {}
     with open(filename) as f:
         rows = csv.reader(f)
         for row in rows:
             if len(row) == 2:
                prices[row[0]] = float(row[1])
     return prices

pprint(read_prices("Data/prices.csv"))
# print(prices['IBM'])