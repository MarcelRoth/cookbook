import os.path

from flask import Flask, render_template, request

from web.core import rezeptOeffnen

app = Flask(__name__)
RECIPE_NAME_INPUT = 'recipeNameInput'

@app.route("/")
def hello():
    return render_template('search.html',
                           recipeNameInput=RECIPE_NAME_INPUT)


@app.route("/receipe")
def receipe():
    recipe_name = request.args.get(RECIPE_NAME_INPUT)
    if os.path.isfile(recipe_name + ".rzp") :
        return rezeptOeffnen.load(recipe_name)
    else:
        return 'Rezept {} nicht gefunden.'.format(recipe_name)


