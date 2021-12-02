from typing import List
import os
from helper import read_input


def _solve(numbers: List[int]) -> int:
    count = 0
    for num1, num2 in zip(numbers, numbers[1:]):
        if num2 > num1:
            count += 1
    return count


def _get_inputs() -> List[int]:
    input_file = os.path.splitext(os.path.basename(__file__))[0]
    return read_input(input_file, int)


def p01():
    return _solve(_get_inputs())


def p02():
    inputs = _get_inputs()
    windowed_inputs = [x + y + z for x, y, z in zip(inputs, inputs[1:], inputs[2:])]
    return _solve(windowed_inputs)


if __name__ == '__main__':
    print(p01())
    print(p02())