from typing import Any, List, Tuple, Type


def read_input(filename: str, cast_to: Type = int) -> List[Any]:
    nums = []
    with open(filename, 'r') as f:
        while l := f.readline().strip():
            nums.append(cast_to(l))
    return nums


def read_sub_commands(filename: str) -> List[Tuple[str, int]]:
    commands = []
    with open(filename, 'r') as f:
        while l := f.readline():
            cmd, number = l.split(' ')
            commands.append((cmd, int(number)))
    return commands
