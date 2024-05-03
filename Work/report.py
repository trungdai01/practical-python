# report.py
#
# Exercise 2.4
import sys
import fileparse


def read_portfolio(fileName: str) -> list:
    return fileparse.parse_csv(
        filename=fileName,
        select=["name", "shares", "price"],
        types=[str, int, float],
    )


def read_prices(fileName: str) -> dict:
    return dict(fileparse.parse_csv(filename=fileName, has_headers=False, types=[str, float]))


def make_report_data(portfolio: list, prices: dict) -> list:
    rows = []
    for stock in portfolio:
        cur_prices = prices[stock["name"]]
        change = cur_prices - stock["price"]
        summary = (stock["name"], stock["shares"], cur_prices, change)
        rows.append(summary)
    return rows


def print_report(report_data: list):
    headers = ("Name", "Shares", "Price", "Change")
    # print("%10s %10s %10s %10s" % headers)
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
