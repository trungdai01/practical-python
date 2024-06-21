# timethis.py

import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__module__:s}.{func.__name__}: {(end-start): 0.2f}")

    return wrapper
