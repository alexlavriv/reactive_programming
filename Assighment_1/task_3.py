def generate_n_grams(size, words_list):
    for w_count in range(len(words_list) - size + 1):
        res = []
        for t in range(size):
            res.append(words_list[w_count + t])
        yield res


def generate_sentence(subjects, verbs, objects):
    for t in range(len(subjects)):
        res = '%s %s %s' % (subjects[t], verbs[t], objects[t])
        yield res


def generate_permutations(some_list):
    if len(some_list) == 1:
        yield some_list
    else:
        for perm in generate_permutations(some_list[1:]):
            for i, _ in enumerate(some_list):
                yield perm[:i] + some_list[0:1] + perm[i:]


def main():
    print("\n3.1:\n")
    sentence = "The fat red fox jumped over the crazy black dog"
    n_grams = generate_n_grams(3, sentence.split())
    print(type(n_grams))
    for x in n_grams:
        print(x)

    print("\n3.2:\n")
    subjects = ["I", "You"]
    verbs = ["play", "love"]
    objects = ["Basketball", "Football"]
    for sentence in generate_sentence(subjects, verbs, objects):
        print(sentence)

    print("\n3.3:\n")
    some_list1 = [1, 2]
    for perm in generate_permutations(some_list1):
        print(perm)
    some_list2 = [1, 'a', True]
    for perm in generate_permutations(some_list2):
        print(perm)


if __name__ == '__main__':
    main()

