import csv
from pprint import pprint


def readFile(filename):
    total_cost = 0.0
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            d = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            total_cost += d["shares"] * d["price"]
            # keys = d.items()

    return total_cost


portfolio = readFile("Data/portfolio.csv")
print("Total cost: ", f"{portfolio:0.2f}")


def listContainer(filename):
    records = []
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            records.append((row[0], int(row[1]), float(row[2])))

    return records


records = listContainer("Data/portfolio.csv")
print("List as containter: ", records)


def dictContainer(filename):
    prices = {}
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
        return prices


prices = dictContainer("Data/prices.csv")
print("Dict as container: ")
pprint(prices)


def make_report(portfolio, prices):
    records_report = []
    for name, shares, price in portfolio:
        change = prices[name] - price
        em = (name, shares, price, change)
        records_report.append(em)

    return records_report


record_report = make_report(records, prices)

headers = ("Name", "Shares", "Prices", "Change")
print("%10s " * len(headers) % headers)
# print(f"{header:>10s}" for header in headers)
print(("-" * 10 + " ") * len(headers))
for row in record_report:
    print("%10s %10d %10.2f %10.2f" % row)


# Ex2.15


def missing_portfolio(filename):
    # portfolio_list = []
    total_costs = 0.0
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rownum, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total_costs += nshares * price
            except ValueError:
                print(f"Row {rownum}: Bad row: {row}")

    return total_costs


costs = missing_portfolio("Data/missing.csv")
print(costs)


def portfoliodate_cost(filename):
    total_costs = 0.0
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rownum, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                total_costs += nshares * price
            except ValueError:
                print(f"Row {rownum}: Bad row: {row}")

    return total_costs


print("Portfolio cost with date %0.2f" % portfoliodate_cost("Data/portfoliodate.csv"))
