from forex import ForexHelper

class AppleStore:
    IPHONE_14_PRO_256 = "iPhone 14 Pro (256GB)"
    IPHONE_14_PRO_MAX_256 = "iPhone 14 Pro Max (256GB)"
    AIRPODS_PRO_2ND_GEN = "Airpods Pro 2nd Gen"

    def __init__(self, name: str, code: str = '', tax_rate: int = 0):
        self.name = name
        self.code = code
        self.tax_rate = tax_rate
        self.forex_helper = ForexHelper()
        
    def get_price(self, product: str, currency: str) -> float:
        currency = currency.upper()
        if product not in self.items:
            return None
        price_before_tax = self.items[product]
        price_after_tax = price_before_tax * ( 1 + self.tax_rate / 100 )
        if currency == self.currency:
            return round(price_after_tax, 2)
        else:
            return round(self.forex_helper.convert(price_after_tax, self.currency, currency), 2)
        
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name
            
        

class UKStore(AppleStore):
    tax_rate = 0
    name = "UK"
    currency = "GBP"
    items = {
        AppleStore.IPHONE_14_PRO_256: 1209,
        AppleStore.IPHONE_14_PRO_MAX_256: 1309,
        AppleStore.AIRPODS_PRO_2ND_GEN: 249,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)
        

class NewYorkStore(AppleStore):
    tax_rate = 8.875
    name = "New York"
    currency = "USD"
    items = {
        AppleStore.IPHONE_14_PRO_256: 1099,
        AppleStore.IPHONE_14_PRO_MAX_256: 1199,
        AppleStore.AIRPODS_PRO_2ND_GEN: 249,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)
        

class IndiaStore(AppleStore):
    tax_rate = 0
    name = "India"
    currency = "INR"
    items = {
        AppleStore.IPHONE_14_PRO_256: 139900,
        AppleStore.IPHONE_14_PRO_MAX_256: 149900,
        AppleStore.AIRPODS_PRO_2ND_GEN: 26900,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)
        

class DubaiStore(AppleStore):
    tax_rate = 0
    name = "Dubai"
    currency = "AED"
    items = {
        AppleStore.IPHONE_14_PRO_256: 4699,
        AppleStore.IPHONE_14_PRO_MAX_256: 5099,
        AppleStore.AIRPODS_PRO_2ND_GEN: 949,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)
        

class AustraliaStore(AppleStore):
    tax_rate = 0
    name = "Australia"
    currency = "AUD"
    items = {
        AppleStore.IPHONE_14_PRO_256: 1899,
        AppleStore.IPHONE_14_PRO_MAX_256: 2099,
        AppleStore.AIRPODS_PRO_2ND_GEN: 399,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)
        

class NewZealandStore(AppleStore):
    tax_rate = 0
    name = "New Zealand"
    currency = "NZD"
    items = {
        AppleStore.IPHONE_14_PRO_256: 2199,
        AppleStore.IPHONE_14_PRO_MAX_256: 2399,
        AppleStore.AIRPODS_PRO_2ND_GEN: 479,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)


class HongKongStore(AppleStore):
    tax_rate = 0
    name = "Hong Kong"
    currency = "HKD"
    items = {
        AppleStore.IPHONE_14_PRO_256: 9399,
        AppleStore.IPHONE_14_PRO_MAX_256: 10199,
        AppleStore.AIRPODS_PRO_2ND_GEN: 1849,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)


class ThailandStore(AppleStore):
    tax_rate = 0
    name = "Thailand"
    currency = "THB"
    items = {
        AppleStore.IPHONE_14_PRO_256: 45900,
        AppleStore.IPHONE_14_PRO_MAX_256: 48900,
        AppleStore.AIRPODS_PRO_2ND_GEN: 8990,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)

class SingaporeStore(AppleStore):
    tax_rate = 0
    name = "Singapore"
    currency = "SGD"
    items = {
        AppleStore.IPHONE_14_PRO_256: 1819,
        AppleStore.IPHONE_14_PRO_MAX_256: 1969,
        AppleStore.AIRPODS_PRO_2ND_GEN: 359,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)
        
class JapanStore(AppleStore):
    tax_rate = 0
    name = "Japan"
    currency = "JPY"
    items = {
        AppleStore.IPHONE_14_PRO_256: 164800,
        AppleStore.IPHONE_14_PRO_MAX_256: 179800,
        AppleStore.AIRPODS_PRO_2ND_GEN: 39800,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)


class MalaysiaStore(AppleStore):
    tax_rate = 0
    name = "Malaysia"
    currency = "MYR"
    items = {
        AppleStore.IPHONE_14_PRO_256: 5799,
        AppleStore.IPHONE_14_PRO_MAX_256: 6299,
        AppleStore.AIRPODS_PRO_2ND_GEN: 1099,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)


class NepalStore(AppleStore):
    tax_rate = 0
    name = "Nepal"
    currency = "NPR"
    items = {
        AppleStore.IPHONE_14_PRO_256: 215_000,
        AppleStore.IPHONE_14_PRO_MAX_256: 235_000,
        AppleStore.AIRPODS_PRO_2ND_GEN: 44_500,
    }

    def __init__(self):
        super().__init__(name=self.name, tax_rate=self.tax_rate)
