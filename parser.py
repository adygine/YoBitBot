import repository
import utils

def get_ticker(coin='btc', coin2='usd'):
    response = repository.get_ticker(coin, coin2)
    return response.text

def get_depth(coin='btc', coin2='usd',limit=150):
    response = repository.get_depth(coin, coin2,limit)
    bids = response.json()[f'{coin}_usd']['bids']

    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount = item[1]
        total_bids_amount += price * coin_amount

    return f'Total bids: {total_bids_amount}$'


def get_trades(coin='btc', coin2='usd',limit=150):
    response = repository.get_trades(coin, coin2,limit)

    utils.generate_as_file('trades.txt', response.text)

    total_ask = 0
    total_bid = 0

    for item in response.json()[f'{coin}_{coin2}']:
        if item['type'] == 'ask':
            total_ask += item['price'] * item['amount']
        else:
            total_bid += item['price'] * item['amount']

    info = f'[-] TOTAL {coin} SELL: {round(total_ask,2)}$\n[+] TOTAL {coin} BUY: {round(total_bid,2)}$'
    return info

def process():
    print(get_trades())