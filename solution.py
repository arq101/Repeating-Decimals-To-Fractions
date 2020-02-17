#!/usr/bin/env python3

import argparse
from fractions import Fraction
from sympy import Symbol, Eq, solve
import re


def repeating_decimals_to_fraction(str_decimal):
    """Takes a number in string form with its repeating decimal part enclosed in parentheses
    and returns the equivalent number in fraction string form.
    """
    decimal_str_pattern = r'(\d+)\.\((\d+)\)'   # eg. 3.(142857)
    if re.fullmatch(decimal_str_pattern, str_decimal):

        # capture the substrings ...
        whole_number = re.fullmatch(decimal_str_pattern, str_decimal).group(1)
        recurring_digits = re.fullmatch(decimal_str_pattern, str_decimal).group(2)

        # the number of 10s needed to multiply recurring decimal to move it to the left of the decimal point
        base_10_multiplier = 10 ** len(recurring_digits)

        # prepare the equation ...
        #   eg.
        #   (base_10_multiplier * x) - x = recurring_digits.recurring_digits
        #
        #   eg. where x = 0.666 and repeating digit is 6
        #
        #         10x = 6.666         # on RHS move repeating digit 1 place to the left of decimal place, x10 on the LHS
        #     10x - x = 6.666 - 0.666    # subtract repeating fraction part from both sides
        #          9x = 6
        #           x = 6/9
        #
        x = Symbol('x')
        equation = Eq(base_10_multiplier * x - x, int(recurring_digits))
        rational_number = solve((equation,), (x,))[x]

        # create improper fraction if needed ...
        if int(whole_number) > 0:
            fraction_obj = Fraction(rational_number)
            whole_number = int(whole_number)
            numerator = (whole_number * fraction_obj.denominator()) + fraction_obj.numerator()
            denominator = fraction_obj.denominator()
            return f'{numerator}/{denominator}'

        return str(rational_number)

    else:
        raise ValueError(
            'Invalid string format: expecting the repeating fractional part of a decimal to be '
            'enclosed in parentheses ... eg. "3.(142857)"'
        )


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Script takes a decimal in string form with the repeating part in parentheses and '
                    'returns the equivalent fraction in string form and in lowest terms.')
    # positional arg
    parser.add_argument('decimal_fraction', action='store',
                        help='decimal value in the form "0.(6)", "3.(36)", etc '
                             'where the digit(s) in the parentheses represent digits that repeat infinitely')
    args = parser.parse_args()
    return args


def main():
    cmdline_args = arg_parser()
    fraction = repeating_decimals_to_fraction(cmdline_args.decimal_fraction)
    print(fraction)


if __name__ == '__main__':
    main()
