# fileparse.py
#
# Exercise 3.3
import csv
from pprint import pprint
def parse_csv(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records

portfolio = parse_csv('Data/portfolio.csv')
# pprint(portfolio)