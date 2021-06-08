from yfinance import Ticker
from requests import get

def read_tickers():
    with open('crypto_ticker.txt') as f:
        return f.read().split()

def get_latest_crypto_prices():
    d = {}
    for tick in read_tickers():
        d.update({
            tick:Ticker(tick).history(period="1m").Close.item()
            })
    return d

def get_latest_crypto_with_percentage():
    headers = {
        'Referer': 'https://in.finance.yahoo.com/__finStreamer-worker.js',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
        'DNT': '1',
    }
    d = {}
    for t in read_tickers():    
        params = (
            ('symbols', t),
            ('fields', 'regularMarketChange,regularMarketChangePercent,regularMarketPrice,regularMarketTime'),
        )
        response = get('https://query1.finance.yahoo.com/v7/finance/quote', headers=headers, params=params).json()
        d.update({
            t:response
        })
        # print(response['quoteResponse']['result'][0]['regularMarketChange'])
        # print(response['quoteResponse']['result'][0]['regularMarketChangePercent'])
        # print(response['quoteResponse']['result'][0]['regularMarketPrice'])
    return d

if __name__ == '__main__':
    print(get_latest_crypto_prices())