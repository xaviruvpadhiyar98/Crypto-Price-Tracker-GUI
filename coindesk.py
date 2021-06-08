import requests

headers = {
    'authority': 'production.api.coindesk.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41',
    'origin': 'https://www.coindesk.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.coindesk.com/',
    'accept-language': 'en-US,en;q=0.9',
}

params = (
    ('start_date', '2021-06-07T10:58'),
    ('end_date', '2021-06-08T10:58'),
    ('ohlc', 'false'),
)

response = requests.get('https://production.api.coindesk.com/v2/price/values/BTC', headers=headers, params=params).json()

print(response['data']['entries'][0])
print(response['data']['entries'][-1])
