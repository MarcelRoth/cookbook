import sys
from pymongo import MongoClient
from pymongo.collation import Collation

class Respository :

    def __init__(self, config) :
        self.__client = MongoClient(config.get('MONGO_URL'))
        data_db = self.__client[config.get('MONGO_DATA')]
        self.__recipes = data_db.get_collection(config.get('MONGO_DATA_RECIPES'))

    def createRecipe(self, document) :
        return self.__recipes.insert_one(document)

    def readRecipe(self, id) :
        return self.__recipes.find_one({'_id': id})

    def findSingleRecipe(self, name) :
        return self.__recipes.find_one({'recipeName': name}, collation=Collation(locale='de', strength=1))

def main(args) :
    rep = Respository({})
    print(rep.createRecipe({'name': 'mydocument'}))

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
