import sys
import glob
from pathlib import Path


class Constants:
    RECIPE_FILE_ENDING = ".rzp"


def load(name: str):
    file = open(name + Constants.RECIPE_FILE_ENDING, "rt")
    content = file.read()
    file.close()
    return content


def create(name: str):
    file = open(name + Constants.RECIPE_FILE_ENDING, "wt")
    file.write("Zutaten\n")
    file.close()


def add(name: str, toAdd: str):
    file = open(name + Constants.RECIPE_FILE_ENDING, "at")
    file.write(toAdd)
    file.close()


def load_all():
    recipes = []
    for file in glob.glob("./*" + Constants.RECIPE_FILE_ENDING):
        recipe = Recipe(file.lstrip("./").rstrip(Constants.RECIPE_FILE_ENDING))
        recipe.load_or_create()
        recipes.append(recipe)
    return recipes

def main(args):
    if args[0] == "create":
        create(args[1])
    elif args[0] == "load":
        load(args[1])
    elif args[0] == "add":
        add(args[1], args[2])


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])


class Recipe:

    def __init__(self, name):
        self.content = ""
        self.name = name
        self.exists = self.exist()

    def exist(self):
        return Path("./"+self.name + Constants.RECIPE_FILE_ENDING).is_file()

    def load_or_create(self):
        if self.exists:
            self.content = load(self.name)
        else:
            create(self.name)

    def save(self):
        add(self.name, self.content)
