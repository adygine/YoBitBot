import requests
import repository
import utils

def get_ticker(coin='btc', coin2='usd'):
    response = requests.get(repository.get_ticker(coin, coin2))
    return response.text

def get_depth(coin='btc', coin2='usd',limit=150):
    response = requests.get(repository.get_depth(coin, coin2,limit))
    utils.generate_as_file('depth.txt',response.text)

    bids = response.json()[f'{coin}_usd']['bids']

    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount = item[1]

        total_bids_amount += price * coin_amount

    return f'Total bids: {total_bids_amount}$'

def process():
    print(get_ticker())
    print(get_depth())