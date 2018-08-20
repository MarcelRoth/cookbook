import os.path
import json

from flask import Flask, render_template, request

from web.core import rezeptOeffnen

app = Flask(__name__)
RECIPE_NAME_INPUT = 'recipeNameInput'

@app.route("/")
def hello():
    return render_template('search.html',
                           recipeNameInput=RECIPE_NAME_INPUT)


@app.route("/recipe/show")
def show():
    recipe_name = request.args.get(RECIPE_NAME_INPUT)
    if os.path.isfile(recipe_name + ".rzp") :
        data=json.loads(rezeptOeffnen.load(recipe_name))
        return render_template('recipe.html',
                               recipeNameData=data.get("recipeName"),
                               ZutatenData=data.get("Zutaten"),
                               ZubereitungData=data.get("Zubereitung")
                               )
    else:
        return 'Rezept {} nicht gefunden.'.format(recipe_name)


@app.route("/recipe/create")
def create():
    return render_template('recipe.html')


@app.route("/recipe/save", methods=['POST'])
def save():
    file = open(request.form.get("recipeName")+".rzp", "w")
    file.write(json.dumps(request.form))
    return render_template('recipe.html',
                          recipeNameData=request.form.get("recipeName"),
                          ZutatenData=request.form.get("Zutaten"),
                          ZubereitungData=request.form.get("Zubereitung")
                          )