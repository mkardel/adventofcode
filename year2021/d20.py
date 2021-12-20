def read_algo(filename):
    with open(filename, 'r') as f:
        x = f.readline().strip()
    arr = list(x)
    out_arr = []
    for a in arr:
        if a == '#':
            out_arr.append(1)
        else:
            out_arr.append(0)
    return out_arr


def to_str_pos(x, y):
    return f'{x}_{y}'


def read_data(filename):
    d = dict()
    with open(filename, 'r') as f:
        row = 0
        while x := f.readline():
            x = x.strip()
            for col, c in enumerate(x):
                d[to_str_pos(row, col)] = 1 if c == '#' else 0
            row += 1
    return d


def get_num(d, pos):
    bin_address = ''
    x_str, y_str = pos.split('_')
    x, y = int(x_str), int(y_str)
    for xi in (x - 1, x, x + 1):
        for yi in (y - 1, y, y + 1):
            val = d.get(to_str_pos(xi, yi), 0)
            bin_address += str(val)
    dec_address = 0
    for idx, c in enumerate(bin_address[::-1]):
        dec_address += int(c) * 2**idx 
    return dec_address


def non_zero_px_count(d):
    return sum([1 for _, v in d.items() if v])


def eval_image(data, algo, steps):
    for i in range(steps):
        new_d = dict()
        for k, _ in data.items():
            algo_pos = get_num(data, k)
            new_d[k] = algo[algo_pos]
        data = new_d
    return data


def p1(algo_file='d20_sample_algo', data_file='d20_sample', steps=2):
    algo = read_algo(algo_file)
    data = read_data(data_file)
    image = eval_image(data, algo, steps)
    return non_zero_px_count(image)


if __name__ == '__main__':
    px_count = p1()
    assert px_count == 35

    print(p1('d20_algo', 'd20', 2))
