# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

        return portfolio
print(read_portfolio('Data/portfolio.csv'))