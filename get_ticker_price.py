from requests import get


def get_ticker_price(t):
    url = "https://query1.finance.yahoo.com/v7/finance/quote"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41",
    }
    params = (
        ("symbols", t),
        (
            "fields",
            "regularMarketChange,regularMarketChangePercent,regularMarketPrice,regularMarketTime",
        ),
    )
    return get(url, headers=headers, params=params).json()


if __name__ == "__main__":
    print(get_ticker_price("BAJAJHCARE.BO"))
