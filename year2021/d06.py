SAMPLE_INPUT = [3, 4, 3, 1, 2]
SAMPLE_STEPS = 18


def prepare_initial(arr):
    d = dict()
    for val in range(9):
        d[val] = arr.count(val)
    return d


def p1(filename=None, steps=None):
    if filename is None:
        data = SAMPLE_INPUT
    else:
        with open(filename, 'r') as f:
            nums_str = f.readline().split(',')
            data = [int(n.strip()) for n in nums_str] 
    if steps is None:
        steps = SAMPLE_STEPS
    population = prepare_initial(data) 
    for i in range(steps):
        new_fish = population.get(0, 0)
        for k, v in population.items():
            if k == 0:
                continue
            population[k - 1] = v
        population[8] = new_fish
        population[6] += new_fish
    return sum([v for _, v in population.items()])


if __name__ == '__main__':
    sample_p1 = p1()
    assert sample_p1 == 26

    sample_p1_80 = p1(steps=80)
    assert sample_p1_80 == 5934

    print(p1(filename='d06', steps=80))

    sample_p2_256 = p1(steps=256)
    assert sample_p2_256 == 26984457539

    print(p1(filename='d06', steps=256))
