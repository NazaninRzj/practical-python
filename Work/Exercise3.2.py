import csv


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

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        # print(row)
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename, prices_filename):
    portofilio = (read_portfolio(portfolio_filename))
    prices = (read_prices(prices_filename))
    report = (make_report(portofilio, prices))
    print_report(report)

# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
# portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')
files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, 'Data/prices.csv')
        print()