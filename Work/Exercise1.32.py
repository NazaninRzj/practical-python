import csv

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

cost = portfolio_cost('Data/portfolio.csv')
print("Total_cost= ", cost)
