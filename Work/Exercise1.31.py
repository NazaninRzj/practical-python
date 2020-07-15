def portfolio_cost(filename):
    Total_cost = 0
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            try:
                row = line.split(",")
                price = float(row[2])
                share = float(row[1])
                Total_cost += (price * share)
            except ValueError:
                print("Missed data")
    return Total_cost

cost = portfolio_cost('Data/missing.csv')
print("Total_cost= ", cost)
