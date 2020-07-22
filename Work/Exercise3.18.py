from pprint import pprint
from fileparse_2_final import parse_csv

def read_portfolio(filename):
    with open(filename) as line:
        return parse_csv(line, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    with open(filename) as line:
        return dict(parse_csv(line,types=[str,float], has_headers=False))


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

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)