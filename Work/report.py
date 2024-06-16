# report.py
#
# Exercise 2.4
import sys
from fileparse import parse_csv
from stock import Stock


def read_portfolio(fileName: str) -> list:
    with open(fileName, encoding="utf8") as file:
        portdicts = parse_csv(
            lines=file,
            select=["name", "shares", "price"],
            types=[str, int, float],
        )
    portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
    return portfolio


def read_prices(fileName: str) -> dict:
    with open(fileName, encoding="utf8") as file:
        return dict(parse_csv(lines=file, has_headers=False, types=[str, float]))


def make_report_data(portfolio: list, prices: dict) -> list:
    rows = []
    for row in portfolio:
        cur_prices = prices[row.name]
        change = cur_prices - row.price
        summary = (row.name, row.shares, cur_prices, change)
        rows.append(summary)
    return rows


def print_report(report_data: list):
    headers = ("Name", "Shares", "Price", "Change")
    print(" ".join(f"{header:>10}" for header in headers))
    print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report_data:
        price_str = "$" + str(price)
        print(f"{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}")


def portfolio_report(portfolio_data: str, prices_data: str):
    portfolio = read_portfolio(portfolio_data)
    prices = read_prices(prices_data)
    summary = make_report_data(portfolio, prices)
    print_report(summary)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f"Usage: {argv[0]}" " portfile pricefile")
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)


if __name__ == "__main__":
    main(sys.argv)
