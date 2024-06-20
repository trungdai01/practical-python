# ticker.py

import csv
from typing import Iterator, Generator, Dict
from follow import follow
from report import read_portfolio
from tableformat import create_formatter


def select_columns(rows, indices: list[int]) -> Generator[list, None, None]:
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows: Iterator, types: list) -> Generator[list, None, None]:
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows: Iterator, headers: list[str]) -> Generator[None, None, Dict[str, str]]:
    obj = (dict(zip(headers, row)) for row in rows)
    return obj


def filter_symbols(rows: Iterator, names: str) -> Generator[None, None, Dict[str, str]]:
    obj = (row for row in rows if row["name"] in names)
    return obj


def parse_stock_data(lines: Iterator) -> Generator[None, None, Generator]:
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    typeof_rows = type(rows)
    return rows, typeof_rows


def ticker(portfile: str, logfile: str, fmt: str) -> None:
    portfolio = read_portfolio(portfile)
    log = follow(logfile)
    stocks, typeof_stocks = parse_stock_data(log)
    stocks = filter_symbols(stocks, portfolio)
    formatter = create_formatter(fmt)
    print(typeof_stocks)
    columns = ["Name", "Price", "Change"]
    formatter.headings(columns)
    for stock in stocks:
        rowdata = [stock["name"], f"{stock['price']:0.2f}", f"{stock['change']:0.2f}"]
        formatter.row(rowdata)


if __name__ == "__main__":
    ticker("Data/portfolio.csv", "Data/stocklog.csv", "csv")
