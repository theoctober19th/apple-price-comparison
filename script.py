import argparse
from datetime import datetime
from stores import (
    AppleStore,
    NepalStore,
    MalaysiaStore,
    NewYorkStore,
    DubaiStore,
    AustraliaStore,
    UKStore,
    IndiaStore,
    NewZealandStore,
    HongKongStore,
    ThailandStore,
    SingaporeStore,
    JapanStore,
)

STORES = [
    NepalStore(),
    NewYorkStore(),
    DubaiStore(),
    AustraliaStore(),
    UKStore(),
    IndiaStore(),
    NewZealandStore(),
    HongKongStore(),
    ThailandStore(),
    SingaporeStore(),
    JapanStore(),
    MalaysiaStore(),
]

PRODUCTS = [
    AppleStore.IPHONE_14_PRO_256,
    AppleStore.IPHONE_14_PRO_MAX_256,
    AppleStore.AIRPODS_PRO_2ND_GEN
]

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--currency", help="The currency to show the prices in")
    return parser.parse_args()

def display_prices(currency: str):
    buffer = ""
    prices = {}
    for product in PRODUCTS:
        row = {}
        min_price = None
        min_price_store = None
        for store in STORES:
            price = store.get_price(product, currency=currency)
            if min_price is None or (price and price < min_price):
                min_price =  price
                min_price_store = store
            row[store] = price or "N/A"
        row["min_price_store"] = min_price_store
        prices[product] = row

    col_width = 25
    row_width = (col_width + 2) * ( len(PRODUCTS) + 1)
    buffer += "=" * row_width
    buffer += "\n"
    buffer += f"| {'Location':<{col_width}}"
    for product in PRODUCTS:
        buffer += f"| {product:<{col_width}}"
    buffer += "|\n"
    buffer += "=" * row_width
    buffer += "\n"
    
    for store in STORES:
        buffer += f"| {str(store):<{col_width}}"
        for product in PRODUCTS:
            price = prices[product][store]
            min_price_store = prices[product]["min_price_store"]
            if store == min_price_store:
                price = f"{price} ★"
            price = f"{currency} {price}"
            buffer += f"| {price:<{col_width}}"
        buffer += "|\n"
        buffer += "-" * row_width
        buffer += "|\n"
    today = datetime.now().strftime("%Y-%m-%d")
    buffer += f"\n★ indicates the lowest price for the product. All prices are inclusive of taxes. Exchange rates applied for date {today}.\n"
    print(buffer)

def main():
    args = _parse_args()
    currency = args.currency or "USD"
    currency = currency.upper()
    display_prices(currency=currency)

if __name__ == "__main__":
    main()
