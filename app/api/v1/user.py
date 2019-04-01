# -*- coding: utf-8 -*-
# Time    : 2019/4/1 21:37
# Author  : LiaoKong

from app.libs.redprint import Redprint

api = Redprint("user")


@api.route("/get")
def get_user():
    return "i am liaokong"
