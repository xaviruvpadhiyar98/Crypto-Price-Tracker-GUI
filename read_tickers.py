def read_tickers():
    with open('crypto_ticker.txt') as f:
        return f.read().split()