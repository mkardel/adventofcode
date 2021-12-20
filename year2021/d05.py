#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from copy import copy
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __lt__(self, other):
        return self.x < other.x or self.y < other.y

    def __le__(self, other):
        if self == other:
            return True
        return self < other

    def incr(self, other):
        if self.x < other.x:
            self.x += 1
        elif other.x < self.x:
            self.x -= 1
        if self.y < other.y:
            self.y += 1
        elif other.y < self.y:
            self.y -= 1

    def __repr__(self):
        return f'{self.x}_{self.y}'

    def __hash__(self):
        return self.x + self.y


@dataclass
class Line:
    source: Point
    target: Point

    def __init__(self, p1, p2):  # Store sorted
        self.source = p1 if p1 < p2 else p2
        self.target = p2 if p1 < p2 else p1

    def draw(self, board):
        source_copy = copy(self.source)
        while source_copy <= self.target:
            s = str(source_copy)
            if board.get(s, None):
                board[s] += 1
            else:
                board[s] = 1
            if source_copy == self.target:
                return
            source_copy.incr(self.target)

    def is_straight(self):
        return self.source.x == self.target.x or self.source.y == self.target.y

    def is_diagonal(self):
        return abs(self.source.x - self.target.x) == abs(self.source.y - self.target.y)
        

def drawing_sum(d) -> int:
    return sum([1 for _, v in d.items() if v >= 2])


def read_input(filename):
    lines = []
    with open(filename, 'r') as f:
        while l := f.readline():
            source, target = l.split('->')
            x1_str, y1_str = source.strip().split(',')
            p1 = Point(int(x1_str), int(y1_str))
            x2_str, y2_str = target.strip().split(',')
            p2 = Point(int(x2_str), int(y2_str))
            lines.append(Line(p1, p2))
    return lines


def eval_lines(lines):
    board = dict()
    for l in lines:
        l.draw(board)
    return drawing_sum(board)


def p1(filename):
    lines = [l for l in read_input(filename) if l.is_straight()]
    return eval_lines(lines)

def p2(filename):
    lines = [l for l in read_input(filename) if l.is_straight() or l.is_diagonal()]
    return eval_lines(lines)


if __name__ == "__main__":
    sample_p1 = p1('d05_sample')
    assert sample_p1 == 5
    print(p1('d05'))

    sample_p2 = p2('d05_sample')
    assert sample_p2 == 12
    print(p2('d05'))
