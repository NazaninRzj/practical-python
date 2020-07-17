import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    total = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            stock = {'name': row[0],
           'shares' : int(row[1]),
           'price' : float(row[2])}
            portfolio.append(stock)
        for r in portfolio:
            total += r['shares'] * r['price']
        return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])
    return prices


def make_report(portofilio, prices):
    summary = []
    for stock in portofilio:
        current_price = prices[stock['name']]
        # print(stock['name'],current_price)
        change = round(current_price - stock['price'], 2)
        # print(change)
        s = (stock['name'], stock['shares'], current_price, change)
        summary.append(s)
    return summary

portofilio = (read_portfolio("Data/portfolio.csv"))
prices = (read_prices("Data/prices.csv"))
report = (make_report(portofilio, prices))

for r in report:
    print(r)
