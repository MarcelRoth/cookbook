import json
import os.path

from flask import render_template, request, Blueprint
from flask import current_app as app

from web.core import repository

bp = Blueprint('recipe', __name__, url_prefix='/', template_folder='templates')


@bp.route("/")
def hello():
    return render_template('search.html')


@bp.route("/recipe/show")
def show():
    recipe_name = request.args.get("recipeName")
    result = app.repository.findSingleRecipe(recipe_name)
    if result:
        return render_template('recipe.html', data=result)
    else:
        return 'Rezept {} nicht gefunden.'.format(recipe_name)


@bp.route("/recipe/create")
def create():
    return render_template('recipe.html', data=create_empty_recipe_data())


def reformat(formData):
    outData = dict()
    outData["recipeName"] = formData["recipeName"]
    all_ingreds = list()
    single_ingred = dict()
    single_ingred["ingredAmount"] = formData["ingredAmount1"]
    single_ingred["ingredMeasure"] = formData["ingredMeasure1"]
    single_ingred["ingredName"] = formData["ingredName1"]
    all_ingreds.append(single_ingred)
    single_ingred = dict()
    single_ingred["ingredAmount"] = formData["ingredAmount2"]
    single_ingred["ingredMeasure"] = formData["ingredMeasure2"]
    single_ingred["ingredName"] = formData["ingredName2"]
    all_ingreds.append(single_ingred)
    outData["allIngreds"] = all_ingreds
    outData["prepText"] = formData["prepText"]
    return outData


@bp.route("/recipe/save", methods=['POST'])
def save():
    data = reformat(request.form)
    app.repository.createRecipe(data)
    return render_template('recipe.html', data=data)


def create_empty_recipe_data():
    return {"allIngreds": [{}, {}]}
