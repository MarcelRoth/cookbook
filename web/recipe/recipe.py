import json
import os.path
import re

from flask import render_template, request, Blueprint
from flask import current_app as app

from web.core import rezeptOeffnen

bp = Blueprint('recipe', __name__,
               url_prefix='/',
               static_url_path='/recipe/static',
               static_folder='./static',
               template_folder='./templates')
ingRegex = re.compile('([\w]+)\[([0-9]+)\]\[([\w]+)\]')

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
    return render_template('recipe.html', data=create_empty_recipe_data())


@bp.route("/recipe/save", methods=['POST'])
def save():
    save_path = app.config.get("SAVE_PATH")
    file = open(save_path + request.form.get("recipeName") + ".rzp", "w")
    data = reformat(request.form)
    file.write(json.dumps(data, indent=4))
    return render_template('recipe.html', data=data)


def reformat(formData):
    outData = dict()
    outData["recipeName"] = formData["recipeName"]
    all_ingreds_pre = dict()
    for key in formData:
        result = ingRegex.match(key)
        if result :
            groups = result.groups()
            if groups[0] == "allIngreds" :
                ingred_no = groups[1]
                single_ingred = all_ingreds_pre.setdefault(ingred_no, dict())
                single_ingred[groups[2]] = formData[key]

    all_ingreds = list()
    for key in sorted(all_ingreds_pre.keys()) :
        all_ingreds.append(all_ingreds_pre[key])

    outData["allIngreds"] = all_ingreds
    outData["prepText"] = formData["prepText"]
    return outData


def create_empty_recipe_data():
    return {"allIngreds": [{}, {}]}
