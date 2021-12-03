from typing import Any, Callable, List
import os

from helper import read_input


def bin_str_to_decimal(num: str) -> int:
    reverse = num[::-1]
    result = 0
    for i in range(len(num)):
        result += int(reverse[i]) * (2 ** i)
    return result


def extract_digits(bin_strings: List[str]) -> List[List[int]]:
    all_numbers = []
    for digit_index in range(len(bin_strings[0])):
        digit_numbers = []
        for num in bin_strings:
            digit_numbers.append(int(num[digit_index]))
        all_numbers.append(digit_numbers)
    return all_numbers


def find_most_common_binary_digit(l):
    return find_common_binary_digit(l, True)


def find_least_common_binary_digit(l):
    return find_common_binary_digit(l, False)


def find_common_binary_digit(l: List[int], most_common=True) -> str:
    list_copy = l.copy()
    list_copy.sort()
    first_1 = list_copy.index(1)
    if first_1 <= (len(list_copy) // 2):
        return '1' if most_common else '0'
    else:
        return '0' if most_common else '1'


def p01():
    input_file = os.path.splitext(os.path.basename(__file__))[0]
    diagnostics = read_input(input_file, str)
    nums = extract_digits(diagnostics)
    gamma = ''
    epsilon = ''
    for digit_index in range(len(nums)):
        most_common_number = find_most_common_binary_digit(nums[digit_index])
        if int(most_common_number):  # It's 1!
            gamma += str(1)
            epsilon += str(0)
        else:
            gamma += str(0)
            epsilon += str(1)
    return bin_str_to_decimal(gamma) * bin_str_to_decimal(epsilon)


def filter_nums_index_by_digit(l: List[str], digit: str, index: int):
    res = []
    for item in l:
        if item[index] == digit:
            res.append(item)
    return res


def filter_inputs(l: List[str], discriminator_func: Callable[[List[Any]], Any]) -> str:
    out = l.copy()
    for i in range(len(l[0])):
        if len(out) == 1:
            break
        digits = extract_digits(out)  # extract digits
        filter_by = discriminator_func(digits[i])
        out = filter_nums_index_by_digit(out, filter_by, i)
    return out[0]


def p02():
    input_file = os.path.splitext(os.path.basename(__file__))[0]
    nums = read_input(input_file, str)
    oxygen = filter_inputs(nums, find_most_common_binary_digit)
    co2 = filter_inputs(nums, find_least_common_binary_digit)
    return bin_str_to_decimal(oxygen) * bin_str_to_decimal(co2)


if __name__ == '__main__':
    print(p01())
    print(p02())