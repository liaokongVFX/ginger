# -*- coding: utf-8 -*-
# Time    : 2019/4/3 21:48
# Author  : LiaoKong

from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = "ok"
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = "sorry,we made a mistake!"
    error_code = 999


class ClientTypeError(APIException):
    # 400 请求参数错误
    # 401 未授权
    # 403 禁止访问
    # 404 没有找到资源或者页面
    # 500 服务器未知错误
    # 301/302 重定向
    # 200 查询成功
    # 201 创建成功/更新成功
    # 204 删除成功

    code = 400
    msg = "Client is invalid"
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = "invalid parameter"
    error_code = 1000
