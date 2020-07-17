import csv
from pprint import pprint
def read_portfolio(filename):
    portfolio = []
    total = 0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            dic = {'name': row[0],
           'shares' : int(row[1]),
           'price' : float(row[2])}
            portfolio.append(dic)
        for r in portfolio:
            total += r['shares'] * r['price']
        return portfolio

pprint(read_portfolio("Data/portfolio.csv"))
