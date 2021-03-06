from flask import Flask
from web.recipe import recipe


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    # other setup tasks
    app.config.from_pyfile("config/app.conf", silent=False)
    app.config.from_envvar('EXTERNAL_CONFIG_FILE', silent=True)

    # blueprints
    app.register_blueprint(recipe.bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()