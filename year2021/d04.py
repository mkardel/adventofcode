from typing import List

BINGO_NUMBERS = [4,75,74,31,76,79,27,19,69,46,98,59,83,23,90,52,87,6,11,92,80,51,43,5,94,17,15,67,25,30,48,47,62,71,85,58,60,1,72,99,3,35,42,10,96,49,37,36,8,44,70,40,45,39,0,63,2,78,68,53,50,77,20,55,38,86,54,93,26,88,12,91,95,34,9,14,33,66,41,13,28,57,29,73,56,22,89,21,64,61,32,65,97,84,18,82,81,7,16,24]


class BingoField:
    def __init__(self, num):
        self._num = num
        self._hit = False

    def get_num(self) -> int:
        return self._num

    def hit(self, num):
        if self._num == num:
            self._hit = True

    def is_hit(self) -> bool:
        return self._hit

    def __repr__(self):
        hit_str = "(X)" if self._hit else "( )"
        return f'{self._num} {hit_str}'


class BingoCard:
    def __init__(self):
        self._list = []
        self.has_won = False

    def is_winner(self) -> bool:
        is_winner = self._has_winning_row() or self._has_winning_column()
        if is_winner:
            self.has_won = True
        return is_winner

    def _has_winning_row(self):
        return self._is_winning_row_or_col('row')

    def _has_winning_column(self):
        return self._is_winning_row_or_col('col')

    def _is_winning_row_or_col(self, identifier):
        iterator = self.columns()
        if identifier == 'row':
            iterator = self.rows()
        for items in iterator:
            winning_items = all([num.is_hit() for num in items])
            if winning_items:
                return True
        return False

    def rows(self):
        for row in self._list:
            yield row

    def columns(self):
        for col_idx in range(len(self._list)):
            col = []
            for row in self._list:
                col.append(row[col_idx])
            yield col

    def add_row(self, nums: List[BingoField]):
        self._list.append(nums)

    def add_row_str(self, str_nums: List[str]):
        bingo_fields = []
        for str_num in str_nums:
            if len(str_num):
                bingo_fields.append(BingoField(int(str_num.strip())))
        self.add_row(bingo_fields)

    def __iter__(self):
        for row in self.rows():
            for num in row:
                yield num

    def hit(self, number):
        for num in self:
            num.hit(number)

    def unmarked_numbers(self):
        return [num.get_num() for num in self if not num.is_hit()]

    def unmarked_sum(self):
        return sum(self.unmarked_numbers())

    def __repr__(self):
        return str([num for num in self._list])


def read_bingo_cards() -> List[BingoCard]:
    bingo_cards = []
    with open('d04', 'r') as f:
        current_bingo_card = BingoCard()
        while line := f.readline():
            line = line.strip()
            if len(line) == 0:
                bingo_cards.append(current_bingo_card)
                current_bingo_card = BingoCard()
            else:
                nums = line.split(' ')
                current_bingo_card.add_row_str(nums)
    return bingo_cards


def p01():
    bingo_cards = read_bingo_cards()
    winner = False
    for number in BINGO_NUMBERS:
        for card in bingo_cards:
            card.hit(number)
            if card.is_winner():
                print(card.unmarked_sum() * number)
                winner = True
                break
        if winner:
            break


def p02():
    bingo_cards = read_bingo_cards()
    for number in BINGO_NUMBERS:
        cards = [card for card in bingo_cards if not card.has_won]
        for card in cards:
            card.hit(number)
            if card.is_winner():
                if len(cards) == 1:
                    print(card.unmarked_sum() * number)


if __name__ == "__main__":
    p01()
    p02()
