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
    reader = line_reader_generator("openrecipes.json")
    for _ in range(1):
        for key,value in next(reader).items():
            print('%s: %s'%(key,value))


if __name__ == '__main__':
    main()
