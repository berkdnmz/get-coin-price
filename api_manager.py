
import requests

class ApiManager():

    def __init__(self,gui):
        self.gui = gui
        self.BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

    def get_price(self, coin="btc", currency="usd"):
        coim_id = coin.casefold()
        currency_id = currency.casefold()

        params = {
            "ids": coim_id,
            "vs_currencies": currency_id
        }
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            price = data[coim_id][currency_id]
            self.gui.label_coin_price.config(text=f"{coin.capitalize()} Price: {price} $")
            self.gui.label_coin_price.place(rely=0.75, relx=0.5, anchor="center")
        except KeyError:
            self.gui.show_error(f"Error: '{coin}' not found!")
            return
        except requests.exceptions.RequestException as e:
            self.gui.show_error(f"API error: {e}")
            return


