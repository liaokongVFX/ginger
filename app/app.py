# -*- coding: utf-8 -*-
# Time    : 2019/4/1 21:28
# Author  : LiaoKong

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, "keys") and hasattr(o, "__getitem__"):
            return dict(o)

        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1

    app.register_blueprint(create_blueprint_v1(), url_prefix="/v1")


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)

    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.setting")
    app.config.from_object("app.config.secure")

    register_blueprints(app)
    register_plugin(app)

    return app
