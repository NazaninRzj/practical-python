import csv
def portfolio_cost(filename):
    Total_cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for i, line in enumerate(rows, start=1):
            # print(i , line)
            try:
                price = float(line[2])
                share = int(line[1])
                Total_cost += (price * share)
            except ValueError:
                print(f'Row {i}: Bad row: {line}')
    return Total_cost

portfolio_cost("Data/missing.csv")
