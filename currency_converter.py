CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}


def to_usd(currency_code, amount):
    # Check if the currency code is in the CURRENCIES dictionary
    if currency_code not in CURRENCIES:
        raise Exception(f"{currency_code} is not supported")

    # Check if the amount is valid
    if amount < 0:
        raise Exception(f"Invalid amount")

    # Get the conversion rate for the given currency code
    conversion_rate = CURRENCIES[currency_code]

    # Convert the amount to USD
    usd_amount = amount * conversion_rate

    return usd_amount


def from_usd(currency_code, amount):
    if currency_code not in CURRENCIES:
        raise Exception(f"{currency_code} is not supported")
    if amount < 0:
        raise Exception(f"Invalid amount")
    conversion_rate = CURRENCIES[currency_code]
    currency_amount = amount / conversion_rate
    return round(currency_amount, 4)


def convert(from_currency, amount, to_currency):
    try:
        # Convert from the source currency to USD
        usd_amount = to_usd(from_currency, amount)

        # Convert from USD to the target currency
        target_amount = from_usd(to_currency, usd_amount)

        # Print the equivalent value in the target currency
        print(f"{amount} {from_currency} is {target_amount} {to_currency}")
    except Exception as e:
        print(e)


# Example usage:
convert('CAD', 100, 'EUR')  # Should print the equivalent EUR value of 100 CAD
convert('USD', -50, 'GBP')  # Should raise an exception for invalid amount
convert('EUR', 100, 'INR')  # Should raise an exception for unsupported currency