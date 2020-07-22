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