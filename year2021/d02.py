from typing import List, Tuple
import os
from helper import read_sub_commands


def _get_inputs() -> List[Tuple[str, int]]:
    input_file = os.path.splitext(os.path.basename(__file__))[0]
    return read_sub_commands(input_file)


def _process_command(command: str, number: int) -> Tuple[int, int]:
    dx, dy = 0, 0
    if command == 'forward':
        dx = number
    elif command == 'up':
        dy -= number
    elif command == 'down':
        dy = number
    return dx, dy


def p01():
    commands = _get_inputs()
    x, y = 0, 0
    for cmd, num in commands:
        dx, dy = _process_command(cmd, num)
        x += dx
        y += dy
    return x * y


def p02():
    commands = _get_inputs()
    x, y, aim = 0, 0, 0
    for cmd, num in commands:
        dx, daim = _process_command(cmd, num)
        x += dx
        aim += daim
        if dx:
            y += dx * aim
    return x * y


if __name__ == '__main__':
    print(p01())
    print(p02())