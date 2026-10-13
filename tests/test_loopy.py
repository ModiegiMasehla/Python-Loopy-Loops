from io import StringIO
import loopy as lp


class TestFunctions():

    # ---------- Q1 till_total ----------
    def test_till_total_no_sales(self):
        assert lp.till_total([]) == 0

    def test_till_total_single_sale(self):
        assert lp.till_total([45]) == 45

    def test_till_total_multiple_single_sales(self):
        for amount in [9, 14, 60]:
            assert lp.till_total([amount]) == amount

    def test_till_total_multiple_sales(self):
        assert lp.till_total([12, 8, 25, 5]) == 50

    def test_till_total_multiple_sales_2(self):
        assert lp.till_total([0, 15, 35, 60, 90]) == 200

    def test_till_total_multiple_sales_stress(self):
        lists_of_sales = [
            [4, 6, 9, 11],
            [10, 20, 30, 40, 50, 60],
            list(range(1, 21)),
        ]
        expected_totals = [30, 210, 210]
        for sales, expected in zip(lists_of_sales, expected_totals):
            assert lp.till_total(sales) == expected

    # ---------- Q2 heritage_sale ----------
    def test_heritage_sale_no_items(self):
        assert lp.heritage_sale([]) == []

    def test_heritage_sale_single_item(self):
        assert lp.heritage_sale([100]) == ["R 75"]

    def test_heritage_sale_multiple_single_items(self):
        prices = [80, 200, 40]
        expected = ["R 60", "R 150", "R 30"]
        for price, exp in zip(prices, expected):
            assert lp.heritage_sale([price]) == [exp]

    def test_heritage_sale_multiple_items(self):
        assert lp.heritage_sale([100, 200, 400]) == ["R 75", "R 150", "R 300"]

    def test_heritage_sale_rounds_down(self):
        assert lp.heritage_sale([99, 55, 10]) == ["R 74", "R 41", "R 7"]

    def test_heritage_sale_multiple_items_stress(self):
        lists_of_prices = [
            [120, 240, 360],
            [30, 60, 90, 120],
            [10, 20, 30, 40, 50],
        ]
        expected = [
            ["R 90", "R 180", "R 270"],
            ["R 22", "R 45", "R 67", "R 90"],
            ["R 7", "R 15", "R 22", "R 30", "R 37"],
        ]
        for prices, exp in zip(lists_of_prices, expected):
            assert lp.heritage_sale(prices) == exp

    # ---------- Q3 gate_code ----------
    def _run_gate(self, monkeypatch, capsys, typed, code='9876'):
        monkeypatch.setattr('sys.stdin', StringIO(typed))
        lp.gate_code(code)
        return capsys.readouterr().out

    def test_gate_code_correct_first_try(self, monkeypatch, capsys):
        output = self._run_gate(monkeypatch, capsys, '9876\n')
        assert output.count('Enter your code:') == 1
        assert 'Gate Open!' in output
        assert 'Wrong code. Try again.' not in output

    def test_gate_code_incorrect_then_correct(self, monkeypatch, capsys):
        output = self._run_gate(monkeypatch, capsys, '1111\n9876\n')
        assert output.count('Enter your code:') == 2
        assert output.count('Wrong code. Try again.') == 1
        assert 'Gate Open!' in output

    def test_gate_code_multiple_incorrect_then_correct(self, monkeypatch, capsys):
        output = self._run_gate(monkeypatch, capsys, '1111\n2222\n3333\n9876\n')
        assert output.count('Enter your code:') == 4
        assert output.count('Wrong code. Try again.') == 3
        assert 'Gate Open!' in output

    def test_gate_code_stops_asking_after_correct(self, monkeypatch, capsys):
        output = self._run_gate(monkeypatch, capsys, '9876\n0000\n')
        assert output.count('Enter your code:') == 1

    # ---------- Q4 longest_dry_spell ----------
    def test_dry_spell_no_days(self):
        assert lp.longest_dry_spell([]) == 0

    def test_dry_spell_all_rain(self):
        assert lp.longest_dry_spell(['R', 'R', 'R']) == 0

    def test_dry_spell_all_dry(self):
        assert lp.longest_dry_spell(['D', 'D', 'D', 'D', 'D']) == 5

    def test_dry_spell_mixed(self):
        assert lp.longest_dry_spell(['D', 'R', 'D', 'D', 'R', 'D', 'D', 'D']) == 3

    def test_dry_spell_longest_in_middle(self):
        assert lp.longest_dry_spell(['R', 'D', 'D', 'D', 'D', 'D', 'R', 'D']) == 5

    def test_dry_spell_variations(self):
        test_cases = [
            (['D', 'R', 'D', 'D', 'R', 'D'], 2),
            (['R', 'R', 'D', 'D', 'D', 'R', 'D', 'D'], 3),
            (['D', 'D', 'R', 'R', 'D', 'D', 'D', 'D'], 4),
            (['R', 'D', 'R', 'D', 'R', 'D'], 1),
            (['D', 'D', 'D', 'R', 'R', 'R'], 3),
            (['R', 'D', 'R', 'D', 'D', 'R', 'D', 'D', 'D', 'R', 'R', 'D', 'D', 'D', 'R', 'D', 'D'], 3),
        ]
        for days, expected in test_cases:
            assert lp.longest_dry_spell(days) == expected

    # ---------- Q5 valley_finder ----------
    def test_valley_finder(self):
        assert lp.valley_finder([9, 4, 8, 7, 2, 6, 7, 8]) == [4, 2]

    def test_valley_finder_no_valleys(self):
        assert lp.valley_finder([1, 2, 3, 4, 5]) == []

    def test_valley_finder_multiple_valleys(self):
        assert lp.valley_finder([8, 3, 8, 3, 8, 3, 8]) == [3, 3, 3]

    def test_valley_finder_single_valley(self):
        assert lp.valley_finder([6, 4, 2, 4, 6]) == [2]

    def test_valley_finder_plateau_valley(self):
        assert lp.valley_finder([6, 4, 2, 2, 4, 6]) == []

    def test_valley_finder_edge_valleys(self):
        assert lp.valley_finder([1, 5, 9, 5, 1]) == []

    def test_valley_finder_short_lists(self):
        assert lp.valley_finder([]) == []
        assert lp.valley_finder([3]) == []
        assert lp.valley_finder([3, 1]) == []

    def test_valley_finder_variations(self):
        test_cases = [
            ([5, 2, 6, 3, 7, 4, 9], [2, 3, 4]),
            ([2, 1, 2, 1, 2, 1, 2], [1, 1, 1]),
            ([1, 3, 5, 7, 9], []),
            ([7, 2, 7, 2, 7], [2, 2]),
            ([4, 6, 4, 6, 4, 6, 4], [4, 4]),
        ]
        for data, expected in test_cases:
            assert lp.valley_finder(data) == expected

    # ---------- Q6 mac_validator ----------
    def test_mac_validator_valid(self):
        assert lp.mac_validator(['00:1a:2b:3c:4d:5e']) == {
            'valid_macs': ['00:1a:2b:3c:4d:5e'], 'invalid_macs': []}

    def test_mac_validator_uppercase_valid(self):
        assert lp.mac_validator(['AA:BB:CC:DD:EE:FF']) == {
            'valid_macs': ['AA:BB:CC:DD:EE:FF'], 'invalid_macs': []}

    def test_mac_validator_bad_character(self):
        assert lp.mac_validator(['00:1a:2b:3c:4d:5G']) == {
            'valid_macs': [], 'invalid_macs': ['00:1a:2b:3c:4d:5G']}

    def test_mac_validator_wrong_separator(self):
        assert lp.mac_validator(['00-1a-2b-3c-4d-5e']) == {
            'valid_macs': [], 'invalid_macs': ['00-1a-2b-3c-4d-5e']}

    def test_mac_validator_wrong_length(self):
        bad = ['00:1a:2b:3c:4d', '00:1a:2b:3c:4d:5e:6f', '']
        assert lp.mac_validator(bad) == {'valid_macs': [], 'invalid_macs': bad}

    def test_mac_validator_separator_in_wrong_place(self):
        bad = '001:a2:b3c:4d:5e:'   # 17 characters, colons misplaced
        assert len(bad) == 17
        assert lp.mac_validator([bad]) == {'valid_macs': [], 'invalid_macs': [bad]}

    def test_mac_validator_mixed(self):
        macs = [
            '00:1a:2b:3c:4d:5e',
            '00:1a:2b:3c:4d:5Z',
            'de:ad:be:ef:00:01',
            'de:ad:be:ef:00:0',
        ]
        assert lp.mac_validator(macs) == {
            'valid_macs': ['00:1a:2b:3c:4d:5e', 'de:ad:be:ef:00:01'],
            'invalid_macs': ['00:1a:2b:3c:4d:5Z', 'de:ad:be:ef:00:0'],
        }

    def test_mac_validator_empty_list(self):
        assert lp.mac_validator([]) == {'valid_macs': [], 'invalid_macs': []}

    # ---------- Q7 stock_runout ----------
    def test_stock_runout_no_stock_no_demand(self):
        assert lp.stock_runout(0, []) == "Stock is empty."

    def test_stock_runout_no_stock_with_demand(self):
        assert lp.stock_runout(0, [5, 5, 5]) == "Stock is empty."

    def test_stock_runout_exact_depletion(self):
        assert lp.stock_runout(100, [30, 20, 50]) == "Stock will last the whole period. Remaining stock: 0"

    def test_stock_runout_surplus(self):
        assert lp.stock_runout(50, [10, 15, 5]) == "Stock will last the whole period. Remaining stock: 20"

    def test_stock_runout_runs_out_early(self):
        assert lp.stock_runout(40, [15, 10, 20, 5]) == "Stock will run out on day 3."

    def test_stock_runout_runs_out_first_day(self):
        assert lp.stock_runout(10, [15, 5, 5]) == "Stock will run out on day 1."

    def test_stock_runout_no_demand(self):
        assert lp.stock_runout(25, [0, 0, 0]) == "Stock will last the whole period. Remaining stock: 25"

    def test_stock_runout_empty_projection(self):
        assert lp.stock_runout(12, []) == "Stock will last the whole period. Remaining stock: 12"

    def test_stock_runout_variations(self):
        test_cases = [
            (60, [20, 15, 10], "Stock will last the whole period. Remaining stock: 15"),
            (25, [10, 10, 10], "Stock will run out on day 3."),
            (0, [1, 1, 1], "Stock is empty."),
            (100, [30, 30, 50], "Stock will run out on day 3."),
            (45, [15, 15, 15], "Stock will last the whole period. Remaining stock: 0"),
        ]
        for stock, demand, expected in test_cases:
            assert lp.stock_runout(stock, demand) == expected
