# report.py
#
# Exercise 2.4
import sys
from .fileparse import parse_csv
from .stock import Stock
from .tableformat import TableFormatter, create_formatter
from .portfolio import Portfolio


# def read_portfolio(fileName: str, **opts) -> list:
#     """
#     Read a stock portfolio file into a list of dictionaries with keys
#     name, shares, and price.
#     """
#     with open(fileName, encoding="utf8") as file:
#         portdicts = parse_csv(lines=file, select=["name", "shares", "price"], types=[str, int, float], **opts)
#     # portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
#     portfolio = [Stock(**d) for d in portdicts]  # **d -> {d'name': , d'shares': , d'price': }
#     return Portfolio(portfolio)


def read_portfolio(fileName: str) -> list:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(fileName, encoding="utf8") as line:
        port = Portfolio.from_csv(line)
    return port


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


def print_report(report_data: list, formatter: TableFormatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    # headers = ("Name", "Shares", "Price", "Change")
    formatter.headings(["Name", "Shares", "Price", "Change"])
    # print(" ".join(f"{header:>10}" for header in headers))
    # print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report_data:
        # print(f"{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}")
        rowdata = [name, str(shares), f"${price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_data: str, prices_data: str, fmt: str = "txt"):
    portfolio = read_portfolio(portfolio_data)
    prices = read_prices(prices_data)
    summary = make_report_data(portfolio, prices)
    formatter = create_formatter(fmt)
    print_report(summary, formatter)


def main(argv):
    if len(argv) != 4:
        raise SystemExit(f"Usage: {argv[0]}" " portfile pricefile format")
    portfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]
    portfolio_report(portfile, pricefile, fmt)


if __name__ == "__main__":
    main(sys.argv)
