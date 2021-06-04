from yfinance import Ticker


def get_btc_inr():
    return Ticker("BTC-INR").history(period="1m").Close.item()


def get_eth_inr():
    return Ticker("ETH-INR").history(period="1m").Close.item()


def get_doge_inr():
    return Ticker("DOGE-INR").history(period="1m").Close.item()
