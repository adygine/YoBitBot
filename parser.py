import requests
import constants

def get_info():
    response = requests.get(constants.url)