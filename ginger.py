# -*- coding: utf-8 -*-
# Time    : 2019/4/1 21:28
# Author  : LiaoKong

from app.app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
