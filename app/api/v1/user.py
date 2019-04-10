# -*- coding: utf-8 -*-
# Time    : 2019/4/1 21:37
# Author  : LiaoKong

from flask import jsonify, g

from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint("user")


@api.route("/<int:uid>", methods=["GET"])
@auth.login_required
def supper_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()

    return jsonify(user)


@api.route("", methods=["GET"])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()

    return jsonify(user)


@api.route("/<int:uid>", methods=["DELETE"])
@auth.login_required
def supper_delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()

    return DeleteSuccess()


@api.route("", methods=["DELETE"])
@auth.login_required
def delete_user():
    uid = g.user.uid

    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()

    return DeleteSuccess()
