from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
from config import *
import pprint
import json

# constants
API_KEY = API_KEY
INTERVAL = INTERVAL  # seconds
URL = URL

# CoinMarketCap API requirements
parameters = {
    'slug': 'bitcoin',
    'convert': 'USD',
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY
}


session = Session()
session.headers.update(headers)

try:
    response = session.get(URL, params=parameters)
    data = json.loads(response.text)
    pprint.pprint(data)
except (ConnectionError, Timeout, TooManyRedirects) as exception:
    print(exception)
