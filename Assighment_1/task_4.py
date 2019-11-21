import json


def line_reader_generator(file_name):
    with open(file_name) as file:
        while True:
            data = file.readline()
            if data:
                yield json.loads(data)


def filter_parser(*args):
    keywords, includes, excludes = [], [], []
    for parsed in args:
        if parsed[0] == '-':
            excludes.append(parsed)
        elif parsed[0] == '+':
            includes.append(parsed)
        else:
            keywords.append(parsed)
    print(keywords, includes, excludes)
    return keywords, includes, excludes


def filter_(recipe, keywords, includes, excludes):
    flag = True
    while flag:
        for keyword in keywords:
            # print(recipe.values())
            if keyword not in recipe.values():
                flag = False
                break
        # for include_ingredient, exclude_ingredient in zip(includes, excludes):
        # for include_ingredient in includes:
        #     # print(recipe['ingredients'])
        #     if include_ingredient not in recipe['ingredients']:
        #         flag = False
        #         break
        # print('out')
    print('ret')
    return flag


def search(file_name, *args):
    reader = line_reader_generator(file_name)
    keywords, includes, excludes = filter_parser(args)
    for recipe in reader:
        if filter_(recipe, keywords, includes, excludes):
            yield recipe


def main():
    recipes = search("openrecipes.txt", 'eggs', '+eggs', '-milk', '-rice')
    next(recipes)


if __name__ == '__main__':
    main()