import csv
from pprint import pprint

def parse_csv(filename, select=None ,types=None, has_headers=True, delimiter=','):

    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)

        if has_headers:
            headers = next(rows)
        else:
            headers = []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for num, row in enumerate(rows, 1):
            if not row:
                continue

            if select:
                row = [ row[index] for index in indices ]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(f"Row {num}: Couldn't convert {row}")
                    print(f"Row {num}: Reason {e}")
                    
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records