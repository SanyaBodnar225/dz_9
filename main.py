class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        return amount / self.exchange_rate

def main():
    exchange_rate = float(input("Введіть курс обміну валюти до долара США: "))

    converter = CurrencyConverter(exchange_rate)

    amount_in_local_currency = float(input("Введіть суму в гривнях: "))

    amount_in_usd = converter.convert_to_usd(amount_in_local_currency)
    print(f"{amount_in_local_currency}  гривень дорівнює {amount_in_usd} доларам США.")

if __name__ == "__main__":
    main()
