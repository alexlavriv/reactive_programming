import json


def line_reader_generator(file_name):
    with open(file_name) as file:
        while True:
            data = file.readline()
            if data:
                yield json.loads(data)
            else:
                return False

def prepare_string(text):
    for ch in ['!','#',',','.','&']:
        if ch in text:
            text = text.replace(ch," ")
    return text.lower()    


def filter_parser(*args):
    keywords, includes, excludes = [], [], []
    for parsed in args[0]:
        if parsed.startswith('-'):
            excludes.append(parsed[1:].lower())
        elif parsed.startswith('+'):
            includes.append(parsed[1:].lower())
        else:
            keywords.append(parsed.lower())

    return keywords, includes, excludes

# This function will join all the field to one string
def join_recipe(recipe):
    joined_str = prepare_string(' '.join(val for val in recipe.values()))

    return joined_str

def filter_(recipe, keywords, includes, excludes):


    recipe_str = join_recipe(recipe) 
    ings = prepare_string(recipe["ingredients"])
    
    if (all(keyword in recipe_str for keyword in keywords) and
         all(include in ings for include in includes) and
          not any(exlclude in ings for exlclude in excludes)):
        return True

    return False


def search(file_name,*args):
    reader = line_reader_generator(file_name)
    keywords, includes, excludes = filter_parser(args)
    for recipe in reader:
        if filter_(recipe, keywords, includes, excludes):
            yield recipe
#res = statistics(count, search('openrecipes.txt', 'eggs',  '+eggs', '-milk', '-rice'), property=None)
def statistics(aggregate_function, data, property=None):
    if property==None:
        return aggregate_function ([current for current in data])
    else:
        return aggregate_function ([current[property] for current in data])

def main():

    recipes = search("openrecipes.json",'Pork', '+garlic', '-Herbs', '-fdjdsjf')
    print(statistics(sum_strings, recipes, property='recipeYield'))


def sum_strings (lst):
    return sum([int(t) for t in lst])
if __name__ == '__main__':
    main()