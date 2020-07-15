# pcost.py
#
# Exercise 1.27

Total_cost = 0
with open("Data/portfolio.csv") as f:
    header = next(f)
    for line in f:
        row = line.split(",")
        price = float(row[2])
        share = float(row[1])
        Total_cost += (price * share)
print("Total_cost= ", Total_cost)