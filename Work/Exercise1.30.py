def portfolio_cost(filename):
    Total_cost = 0
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            row = line.split(",")
            price = float(row[2])
            share = float(row[1])
            Total_cost += (price * share)
    return Total_cost

cost = portfolio_cost('Data/portfolio.csv')
print("Total_cost= ", cost)