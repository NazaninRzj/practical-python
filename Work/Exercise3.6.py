import csv
from pprint import pprint

def parse_csv(filename, select=None ,types=None, has_headers=True):

    with open(filename) as f:
        rows = csv.reader(f)

        if has_headers:
            headers = next(rows)
        else:
            headers = []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for row in rows:
            if not row:
                continue

            if select:
                row = [ row[index] for index in indices ]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records


# shares_held = parse_csv('Data/portfolio.csv', select=['name','shares'], types=[str, int])
# portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float], has_headers=True)
prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)

# pprint(shares_held)
# pprint(portfolio)
pprint(prices)