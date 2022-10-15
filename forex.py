from datetime import datetime
import json
import logging
import requests
import os
from dotenv import load_dotenv
import sys

load_dotenv()


class ForexHelper:
    api_url = "https://api.apilayer.com/exchangerates_data/latest"

    def get_rates(self, base_currency: str, refresh: bool = False):
        data_directory = os.path.join(os.path.dirname(__file__), 'forex_data')
        filename = f"{base_currency}.json"
        data_file_path = os.path.join(data_directory, filename)
        if not os.path.exists(data_file_path):
            refresh = True

        if not refresh:
            with open(data_file_path) as data_file:
                data = json.load(data_file)
                timestamp = data["timestamp"]
                pulled_date = datetime.fromtimestamp(timestamp)
                pulled_date = (pulled_date.year, pulled_date.month, pulled_date.day)
                now =  datetime.now()
                today = (now.year, now.month, now.day)
                if pulled_date == today:
                    return data

        base_currency = base_currency.upper()
        response = requests.get(
            url="https://api.apilayer.com/exchangerates_data/latest",
            headers={
                "apikey": os.environ.get("FOREX_API_KEY"),
            },
            params={"base": base_currency},
        )
        if response.status_code != 200:
            logging.error(f"Could not fetch exchange rates for currency {base_currency}. Status Code: {response.status_code}")
        
        try:
            response = response.json()
            with open(data_file_path, "w") as data_file:
                json.dump(response, data_file)
            return response
        except Exception as e:
            logging.error(f"Could not write exchange rates for currency {base_currency}. Reason: {e}")
            return {}
        
    def convert(self, amount: float, _from: str, to: str) -> float:
        _from = _from.upper()
        to = to.upper()
        exchange_rate = self.get_rates(base_currency=_from).get("rates", {}).get(to)
        if not exchange_rate:
            print(f"ERROR: Invalid currency code.", file=sys.stderr)
            exit(-1)
        return amount * exchange_rate


if __name__ == "__main__":
    helper = ForexHelper()
    print(helper.convert(100, "usd", "npr"))
