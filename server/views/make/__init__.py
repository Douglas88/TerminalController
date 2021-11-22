import io
import json
import os
import zipapp
from flask import Blueprint, request, render_template, jsonify
from config import SPEED, cache

make = Blueprint('make', __name__, template_folder=".")


@make.route("/make", methods=['GET', 'POST'])
def __make():
    if request.method == "GET":
        return render_template('make.html')
    else:
        data = json.loads(request.data)
        app_file = open("app.py", "r", encoding="utf8")
        with open("../client/__main__.py", "w", encoding="utf8") as f:
            code = app_file.read().replace("#SERVER_ADDRESS", data["address"])
            f.write(code)
        if data["target"] == "linux":
            temp = io.BytesIO()
            zipapp.create_archive('../client', temp, '/usr/bin/env python3', compressed=True)
            with open('../buildout/linux', 'wb') as f:
                f.write(temp.getvalue())
            os.remove("../client/__main__.py")
            return jsonify({"code": 0, "msg": "创建成功 ---> buildout/linux"})
        elif data["target"] == "win":
            temp = io.BytesIO()
            zipapp.create_archive('../client', temp, 'python.exe', compressed=True)
            with open('../buildenv/nginx.jpg', 'wb') as f:
                f.write(temp.getvalue())
            os.remove("../client/__main__.py")
            return jsonify({"code": 0, "msg": "请手动运行目录下的 build.cmd 进行cab编译打包,一直点下一步"})