import pytest

from solution import repeating_decimals_to_fraction


class TestRepeatingDecimalsToFractions(object):

    def test_repeating_decimals_to_fraction_1(self):
        res = repeating_decimals_to_fraction('0.(6)')
        assert res == '2/3'

    def test_repeating_decimals_to_fraction_2(self):
        res = repeating_decimals_to_fraction('1.(1)')
        assert res == '10/9'

    def test_repeating_decimals_to_fraction_3(self):
        res = repeating_decimals_to_fraction('3.(142857)')
        assert res == '22/7'

    def test_repeating_decimals_to_fraction_4(self):
        res = repeating_decimals_to_fraction('0.(36)')
        assert res == '4/11'

    def test_invalid_format_input(self):
        with pytest.raises(ValueError):
            repeating_decimals_to_fraction('0.36')
