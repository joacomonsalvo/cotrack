from requests import Request, Session
from config import *
import json

# constants
API_KEY = API_KEY
INTERVAL = INTERVAL  # seconds
URL = URL


def main(slug="bitcoin"):
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

    response = session.get(URL, params=parameters)
    data = json.loads(response.text)

    slug = data["data"][0]["slug"]
    symbol = data["data"][0]["symbol"]
    price = data["data"][0]["quote"]["USD"]["price"]
    volume_24h = data["data"][0]["quote"]["USD"]["volume_24h"]
    percent_change_1h = data["data"][0]["quote"]["USD"]["percent_change_1h"]
    percent_change_24h = data["data"][0]["quote"]["USD"]["percent_change_24h"]
    percent_change_7d = data["data"][0]["quote"]["USD"]["percent_change_7d"]
    market_cap = data["data"][0]["quote"]["USD"]["market_cap"]
    last_updated = data["data"][0]["quote"]["USD"]["last_updated"]

    data = [slug, symbol, price, volume_24h, percent_change_1h, percent_change_24h, [percent_change_7d, market_cap, last_updated]]

    return data


if __name__ == "__main__":
    main()
