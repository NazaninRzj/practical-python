import csv

def read_portfolio(filename):
    total = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        for name, number, price in portfolio:
            total += number * price
        return total
print(read_portfolio('Data/portfolio.csv'))