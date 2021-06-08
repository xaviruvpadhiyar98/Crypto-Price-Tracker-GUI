from yfinance import Ticker

def read_tickers():
    with open('crypto_ticker.txt') as f:
        return f.read().split()

def get_ticker_prices():
    d = {}
    for tick in read_tickers():
        d.update({tick:Ticker(tick).history(period="1m").Close.item()})
    return d

if __name__ == '__main__':
    print(get_ticker_prices())