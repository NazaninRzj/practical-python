import csv
import pandas as pd

def read_portfolio(filename):
    portfolio = []
    total = 0
    with open(filename) as f:
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
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])
    return prices


def make_report(portofilio, prices):
    df = pd.DataFrame(columns=['Name', 'Shares', 'Price', 'Change'])
    for stock in portofilio:
        current_price = prices[stock['name']]
        # print(stock['name'],current_price)
        change = round(current_price - stock['price'], 2)
        # print(stock['price'])
        df = df.append({'Name' : stock['name'], 'Shares': stock['shares'], 'Price': current_price, 'Change': change}, ignore_index=True)
    print(df)

portofilio = (read_portfolio("Data/portfolio.csv"))
prices = (read_prices("Data/prices.csv"))
report = (make_report(portofilio, prices))


