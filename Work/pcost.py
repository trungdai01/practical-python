# pcost.py
#
# Exercise 1.27

import sys
import report


def portfolio_cost(fileName):
    records = report.read_portfolio(fileName=fileName)
    return sum((s["shares"] * s["price"] for s in records))


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]}" " portfile")
    portfile = argv[1]
    cost = portfolio_cost(portfile)
    print("Total cost:", cost)


if __name__ == "__main__":
    main(sys.argv)
