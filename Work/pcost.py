# pcost.py
#
# Exercise 1.27

import sys
import csv


def portfolio_cost(filename):
    # file = open(filename, 'rt')
    total_cost = 0.0
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for line in rows:
            # fields = line.split(',')
            try:
                t = (line[0], int(line[1]), float(line[2]))
                # t = (t[0], 0, t[1])
                # shares = int(line[1])
                # price = float(line[2])
                total_cost += t[1] * t[2]
            except ValueError:
                print("Could not parse", line)
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost: ", f"{cost:0.2f}")
