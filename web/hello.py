from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():
    return render_template('template.html', buttonname='Klücke mich')