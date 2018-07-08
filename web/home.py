from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextAreaField
from flask import url_for, redirect
from core import rezeptManagement
from core.rezeptManagement import Recipe
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'please, tell nobody'


class RecipeForm(FlaskForm):
    name = StringField(u'Name of the recipe')
    content = TextAreaField(u'content')
    submit = SubmitField(u'save')


@app.route("/")
def home():
    form = RecipeForm()
    recipes = rezeptManagement.load_all()
    return render_template('index.html', form=form, recipes=recipes)


@app.route(u'/new', methods=[u'POST'])
def new_recipe():
    form = RecipeForm()
    new_recipe = Recipe(form.name.data)
    new_recipe.content = form.content.data
    new_recipe.save()
    return redirect(url_for('home'))


@app.route("/alive")  # take note of this decorator syntax, it's a common pattern
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
