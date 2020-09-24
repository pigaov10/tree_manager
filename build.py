import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models.tree import configure as config_db_tree
from models.specie import configure as config_db_specie
from models.group import configure as config_db_group
from models.harvest import configure as config_db_harvest


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sq.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')

    from routes import bp_trees
    app.register_blueprint(bp_trees)

    config_db_tree(app)
    # config_db_specie(app)
    # config_db_group(app)
    # config_db_harvest(app)
    Migrate(app, app.db)

    return app