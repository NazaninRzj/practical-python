import report_final
import sys

def portfolio_cost(filename):
    portfolio = report_final.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total_cost= ", cost)
