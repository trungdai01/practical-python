# report.py
#
# Exercise 2.4


import sys
import csv


def read_list_tuples(filename):
    # file = open(filename, 'rt')
    total_cost = 0.0
    portfolio = []
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for line in rows:
            # fields = line.split(',')
            try:
                t = (line[0], int(line[1]), float(line[2]))
                portfolio.append(t)
                # t = (t[0], 0, t[1])
                shares = int(line[1])
                price = float(line[2])
                total_cost += t[1] * t[2]
            except ValueError:
                print("Could not parse", line)
    return portfolio


def read_list_dict(filename):
    portfolio = []
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            row_dict = {}
            row_dict[headers[0]] = row[0]
            row_dict[headers[1]] = int(row[1])
            row_dict[headers[2]] = float(row[2])
            portfolio.append(row_dict)
    return portfolio


def read_dict(filename):
    prices = {}
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


# filename = sys.argv[1]
# if filename == 'Data/prices.csv':
#     prices = read_dict(filename)
# else:
#     if filename == '':
#         filename = 'Data/portfolio.csv'
#     cost_dict = read_list_dict(filename)
#     cost_tuples = read_list_tuples(filename)
# print('Total cost: ', f'{cost:0.2f}')

# Exercise 2.7

costs = read_list_dict("Data/portfolio.csv")
prices = read_dict("Data/prices.csv")

total_costs = 0.0
total_value = 0.0
for cost in costs:
    total_costs += cost["shares"] * cost["price"]
for cost in costs:
    total_value += prices[cost["name"]] * cost["shares"]

print("Current value", total_value)
print("Gain", total_value - total_costs)

# Exercise 2.9


def make_report(portfolio, prices):
    list_portfolio = []
    for row in portfolio:
        change = float(prices[row["name"]]) - float(row["price"])
        t = (row["name"], int(row["shares"]), float(prices[row["name"]]), change)
        list_portfolio.append(t)
    return list_portfolio


report = make_report(costs, prices)
