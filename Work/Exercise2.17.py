import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    total = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
        return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
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


headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' %headers)
print(('-'*10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10} {change:10.2f}')
