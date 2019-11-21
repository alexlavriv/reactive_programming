import json


def denerate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def line_reader_generator(file_name):
    with open(file_name) as file:
        while True:
            data = file.readline()
            if data:
                yield json.loads(data)


def main():
    reader = line_reader_generator("openrecipes.txt")
    for _ in range(100):
        for x in next(reader).values() :
            print(x)


if __name__ == '__main__':
    main()
