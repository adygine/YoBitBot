import requests

def get_ticker(coin='btc', coin2='usd'):
    return requests.get(f'https://yobit.net/api/3/ticker/{coin}_{coin2}?ignore_invalid=1')

def get_depth(coin='btc', coin2='usd',limit=150):
    return requests.get(f'https://yobit.net/api/3/depth/{coin}_{coin2}?limit={limit}&ignore_invalid=1')

def get_trades(coin='btc', coin2='usd',limit=150):
    return requests.get(f'https://yobit.net/api/3/trades/{coin}_{coin2}?limit={limit}&ignore_invalid=1')