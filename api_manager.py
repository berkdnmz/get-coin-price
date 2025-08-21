
import requests

class ApiManager():

    def __init__(self,gui):
        self.gui = gui
        self.BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

    def get_price(self, coin="btc", currency="usd"):
        params = {
            "ids": coin.lower(),
            "vs_currencies": currency.lower()
        }
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            self.gui.label_coin_price.config(text=f"{self.gui.entry_coin_name.get().lower().capitalize()} Price: {data[coin.lower()][currency.lower()]} $")
            self.gui.label_coin_price.place(rely=0.75, relx=0.5, anchor="center")
        except KeyError:
            return f"Error: '{coin}' not found!"
        except requests.exceptions.RequestException as e:
            return f"API error: {e}"


