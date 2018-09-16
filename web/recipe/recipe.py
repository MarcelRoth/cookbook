import json
import os.path

from flask import render_template, request, Blueprint
from flask import current_app as app

from web.core import rezeptOeffnen

bp = Blueprint('recipe', __name__, url_prefix='/', template_folder='templates')


@bp.route("/")
def hello():
    return render_template('search.html')


@bp.route("/recipe/show")
def show():
    recipe_name = request.args.get("recipeName")
    if os.path.isfile(recipe_name + ".rzp") :
        data=json.loads(rezeptOeffnen.load(recipe_name))
        return render_template('recipe.html',
                               recipeNameData=data.get("recipeName"),
                               incredNameData=data.get("incredName"),
                               prepTextData=data.get("prepText")
                               )
    else:
        return 'Rezept {} nicht gefunden.'.format(recipe_name)


@bp.route("/recipe/create")
def create():
    return render_template('recipe.html')


@bp.route("/recipe/save", methods=['POST'])
def save():
    save_path = app.config.get("SAVE_PATH")
    file = open(save_path + request.form.get("recipeName") + ".rzp", "w")
    file.write(json.dumps(request.form))
    return render_template('recipe.html',
                          recipeNameData=request.form.get("recipeName"),
                          ZutatenData=request.form.get("Zutaten"),
                          ZubereitungData=request.form.get("Zubereitung")
                          )