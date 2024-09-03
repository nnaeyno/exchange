from tkinter import messagebox

import requests


def fetch_currencies():
    url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/currencies.json"
    response = requests.get(url)
    if response.status_code == 200:
        currencies = response.json()
        return currencies
    else:
        messagebox.showerror("Error", "Could not fetch currencies from the API.")
        return {}


def fetch_conversion_rate(from_currency, to_currency):
    # /currencies/{currencyCode}
    # Get the currency list with EUR as base currency:
    # https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}.json"
    response = requests.get(url)
    if response.status_code == 200:
        rate = response.json()[from_currency][to_currency]
        return rate
    else:
        messagebox.showerror("Error", f"Could not fetch conversion rate from {from_currency} to {to_currency}.")
        return None


def convert_and_display(from_currency, to_currency, amount):
    conversion_rate = fetch_conversion_rate(from_currency, to_currency)
    if conversion_rate is not None:
        converted_amount = float(amount) * conversion_rate
        return converted_amount
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number (integer or float).")
        return None


def get_currencies_codes():
    return sorted(fetch_currencies().keys())
