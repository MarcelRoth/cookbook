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
    save_path = app.config.get("SAVE_PATH")
    if os.path.isfile(save_path + recipe_name + ".rzp"):
        data = json.loads(rezeptOeffnen.load(save_path + recipe_name))
        return render_template('recipe.html', data=data)
    else:
        return 'Rezept {} nicht gefunden.'.format(recipe_name)


@bp.route("/recipe/create")
def create():
    return render_template('recipe.html', data=dict())


@bp.route("/recipe/save", methods=['POST'])
def save():
    save_path = app.config.get("SAVE_PATH")
    file = open(save_path + request.form.get("recipeName") + ".rzp", "w")
    file.write(json.dumps(request.form, indent=4))
    return render_template('recipe.html', data=request.form)
