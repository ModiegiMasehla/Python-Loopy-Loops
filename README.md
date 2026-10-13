#Python Repeating Instructions (Loopy Loops)

## Learning Outcomes assessed

- Conditional statements
- Functions
- Basic loops
- Advanced loops
- Simple algorithms (problem solving)
- Basic command line commands

## Scoring & Weighting

| Component                                     | Weight  |
| --------------------------------------------- | ------- |
| Coding Section (unit tests)                   | **60%** |
| Form-Based Section (MCQs + written responses) | **40%** |

```bash
Coding Score = (P / T) x 60%     # P = tests passed, T = total tests
Form Score   = (C / Q) x 40%     # C = correct answers, Q = total questions
Final Score  = Coding Score + Form Score
```

The minimum pass mark is **60%**.

## How to run your tests

```bash
python3 -m pytest tests/test_loopy.py -v
python3 -m pytest tests/test_loopy.py::TestFunctions::test_till_total_multiple_sales -v
```

## Project structure

```text
fun-002-loopy-0.2/
├── loopy.py              # <-- write your solutions here
├── tests/
│   └── test_loopy.py     # <-- tests you must make pass
└── README.md             # <-- these instructions
```

Each function in `loopy.py` is partly written or buggy. **Fix the bugs**, **complete the logic** and make **all tests pass**.

---

### Question 1 - `till_total(sales)`

Mama Nomsa runs a tuck shop at a school in Soweto. At closing time she has a list of every sale she made today and needs the day's takings.

- **Input:** a list of integers, e.g. `[12, 8, 25, 5]`
- **Output:** one integer, the sum of all sales, e.g. `50`

---

### Question 2 - `heritage_sale(prices_list)`

For Heritage Day, a Durban clothing store is taking **25% off** everything. Print-ready receipts need the new prices.

Calculate the discounted price of each item (75% of the original, **rounded down** to a whole rand) and return a list of strings.

- **Input:** a list of integers, e.g. `[100, 200, 99]`
- **Output:** a list of strings, e.g. `["R 75", "R 150", "R 74"]`

---

### Question 3 - `gate_code(code)`

At a Johannesburg security estate, the boom gate only opens for the right code. Residents who get it wrong are asked again, for as long as it takes.

The function must repeatedly ask with `"Enter your code: "`.

- Wrong code: print `Wrong code. Try again.` and ask again.
- Correct code: print `Gate Open!` and stop asking.

---

### Question 4 - `longest_dry_spell(days)`

The Cape Town water department tracks rainfall. In a list of daily records, `"D"` is a dry day and `"R"` is a rainy day. Find the longest run of consecutive dry days.

- **Input:** a list of strings, e.g. `["D", "R", "D", "D", "R", "D", "D", "D"]`
- **Output:** an integer, e.g. `3`

---

### Question 5 - `valley_finder(prices)`

A Karoo farmer tracks the daily price of wool per kilogram and wants to buy at the lowest points. A "valley" is a price that is **strictly lower** than the price before it **and** the price after it. The first and last values can never be valleys, and flat spots (equal neighbours) do not count.

- **Input:** a list of integers, e.g. `[9, 4, 8, 7, 2, 6, 7, 8]`
- **Output:** a list of the valley prices in order, e.g. `[4, 2]`

---

### Question 6 - `mac_validator(list_of_macs)`

A Telkom network team is cleaning up a list of device MAC addresses. A valid MAC address:

```text
- is exactly 17 characters long
- follows the XX:XX:XX:XX:XX:XX pattern (six pairs separated by colons)
- uses only hexadecimal characters in the pairs (0-9, a-f, A-F)
```

- **Input:** a list of strings
- **Output:** a dictionary with the keys `'valid_macs'` and `'invalid_macs'`, each holding a list of strings in their original order

```python
{'valid_macs': ['00:1a:2b:3c:4d:5e'], 'invalid_macs': ['00-1a-2b-3c-4d-5e']}
```

---

### Question 7 - `stock_runout(stock, daily_demand)`

A Bo-Kaap spice shop has `stock` units of masala. A list `daily_demand` gives the expected demand for each day (day 1 is the first item).

- If `stock` is 0 (or less): return `"Stock is empty."`
- If on some day the demand is **more than what is left**: return `"Stock will run out on day N."`
- Otherwise: return `"Stock will last the whole period. Remaining stock: X"` (using up exactly everything counts as lasting, with `X` = 0)

Examples:

```python
stock_runout(40, [15, 10, 20, 5])  # "Stock will run out on day 3."
stock_runout(50, [10, 15, 5])      # "Stock will last the whole period. Remaining stock: 20"
```

---

Good luck, and think carefully about your solutions!