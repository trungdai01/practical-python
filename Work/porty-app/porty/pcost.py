# pcost.py

# Exercise 1.27

import sys
from .report import read_portfolio


def portfolio_cost(fileName):
    records = read_portfolio(fileName=fileName)
    # return sum((s.cost for s in records))
    return records.total_cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]}" " portfile")
    portfile = argv[1]
    cost = portfolio_cost(portfile)
    print("Total cost:", cost)


if __name__ == "__main__":
    main(sys.argv)
