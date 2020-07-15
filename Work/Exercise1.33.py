import csv
import sys

def portfolio_cost(filename):
    Total_cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)

        for row in rows:
            try:
                price = float(row[2])
                share = float(row[1])
                Total_cost += (price * share)
            except ValueError:
                print("Missed data")
    return Total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total_cost= ", cost)
