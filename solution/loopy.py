"""Python Repeating Instructions (Loops)

COMPLETED SOLUTION
"""


def till_total(sales):
    """Q1 - Add up every sale made today and return the total."""
    total = 0
    for amount in sales:
        total += amount
    return total


def heritage_sale(prices_list):
    """Q2 - Take 25% off every price (rounded DOWN to a whole rand)
    and return the new prices as strings such as "R 75"."""
    sale_prices = []
    for price in prices_list:
        discounted = price * 75 // 100  # 75% of the price, rounded down
        sale_prices.append(f"R {discounted}")
    return sale_prices


def gate_code(code):
    """Q3 - Keep asking for the estate gate code until it is correct."""
    while True:
        attempt = input("Enter your code: ")
        if attempt == code:
            print("Gate Open!")
            break
        print("Wrong code. Try again.")


def longest_dry_spell(days):
    """Q4 - 'D' = dry day, 'R' = rainy day.
    Return the longest run of consecutive dry days."""
    current = 0
    longest = 0
    for day in days:
        if day == "D":
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


def valley_finder(prices):
    """Q5 - Return every price that is strictly lower than the price
    immediately before it AND the price immediately after it."""
    valleys = []
    for i in range(1, len(prices) - 1):
        if prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
            valleys.append(prices[i])
    return valleys


def mac_validator(list_of_macs):
    """Q6 - Sort MAC addresses into valid and invalid ones.

    A valid MAC address:
      - is exactly 17 characters long
      - has the pattern XX:XX:XX:XX:XX:XX (six pairs separated by colons)
      - only uses hexadecimal characters (0-9, a-f or A-F) in the pairs
    """
    hexadecimals = "0123456789abcdefABCDEF"
    valid_macs = []
    invalid_macs = []

    for mac in list_of_macs:
        is_valid = len(mac) == 17
        if is_valid:
            for position, char in enumerate(mac):
                if position % 3 == 2:          # positions 2, 5, 8, 11, 14
                    if char != ":":
                        is_valid = False
                        break
                elif char not in hexadecimals:
                    is_valid = False
                    break

        if is_valid:
            valid_macs.append(mac)
        else:
            invalid_macs.append(mac)

    return {"valid_macs": valid_macs, "invalid_macs": invalid_macs}


def stock_runout(stock, daily_demand):
    """Q7 - Work out whether the stock lasts the projection period.

    - If the starting stock is 0 (or less): "Stock is empty."
    - If demand on some day is MORE than what is left, return
      "Stock will run out on day N." (N starts at 1)
    - Otherwise return
      "Stock will last the whole period. Remaining stock: X"
    """
    if stock <= 0:
        return "Stock is empty."

    remaining = stock
    for day, demand in enumerate(daily_demand, start=1):
        remaining -= demand
        if remaining < 0:
            return f"Stock will run out on day {day}."

    return f"Stock will last the whole period. Remaining stock: {remaining}"
