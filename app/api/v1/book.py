# -*- coding: utf-8 -*-
# Time    : 2019/4/1 21:37
# Author  : LiaoKong

from app.libs.redprint import Redprint

api = Redprint("book")


@api.route("", methods=["GET"])
def get_book():
    return "get book"


@api.route("", methods=["POST"])
def create_book():
    return "create book"
