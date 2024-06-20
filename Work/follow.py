# follow.py

import os
import time
from typing import Generator
from report import read_portfolio


def follow(filename: str) -> Generator[str, None, None]:
    file = open(filename, encoding="utf8")
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if line == "":
            time.sleep(0.1)
            continue
        yield line


if __name__ == "__main__":
    portfolio = read_portfolio("Data/portfolio.csv")
    print(follow("Data/stocklog.csv"))
    for stocks in follow("Data/stocklog.csv"):
        fields = stocks.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")
