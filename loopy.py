""" Python Repeating Instructions (Loops)

"""


def till_total(sales):
    total = 0
    for amount in sales:
        total = amount          # BUG: something is wrong here
    return total


def heritage_sale(prices_list):
    sale_prices = []
    for price in prices_list:
        # TODO: take 25% off (round DOWN) and format as "R <amount>"
        pass
    return sale_prices


def gate_code(code):
    # TODO: keep asking "Enter your code: " until it is correct
    pass


def longest_dry_spell(days):
    current = 0
    longest = 0
    for day in days:
        if day == "D":
            current += 1
            longest = max(longest, current)
        else:
            return longest      # BUG: think about what should happen on a rainy day
    return longest


def valley_finder(prices):
    valleys = []
    for p in range(len(prices)):
        if p < prices[p - 1] and p < prices[p + 1]:   # BUG(s)
            valleys.append(p)
    return valleys


def mac_validator(list_of_macs):
    """Sort MAC addresses into 'valid_macs' and 'invalid_macs'. See README."""
    valid_macs = []
    invalid_macs = []
    # TODO
    return {"valid_macs": valid_macs, "invalid_macs": invalid_macs}


def stock_runout(stock, daily_demand):
    """See README."""
    # TODO
    pass
