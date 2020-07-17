import csv
def portfolio_cost(filename):
    Total_cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            # print(record)
            try:
                price = float(record['price'])
                share = int(record['shares'])
                Total_cost += (price * share)
            except ValueError:
                print(f'Row {i}: Bad row: {line}')
    return Total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)