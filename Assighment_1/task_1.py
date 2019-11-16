def p_1_lc(inputlist):
    return [i + x + 1 for i, x in enumerate(inputlist)]


def p_1_fo(inputlist):
    return list(map(lambda i_x: i_x[0] + i_x[1] + 1, enumerate(inputlist)))


def p_2_lc(inputlist):
    return [True if x % 3 == 0 else False for x in inputlist]


def p_2_fo(inputlist):
    return list(map(lambda x: x % 3 == 0, inputlist))


def p_3_lc(inputlist):
    return [x ** 2 for x in inputlist]


def p_3_fo(inputlist):
    return list(map(lambda x: x ** 2, inputlist))


def p_4_lc(inputlist):
    return [word[0].upper() for word in inputlist]


def p_4_fo(inputlist):
    return list(map(lambda word: word[0].upper(), inputlist))


def p_5_lc(inputlist):
    return [word for word in inputlist if 'p' in word]


def p_5_fo(inputlist):
    return list(filter(lambda word: 'p' in word, inputlist))


def p_6_lc(inputlist):
    return [(word, len(word)) for word in inputlist]


def p_6_fo(inputlist):
    return list(map(lambda word: (word, len(word)), inputlist))


def p_7_lc(inputlist):
    return [x for x in inputlist if x % 2 != 0]


def p_7_fo(inputlist):
    return list(filter(lambda x: x % 2 != 0, inputlist))


def p_8_lc(inputlist):
    return [inputlist[i] for i in range(len(inputlist)) if i % 2 == 0]


def p_8_fo(inputlist):
    return list(map(lambda i_x: i_x[1], filter(lambda i_x: i_x[0] % 2 == 0, enumerate(inputlist))))


def main():
    print("p_1_lc([0, 1, 2, 3]) -> ", p_1_lc([0, 1, 2, 3]))
    print("p_1_fo([0, 1, 2, 3]) -> ", p_1_fo([0, 1, 2, 3]))
    print("p_2_lc([3, 5, 9, 8]) -> ", p_2_lc([3, 5, 9, 8]))
    print("p_2_fo([3, 5, 9, 8]) -> ", p_2_fo([3, 5, 9, 8]))
    print("p_3_lc([1, 2, 3, 4, 5, 6, 7, 8, 9]) -> ", p_3_lc([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("p_3_fo([1, 2, 3, 4, 5, 6, 7, 8, 9]) -> ", p_3_fo([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("p_4_lc([\"apple\", \"orange\", \"pear\"]) -> ", p_4_lc(["apple", "orange", "pear"]))
    print("p_4_fo([\"apple\", \"orange\", \"pear\"]) -> ", p_4_fo(["apple", "orange", "pear"]))
    print("p_5_lc([\"apple\", \"orange\", \"pear\"]) -> ", p_5_lc(["apple", "orange", "pear"]))
    print("p_5_fo([\"apple\", \"orange\", \"pear\"]) -> ", p_5_fo(["apple", "orange", "pear"]))
    print("p_6_lc([\"apple\", \"orange\", \"pear\"]) -> ", p_6_lc(["apple", "orange", "pear"]))
    print("p_6_fo([\"apple\", \"orange\", \"pear\"]) -> ", p_6_fo(["apple", "orange", "pear"]))
    print("p_7_lc([0, 1, 2, 3, 4, 5, 6, 8]) -> ", p_7_lc([0, 1, 2, 3, 4, 5, 6, 8]))
    print("p_7_fo([0, 1, 2, 3, 4, 5, 6, 8]) -> ", p_7_fo([0, 1, 2, 3, 4, 5, 6, 8]))
    print("p_8_lc([1, 2, 4, 5, 7]) -> ", p_8_lc([1, 2, 4, 5, 7]))
    print("p_8_fo([1, 2, 4, 5, 7]) -> ", p_8_fo([1, 2, 4, 5, 7]))


if __name__ == '__main__':
    main()
